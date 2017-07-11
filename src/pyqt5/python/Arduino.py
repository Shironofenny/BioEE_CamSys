import serial

import Constant

class Arduino(object):

    def __init__(self):
        self.arduino = None
        self.port = Constant.ARD_PORT
        self.baudrate = Constant.ARD_BAUDRATE
        self.timeout = Constant.ARD_TIMEOUT

    def connect(self):
        try :
            self.arduino = serial.Serial(port = Constant.ARD_PORT, baudrate = Constant.ARD_BAUDRATE, timeout = Constant.ARD_TIMEOUT)
        except :
            print("SERIAL CONNECT: Arduino open unsucessful, please check the port that arduino is connected")
            return None

        while self.arduino.in_waiting == 0 :
            pass

        receivedData = self.arduino.readline()
        print("SERIAL CONNECT: " + receivedData)

    def turnOnLED(self):
        self.arduino.write('1')
        while self.arduino.in_waiting == 0 :
            pass
        self.arduino.readline()
        receivedData = self.arduino.readline()
        print("SERIAL LED ON: " + receivedData)

    def turnOffLED(self):
        self.arduino.write('0')
        while self.arduino.in_waiting == 0 :
            pass
        self.arduino.readline()
        receivedData = self.arduino.readline()
        print("SERIAL LED OFF: " + receivedData)

    def disconnect(self):
        if self.arduino.isOpen() :
            self.arduino.close()
            print("SERIAL DISCONNECT: Arduino disconnected")
        else :
            print("SERIAL DISCONNECT: No connected deivces found")
