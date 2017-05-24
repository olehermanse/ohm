import sys
from PyQt5 import QtWidgets
from ui_mainwindow import Ui_MainWindow as MainWindowBuilder

class MainWindow(QtWidgets.QMainWindow):
    """Like QMainWindow, but with custom behavior on window events"""
    def __init__(self):
        super().__init__()
        # This class is empty for now, but will include event functions, e.g.:
        # on_resize, on_quit, on_focus

class App():
    """The main application class.

    contains GUI (the window), data struccture, actions etc.

    Todo:
        * Can make a separate GUI class if needed
    """

    def __init__(self):
        """Initializes a Qt Application and builds GUI inside a main window"""
        self.qt_app = QtWidgets.QApplication(sys.argv)
        self.window = MainWindow()

        # Build GUI using generated python file:
        self.builder = MainWindowBuilder()
        self.builder.setupUi(self.window)

        # Add our functions to GUI actions:
        self.connect_actions(self.builder)

    def start(self):
        """Show the window, execute Qt app, return Qt app exit code"""
        self.window.show()
        exit_code = self.qt_app.exec_()
        sys.exit(exit_code)

    def connect_actions(self, builder):
        """Register behavior(functions) with GUI events/actions"""

        # General actions:
        builder.actionSave.triggered.connect(self.save)
        builder.actionLoad.triggered.connect(self.load)

        # Push button:
        builder.cmd_button.clicked.connect(self.run)

        # Line Edit text field:
        builder.cmd_text.returnPressed.connect(self.run)

    def save(self):
        print("SAVE")

    def load(self):
        print("LOAD")

    def run(self):
        print("RUN: " + self.builder.cmd_text.text())
        self.builder.cmd_text.clear()

if __name__ == '__main__':
    app = App()
    app.start()
