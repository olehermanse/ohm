import sys
from PyQt5 import QtGui, uic, QtWidgets
from mainwindow import Ui_MainWindow

class Gui():
    def __init__(self):
        self.window = QtWidgets.QMainWindow()
        self.builder = MainWindowBuilder(self.window, self)

    def show(self):
        self.window.show()

    def save(self):
        print("SAVE")

    def load(self):
        print("LOAD")

    def run(self):
        print("RUN: " + self.builder.cmd_text.text())
        self.builder.cmd_text.clear()

class MainWindowBuilder(Ui_MainWindow):
    def __init__(self, target, gui):
        Ui_MainWindow.__init__(self)
        self.setupUi(target)
        self.actionSave.triggered.connect(gui.save)
        self.actionLoad.triggered.connect(gui.load)
        self.cmd_button.clicked.connect(gui.run)
        self.cmd_text.returnPressed.connect(gui.run)

class App():
    def __init__(self):
        pass

    def start(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.gui = Gui()
        self.gui.show()
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    app = App()
    app.start()
