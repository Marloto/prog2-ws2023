from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Widget-Examples")
        widget = QComboBox()
        widget.addItems(["One", "Two", "Three"])
        widget.textActivated.connect(self.show_selection)
        self.setCentralWidget(widget)
        self.setFixedSize(QSize(200, 40))
    def show_selection(self, selection):
        print(selection)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()