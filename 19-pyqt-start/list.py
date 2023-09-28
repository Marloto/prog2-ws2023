from PyQt6.QtCore import Qt,QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Widget-Examples")
        widget = QListWidget()
        widget.addItems(["One", "Two", "Three", "Four"])
        self.setCentralWidget(widget)
        self.setFixedSize(QSize(200, 40))

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()