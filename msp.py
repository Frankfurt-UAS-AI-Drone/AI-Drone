import serial
import struct
import time
from time import sleep

# https://gist.github.com/reefwing/e9ba13aed51e83cb7245bb4e55b84dea

port = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

MSP_STATUS = 101
MSP_RC = 105
MSP_RAW_GPS = 106
MSP_SET_RAW_RC = 200

DEFAULT_ROLL = 1500
DEFAULT_PITCH = 1500
DEFAULT_THROTTLE = 1000
DEFAULT_YAW = 1500

AUX1 = 0
AUX2 = 0
AUX3 = 0
AUX4 = 0

def send_msp_request(serial_port, msp_command_id):
    header = b'$M<'
    length = 0
    checksum = get_checksum(msp_command_id, bytes([]))

    msp_package = header + struct.pack('<BB', length, msp_command_id) + bytes([checksum])
    serial_port.write(msp_package)

def get_checksum(msp_command_id, payload):
    checksum = 0
    length = len(payload)

    for byte in bytes([length, msp_command_id]) + payload:
        checksum ^= byte
    
    checksum &= 0xFF
    return checksum

def send_msp_command(serial_port, msp_command_id, data):
    payload = bytearray()
    for value in data:
        payload += struct.pack('<1H', value)

    header = b'$M<'
    length = len(payload)
    checksum = get_checksum(msp_command_id, payload)

    msp_package = header + bytes([length, msp_command_id]) + payload + bytes([checksum])
    serial_port.write(msp_package)

def read_msp_response(serial_port):
    response = serial_port.readline()
    if response.startswith(b'$M>'):
        length = response[3]
        msp_command_id = response[4]
        payload = response[5:5 + length]
        return msp_command_id, payload
    else:
        raise ValueError("Invalid MSP response")
    
# TODO: Copypasted from YAMSPY
def readbytes(data, size=8, unsigned=False, read_as_float=False):
        """Unpack bytes according to size / type

        Parameters
        ----------
        data : bytearray
            Data to be unpacked
        size : int, optional
            Number of bits (8, 16 or 32) (default is 8)
        unsigned : bool, optional
            Indicates if data is unsigned or not (default is False)
        read_as_float: bool, optional
            Indicates if data is read as float or not (default is False)
            
        Returns
        -------
        int
            unpacked bytes according to input options
        """
        buffer = bytearray()

        for _ in range(int(size/8)):
            buffer.append(data.pop(0))
        
        if size==8:
            unpack_format = 'b'
        elif size==16:
            if read_as_float: # for special situations like MSP2_INAV_DEBUG
                unpack_format = 'e'
            else:   
                unpack_format = 'h'
        elif size==32:
            if read_as_float: # for special situations like MSP2_INAV_DEBUG
                unpack_format = 'f'
            else:
                unpack_format = 'i'
        
        if unsigned:
            unpack_format = unpack_format.upper()

        return struct.unpack('<' + unpack_format, buffer)[0]

def process_MSP_STATUS(data):
    cycleTime = readbytes(data, size=16, unsigned=True)
    i2cError = readbytes(data, size=16, unsigned=True)
    activeSensors = readbytes(data, size=16, unsigned=True)
    mode = readbytes(data, size=32, unsigned=True)
    profile = readbytes(data, size=8, unsigned=True)

    return {
        'cycleTime': cycleTime,
        'i2cError': i2cError,
        'activeSensors': activeSensors,
        'mode': mode,
        'profile': profile,
    }

def process_MSP_RAW_GPS(data):
    fix = readbytes(data, size=8, unsigned=True)
    numSat = readbytes(data, size=8, unsigned=True)
    lat = readbytes(data, size=32, unsigned=False)
    lon = readbytes(data, size=32, unsigned=False)
    alt = readbytes(data, size=16, unsigned=True)
    speed = readbytes(data, size=16, unsigned=True)
    ground_course = readbytes(data, size=16, unsigned=True)

    print(locals())

def process_msp_rc(data):
    rc_chs = struct.unpack('<' + 'H' * (len(data) // 2), data)

    return {
        'roll': rc_chs[0],
        'pitch': rc_chs[1],
        'yaw': rc_chs[2],
        'throttle': rc_chs[3],
        'aux1': rc_chs[4],
        'aux2': rc_chs[5],
        'aux3': rc_chs[6],
        'aux4': rc_chs[7],
    }

def take_photo():
    from picamera2 import Picamera2
    import cv2
    from pycoral.adapters import common, detect
    from pycoral.utils.edgetpu import make_interpreter

    # Initialize camera
    picam2 = Picamera2()
    picam2.start()
    time.sleep(2)  # Allow camera to warm up

    # Initialize the model
    interpreter = make_interpreter('effdet_lite3.tflite')
    interpreter.allocate_tensors()
    # Set size to fit the model.
    size = common.input_size(interpreter)

    # Capture and resize frame
    frame = picam2.capture_array()
    resized_frame = cv2.resize(frame, size)

    if resized_frame.shape[2] == 4:
        resized_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGRA2BGR)

    common.set_input(interpreter, resized_frame)
    interpreter.invoke()

    objects = detect.get_objects(interpreter, score_threshold=0.5)

    for obj in objects:
        bbox = obj.bbox
        cv2.rectangle(resized_frame, (bbox.xmin, bbox.ymin), (bbox.xmax, bbox.ymax), (0, 255, 0), 2)
        cv2.putText(resized_frame, f'{obj.id} {obj.score:.2f}', (bbox.xmin, bbox.ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Save the image using OpenCV
    cv2.imwrite("test_image.jpg", resized_frame)

    picam2.close()
    print("Image saved as test_image.jpg")

send_msp_request(port, MSP_STATUS)
code, payload = read_msp_response(port)
assert code == MSP_STATUS
print(f'MSP_STATUS: {process_MSP_STATUS(list(payload))}')

send_msp_request(port, MSP_RAW_GPS)
code, payload = read_msp_response(port)
assert code == MSP_RAW_GPS
print(f'GPS: {list(payload)}')
process_MSP_RAW_GPS(list(payload))

# TODO: Remove
exit(0)

aux3_previous = 1000
aux4_previous = 1000

while True:
    send_msp_request(port, MSP_RC)
    code, payload = read_msp_response(port)
    assert code == MSP_RC

    rc_state = process_msp_rc(payload)
    print(f'RC: {rc_state}')

    aux3_current = rc_state['aux3']
    aux4_current = rc_state['aux4']

    if aux3_previous == 1000 and aux3_current == 1503:
        print('Taking photo...')
        take_photo()
    
    if aux4_previous == 1000 and aux4_current == 1503:
        print('Preparing autopilot...')

        # ROLL/PITCH/THROTTLE/YAW/AUX1/AUX2/AUX3/AUX4
        data = [DEFAULT_ROLL, DEFAULT_PITCH, DEFAULT_THROTTLE, DEFAULT_YAW, AUX1, AUX2, AUX3, AUX4]

        send_msp_command(port, MSP_SET_RAW_RC, data)
        msp_command_id, payload = read_msp_response(port)
        assert msp_command_id == MSP_SET_RAW_RC
        print('Successfully prepared autopilot')
    elif aux4_previous == 1503 and aux4_current == 2000:
        print('Starting flight...')

        # ROLL/PITCH/THROTTLE/YAW/AUX1/AUX2/AUX3/AUX4
        data = [DEFAULT_ROLL, DEFAULT_PITCH + 250, DEFAULT_THROTTLE + 200, DEFAULT_YAW, AUX1, AUX2, AUX3, AUX4]

        send_msp_command(port, MSP_SET_RAW_RC, data)
        msp_command_id, payload = read_msp_response(port)
        assert msp_command_id == MSP_SET_RAW_RC

    # Update values
    aux3_previous = aux3_current
    aux4_previous = aux4_current

    sleep(2)

# aux3_raw = int(autopilot.state['aux3'])
# autopilot_mode = autopilot.state['bee_state']

# if aux3_raw == 1000:
#     autopilot_mode = 'OFF'
# elif aux3_raw == 1503:
#     mavs.prepare_go_forward(previous_throttle)
#     time.sleep(0.1)
# elif aux3_raw == 2000:
#     autopilot_mode = 'READY'

# if autopilot_mode != autopilot.state['bee_state']:
#     autopilot.state['bee_state'] = autopilot_mode
#     messages.display(
#                 messages.bee_state_changed_to, [autopilot_mode])
#     command_queue.queue.clear()
