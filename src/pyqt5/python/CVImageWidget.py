# Image widget used to display image captured from opencv

from PyQt5 import QtCore, QtGui, QtWidgets, QtOpenGL
import cv2

class CVImageWidget(QtOpenGL.QGLWidget):
    def __init__(self, parent):
        super(QtOpenGL.QGLWidget, self).__init__()

    def render(self, matBGR):
        matRGB = cv2.cvtColor(matBGR, cv2.COLOR_BGR2RGB)
        image = QtGui.QImage(matRGB, matRGB.shape[1], matRGB.shape[0], QtGui.QImage.Format_RGB888)
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.drawImage(0, 0, image)
        painter.end()
