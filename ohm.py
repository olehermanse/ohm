import sys
from PyQt5 import QtGui, uic, QtWidgets
import mainwindow

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        #uic.loadUi('mainwindow.ui', self)
        #self.show()

def save():
    print("SAVE")

def load():
    print("LOAD")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window_design = mainwindow.Ui_MainWindow()
    window_design.setupUi(window)
    window_design.actionSave.triggered.connect(save)
    window_design.actionLoad.triggered.connect(load)
    window.show()
    sys.exit(app.exec_())
