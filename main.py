from inference import InferenceController
import msp_utils as msp
import serial
from time import sleep

print("Initializing FC connection...")
port = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

print("Initializing Coral and camera...")
controller = InferenceController()

# TODO: Create class for the MSP commands.
MSP_STATUS = 101
MSP_RC = 105
MSP_RAW_GPS = 106
MSP_SET_RAW_RC = 200

aux3_previous = 1000
aux4_previous = 1000

DEFAULT_ROLL = 1500
DEFAULT_PITCH = 1500
DEFAULT_THROTTLE = 1000
DEFAULT_YAW = 1500

AUX1 = 0
AUX2 = 0
AUX3 = 0
AUX4 = 0

msp.send_msp_request(port, MSP_STATUS)
code, payload = msp.read_msp_response(port)
assert code == MSP_STATUS
print(f'MSP_STATUS: {msp.process_MSP_STATUS(list(payload))}')


print("Ready...")
try:
    while True:
        msp.send_msp_request(port, MSP_RC)
        code, payload = msp.read_msp_response(port)
        assert code == MSP_RC

        rc_state = msp.process_MSP_RC(payload)
        print(f'RC: {rc_state}')

        aux3_current = rc_state['aux3']
        aux4_current = rc_state['aux4']

        if aux3_previous == 1000 and aux3_current == 1503:
            print('Taking photo...')
            controller.take_and_infer_still()

        # TODO: Take video until remote control changes away from 2000
        if aux3_previous == 1000 and aux3_current == 2000:
            print("Taking video...")
            controller.stream_and_infer_video()

        # TODO: Create class for the autopilot
        if aux4_previous == 1000 and aux4_current == 1503:
            print('Preparing autopilot...')

            # ROLL/PITCH/THROTTLE/YAW/AUX1/AUX2/AUX3/AUX4
            data = [DEFAULT_ROLL, DEFAULT_PITCH, DEFAULT_THROTTLE, DEFAULT_YAW, AUX1, AUX2, AUX3, AUX4]

            msp.send_msp_command(port, MSP_SET_RAW_RC, data)
            msp_command_id, payload = msp.read_msp_response(port)
            assert msp_command_id == MSP_SET_RAW_RC
            print('Successfully prepared autopilot')

        elif aux4_previous == 1503 and aux4_current == 2000:
            print('Starting flight...')

            # ROLL/PITCH/THROTTLE/YAW/AUX1/AUX2/AUX3/AUX4
            data = [DEFAULT_ROLL, DEFAULT_PITCH + 20, DEFAULT_THROTTLE + 100, DEFAULT_YAW, AUX1, AUX2, AUX3, AUX4]

            msp.send_msp_command(port, MSP_SET_RAW_RC, data)
            msp_command_id, payload = msp.read_msp_response(port)
            assert msp_command_id == MSP_SET_RAW_RC

        # Update values
        aux3_previous = aux3_current
        aux4_previous = aux4_current

        sleep(1)
except KeyboardInterrupt:
    controller.camera.close()

"""

    
    
"""