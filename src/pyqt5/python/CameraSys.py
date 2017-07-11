from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import time
from datetime import datetime
from threading import Thread, Event, RLock

import UI
from Camera import Camera
from Arduino import Arduino
import Constant

class CameraSys(QtWidgets.QMainWindow):
    def __init__(self):
        super(QtWidgets.QMainWindow, self).__init__()

        # System internal flags
        self.isUIReady = False;
        self.isArduinoReady = False;
        self.isCameraReady = False;

        # Bring up the UI
        # If UI is not avaiable, then there is no point running this program any longer.
        try :
            self.ui = UI.Ui_MainWindow()
            self.ui.setupUi(self)
            self.isUIReady = True
        except Exception as e :
            print("MAIN: " + e)
            print("MAIN: Unknown error when setting up UI")
            QtCore.QCoreApplication.exit(-1)
            return

        self.ui.statusbar.showMessage("Initializing UI...")

        # Connecting to arduino
        # Program will carry on if no arduino is connected
        self.arduino = Arduino()
        self.arduino.connect()
        if None == self.arduino :
            print("MAIN: Arduino not found, LED related function will be turned off")
        else :
            self.isArduinoReady = True
            self.arduino.turnOffLED()

        # Loading constants
        self.displaySize = Constant.SCREEN_DISPLAY_RES

        # Open camera
        # Program will carry on even if there is no camera detected
        self.cam = Camera()

        # Threads
        # Camera thread control
        self.cameraThread = Thread(group = None, target = self.capture, name = "Camera System, Camera")
        self.cameraThreadKiller = Event()
        self.cameraLock = RLock()

        self.frame = None
        self.videoFrame = None

        # Flags remembering the startup initialization
        self.savePictureStartUpFlag = False
        self.startingTime = time.time()
        self.lastShotTime = time.time()

        # Control for picture saving
        self.ledOnTime = Constant.DEFAULT_LED_ON_TIME
        self.ledOffTime = Constant.DEFAULT_LED_OFF_TIME
        self.isLEDOn = False
        self.pictureSavingInterval = Constant.DEFAULT_SAVE_INTERVAL
        self.pictureSavingTimer = QtCore.QTimer(self)

        self.bondInteraction()

        # Display thread control (unfortunately this need to be within main thread)
        self.displayUpdater = Event()
        self.displayUpdater.clear()
        self.displayTimer = QtCore.QTimer(self)
        self.startDisplay()

        self.startCameraThread()
        self.startSavingPicture()

    def bondInteraction(self):
        pass
        #self.ui.pbCapture.clicked.connect(self.startSavingPicture)

    # Camera thread control functions:
    def startCameraThread(self):
        if not self.cameraThread.isAlive() :
            if not self.cam.isCameraOpened() :
                self.cam.openCamera()
            self.cameraThread = Thread(group = None, target = self.capture, name = "Camera System, Camera")

        try :
            self.cameraThread.start()
        except RuntimeError as e :
            print("Runtime Error: ({0}): {1}".format(e.errno, e.strerror))

    def stopCameraThread(self):
        self.cameraThreadKiller.set()

    # Capture thread function
    def capture(self):
        while not self.cameraThreadKiller.wait(0.001) :
            self.cameraLock.acquire()
            self.frame = self.cam.captureOnce()
            self.videoFrame = cv2.resize(self.frame, self.displaySize)
            self.cameraLock.release()
            self.displayUpdater.set()

        self.cam.release()
        self.cameraThreadKiller.clear()

    # Display control functions
    def startDisplay(self):
        if self.displayTimer.isActive() :
            self.displayTimer.stop()
        self.displayTimer.setInterval(0.001)
        self.displayTimer.setSingleShot(False)
        self.displayTimer.timeout.connect(self.display)
        self.displayTimer.start()

    def display(self) :
        if self.displayUpdater.isSet() :
            self.cameraLock.acquire()
            self.ui.cviCamera.render(self.videoFrame)
            self.displayUpdater.clear()
            self.cameraLock.release()

    # Picture saving function
    def startSavingPicture(self) :
        if self.pictureSavingTimer.isActive() :
            self.pictureSavingTimer.stop()
        self.pictureSavingTimer.setInterval(0.5)
        self.pictureSavingTimer.setSingleShot(False)
        self.pictureSavingTimer.timeout.connect(self.savePicture)
        self.pictureSavingTimer.start()

    def savePicture(self):
        if self.displayUpdater.isSet() :
            if self.savePictureStartUpFlag :
                self.lastShotTime = time.time()
            else :
                timeNow = time.time()
                if ( timeNow - self.lastShotTime ) > self.ledOnTime and not self.isLEDOn:
                    self.arduino.turnOnLED()
                    self.isLEDOn = True
                elif ( timeNow - self.lastShotTime ) > self.pictureSavingInterval :
                    filename = Constant.FILE_PREFIX + datetime.now().strftime('%m%d%yD%HH%MM') + '.png'
                    print("Saving capture to file" + filename)
                    self.cameraLock.acquire()
                    cv2.imwrite(filename, self.frame, [cv2.IMWRITE_PNG_COMPRESSION, Constant.PNG_COMPRESSION_LEVEL])
                    self.ui.cviPhoto.render(self.videoFrame)
                    self.cameraLock.release()
                    self.lastShotTime = timeNow
                    self.arduino.turnOffLED()
                    self.isLEDOn = False

    # Overriden close event
    def closeEvent(self, event) :
        self.stopCameraThread()
        self.arduino.disconnect()
        print("Closing event accepted")
        time.sleep(1)
        event.accept()
