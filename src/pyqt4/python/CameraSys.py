from PyQt4 import QtCore, QtGui
import cv2
from threading import Thread

import UI
from Camera import Camera

class CameraSys(QtGui.QMainWindow):
    def __init__(self):
        super(QtGui.QMainWindow, self).__init__()

        self.ui = UI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.cam = Camera()

        # Loading constants
        self.displaySize = (720, 405)

        # Local signals
        self.stopFlag = False

        self.bondInteraction()

    def bondInteraction(self):
        self.ui.pbCapture.clicked.connect(self.display)
        self.ui.pbStop.clicked.connect(self.release)

    def display(self):
        print("Reading incoming stream")
        while True :
            frame = self.cam.captureOnce()
            frame480 = cv2.resize(frame, self.displaySize)
            self.ui.cviVideo.render(frame480)

            if self.stopFlag :
                break

        print("Stop reading from incoming stream")
    
    def release(self):
        self.stopFlag = True
        self.cam.release()
        cv2.destroyAllWindows()
