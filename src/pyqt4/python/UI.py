# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/camsys.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(900, 720)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(560, 0))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.cviVideo = CVImageWidget(self.widget)
        self.cviVideo.setMinimumSize(QtCore.QSize(560, 315))
        self.cviVideo.setMaximumSize(QtCore.QSize(560, 315))
        self.cviVideo.setObjectName(_fromUtf8("cviVideo"))
        self.verticalLayout.addWidget(self.cviVideo)
        self.cviPhoto = CVImageWidget(self.widget)
        self.cviPhoto.setMinimumSize(QtCore.QSize(560, 315))
        self.cviPhoto.setMaximumSize(QtCore.QSize(560, 315))
        self.cviPhoto.setObjectName(_fromUtf8("cviPhoto"))
        self.verticalLayout.addWidget(self.cviPhoto)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pbCapture = QtGui.QPushButton(self.widget_2)
        self.pbCapture.setObjectName(_fromUtf8("pbCapture"))
        self.verticalLayout_2.addWidget(self.pbCapture)
        self.pbStop = QtGui.QPushButton(self.widget_2)
        self.pbStop.setObjectName(_fromUtf8("pbStop"))
        self.verticalLayout_2.addWidget(self.pbStop)
        self.horizontalLayout.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pbCapture.setText(_translate("MainWindow", "Capture", None))
        self.pbStop.setText(_translate("MainWindow", "Stop", None))

from CVImageWidget import CVImageWidget
