from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QMainWindow
import sys

app = QApplication(sys.argv)

class MyButton(QPushButton):
    def __init__(self, msg: str):
        super().__init__(msg)

    def mouseMoveEvent(self, e):
        self.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        self.setText("mousePressEvent")
        print(str(e.position()))
        print(str(e.button()))

    def mouseReleaseEvent(self, e):
        self.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.setText("mouseDoubleClickEvent")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = MyButton("Click in this window")
        self.setCentralWidget(self.button)
        self.setWindowTitle("Hello World")



window = MainWindow()
window.show()

app.exec()
