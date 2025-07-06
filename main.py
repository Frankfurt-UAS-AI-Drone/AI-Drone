from inference import InferenceController
from autopilot import AutopilotController
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
video_thread = None

print("Initializing Autopilot...")
autopilot = AutopilotController(serial_port=port)

aux3_previous = 1000
aux4_previous = 1000

prepared = False

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

        # Stop video stream if AUX4 switches away from 2000 
        if video_thread and aux3_current != 2000:
            print("Stop recording...")
            controller.stop_event.set()
            video_thread.join(timeout=2)
            video_thread = None

        if aux3_previous == 1000 and aux3_current == 1503:
            print('Taking photo...')
            controller.take_and_infer_still()

        if aux3_previous == 1000 and aux3_current == 2000:
            print("Taking video...")
            video_thread = threading.Thread(target=controller.stream_and_infer_video)
            video_thread.start()
           
        if aux4_previous == 1000 and aux4_current == 1503:
            print('Preparing autopilot...')
            prepared = autopilot.prepare()

            if prepared:           
                print('Successfully prepared autopilot')
            else: 
                #TODO: Implement abort sequence (i.e. switching back to user control or disarming.)
                print("Preparation unsuccessful")

        elif aux4_previous == 1503 and aux4_current == 2000:
            print('Starting flight...')
            autopilot.go_forward()

        # Update values
        aux3_previous = aux3_current
        aux4_previous = aux4_current

        sleep(1)

except KeyboardInterrupt:
    controller.camera.close()