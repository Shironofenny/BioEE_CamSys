from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import time
from datetime import datetime
from threading import Thread, Event, RLock

import UI
from Camera import Camera
import Constant

class CameraSys(QtWidgets.QMainWindow):
    def __init__(self):
        super(QtWidgets.QMainWindow, self).__init__()

        self.ui = UI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.cam = Camera()

        # Loading constants
        self.displaySize = Constant.SCREEN_DISPLAY_RES

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
        self.pictureSavingInterval = Constant.DEFAULT_SAVE_INTERVAL;
        self.pictureSavingTimer = QtCore.QTimer(self)

        self.bondInteraction()

        # Display thread control (unfortunately this need to be within main thread)
        self.displayUpdater = Event()
        self.displayUpdater.clear()
        self.displayTimer = QtCore.QTimer(self)
        self.startDisplay()

        self.startCameraThread()

    def bondInteraction(self):
        self.ui.pbCapture.clicked.connect(self.startSavingPicture)

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
                if ( timeNow - self.lastShotTime ) > self.pictureSavingInterval :
                    filename = Constant.FILE_PREFIX + datetime.now().strftime('%m%d%yD%HH%MM') + '.png'
                    print("Saving capture to file" + filename)
                    self.cameraLock.acquire()
                    cv2.imwrite(filename, self.frame, [cv2.IMWRITE_PNG_COMPRESSION, Constant.PNG_COMPRESSION_LEVEL])
                    self.ui.cviPhoto.render(self.videoFrame)
                    self.cameraLock.release()
                    self.lastShotTime = timeNow

    # Overriden close event
    def closeEvent(self, event) :
        self.stopCameraThread()
        print("Closing event accepted")
        time.sleep(1)
        event.accept()
