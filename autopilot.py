import msp

class AutopilotController():
    def __init__(self, serial_port):
        self.serial_port = serial_port
        self.DEFAULT_ROLL = 1500
        self.DEFAULT_PITCH = 1500
        self.DEFAULT_THROTTLE = 1000
        self.DEFAULT_YAW = 1500
        self.AUX1 = 0
        self.AUX2 = 0
        self.AUX3 = 0
        self.AUX4 = 0

    def override_rc(self, roll, pitch, throttle, yaw, aux1, aux2, aux3, aux4):  
        data = [roll, 
                pitch, 
                throttle, 
                yaw, 
                aux1, aux2, aux3, aux4]

        msp.send_msp_command(self.serial_port, msp.Command.MSP_SET_RAW_RC, data)
        
        msp_command_id, payload = msp.read_msp_response(self.serial_port)

        if msp_command_id == msp.Command.MSP_SET_RAW_RC:
            return True
        return False

    def prepare(self):
        status = self.override_rc(
            self.DEFAULT_ROLL,
            self.DEFAULT_PITCH,
            self.DEFAULT_THROTTLE,
            self.DEFAULT_YAW, 
            self.AUX1, self.AUX2, self.AUX3, self.AUX4) 

        return status 

    def go_forward(self):
        status = self.override_rc(
            self.DEFAULT_ROLL,
            self.DEFAULT_PITCH + 20, 
            self.DEFAULT_THROTTLE + 100, 
            self.DEFAULT_YAW, 
            self.AUX1, self.AUX2, self.AUX3, self.AUX4) 

        return status
    