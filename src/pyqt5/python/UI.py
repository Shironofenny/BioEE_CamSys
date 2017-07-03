# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camsys.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(10, 9, 10, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.camPanel = QtWidgets.QWidget(self.centralwidget)
        self.camPanel.setMinimumSize(QtCore.QSize(560, 0))
        self.camPanel.setMaximumSize(QtCore.QSize(720, 16777215))
        self.camPanel.setObjectName("camPanel")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.camPanel)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cviCamera = CVImageWidget(self.camPanel)
        self.cviCamera.setMaximumSize(QtCore.QSize(560, 315))
        self.cviCamera.setObjectName("cviCamera")
        self.verticalLayout.addWidget(self.cviCamera)
        self.cviPhoto = CVImageWidget(self.camPanel)
        self.cviPhoto.setMaximumSize(QtCore.QSize(560, 315))
        self.cviPhoto.setObjectName("cviPhoto")
        self.verticalLayout.addWidget(self.cviPhoto)
        self.horizontalLayout.addWidget(self.camPanel)
        self.controlPanel = QtWidgets.QWidget(self.centralwidget)
        self.controlPanel.setObjectName("controlPanel")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.controlPanel)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pbCapture = QtWidgets.QPushButton(self.controlPanel)
        self.pbCapture.setObjectName("pbCapture")
        self.verticalLayout_2.addWidget(self.pbCapture)
        self.pbStop = QtWidgets.QPushButton(self.controlPanel)
        self.pbStop.setObjectName("pbStop")
        self.verticalLayout_2.addWidget(self.pbStop)
        self.horizontalLayout.addWidget(self.controlPanel)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pbCapture.setText(_translate("MainWindow", "Capture"))
        self.pbStop.setText(_translate("MainWindow", "Stop"))

from CVImageWidget import CVImageWidget
