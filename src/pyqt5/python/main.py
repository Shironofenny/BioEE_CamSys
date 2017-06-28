import sys
import PyQt4
from CameraSys import CameraSys

if __name__ == "__main__":
    app = PyQt4.QtGui.QApplication(sys.argv)
    window = CameraSys()
    window.show()
    app.exec_()
