from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Widget-Examples")
        widget = QLineEdit()
        widget.textChanged.connect(self.handle_input)
        widget.setPlaceholderText("Enter your text")
        self.setCentralWidget(widget)
        self.setFixedSize(QSize(200, 40))
    def handle_input(self, value):
        print(value)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()