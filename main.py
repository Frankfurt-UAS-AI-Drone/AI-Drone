from inference import InferenceController
import threading
import msp
import serial
from time import sleep

print("Initializing FC connection...")
port = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

msp.send_msp_request(port, msp.Command.MSP_STATUS)
code, payload = msp.read_msp_response(port)
assert code == msp.Command.MSP_STATUS
print(f'MSP_STATUS: {msp.process_MSP_STATUS(list(payload))}')

print("Initializing Coral and camera...")
controller = InferenceController()

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

video_thread = None

print("Ready...")
try:
    while True:
        msp.send_msp_request(port, msp.Command.MSP_RC)
        code, payload = msp.read_msp_response(port)
        assert code == msp.Command.MSP_RC

        rc_state = msp.process_MSP_RC(payload)
        print(f'RC: {rc_state}')

        aux3_current = rc_state['aux3']
        aux4_current = rc_state['aux4']

        if video_thread and aux3_current != 2000:
            print("Stop recording...")
            controller.stop_event.set()
            video_thread.join(timeout=2)
            video_thread = None

        if aux3_previous == 1000 and aux3_current == 1503:
            print('Taking photo...')
            controller.take_and_infer_still()

        # TODO: Take video until remote control changes away from 2000
        if aux3_previous == 1000 and aux3_current == 2000:
            print("Taking video...")
            video_thread = threading.Thread(target=controller.stream_and_infer_video)
            video_thread.start()
           
        # TODO: Create class for the autopilot
        if aux4_previous == 1000 and aux4_current == 1503:
            print('Preparing autopilot...')

            # ROLL/PITCH/THROTTLE/YAW/AUX1/AUX2/AUX3/AUX4
            data = [DEFAULT_ROLL, DEFAULT_PITCH, DEFAULT_THROTTLE, DEFAULT_YAW, AUX1, AUX2, AUX3, AUX4]

            msp.send_msp_command(port, msp.Command.MSP_SET_RAW_RC, data)
            msp_command_id, payload = msp.read_msp_response(port)
            assert msp_command_id == msp.Command.MSP_SET_RAW_RC
            print('Successfully prepared autopilot')

        elif aux4_previous == 1503 and aux4_current == 2000:
            print('Starting flight...')

            # ROLL/PITCH/THROTTLE/YAW/AUX1/AUX2/AUX3/AUX4
            data = [DEFAULT_ROLL, DEFAULT_PITCH + 20, DEFAULT_THROTTLE + 100, DEFAULT_YAW, AUX1, AUX2, AUX3, AUX4]

            msp.send_msp_command(port, msp.Command.MSP_SET_RAW_RC, data)
            msp_command_id, payload = msp.read_msp_response(port)
            assert msp_command_id == msp.Command.MSP_SET_RAW_RC

        # Update values
        aux3_previous = aux3_current
        aux4_previous = aux4_current

        sleep(1)
except KeyboardInterrupt:
    controller.camera.close()