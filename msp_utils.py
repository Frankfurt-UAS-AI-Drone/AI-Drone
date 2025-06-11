import struct

# https://gist.github.com/reefwing/e9ba13aed51e83cb7245bb4e55b84dea

# BEGIN Send and receive MSP commands. Taken from: https://github.com/under0tech/autopilot_bee_ept/blob/main/msp_helper.py
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
        print(response)
        raise ValueError("Invalid MSP response")

# BEGIN Processing MSP responses. Taken from: https://github.com/thecognifly/YAMSPy/blob/7adda7953645d2e4d619075e4d8232c91a289049/yamspy/__init__.py
def readbytes(data, size=8, unsigned=False, read_as_float=False):
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

    return {

    }

def process_MSP_RC(data):
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