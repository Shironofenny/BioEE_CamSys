import sys
import PyQt5
from CameraSys import CameraSys

if __name__ == "__main__":
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    window = CameraSys()
    window.show()
    app.exec_()
