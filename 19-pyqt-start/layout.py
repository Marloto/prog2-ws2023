from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QLabel, QRadioButton
import sys

# ToDo: Aufgabe -> erweitern Sie das MainWindow um weitere (bereits bekannte) Widgets

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window,
            QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")
        layout = QHBoxLayout()
        sub = QVBoxLayout()
        layout.addWidget(Color('red'))
        layout.addLayout(sub)
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))
        sub.addWidget(QRadioButton("Python"))

        widget2 = QLabel("Some Text")
        sub.addWidget(widget2)
        font = widget2.font()
        font.setPointSize(45)
        widget2.setFont(font)


        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
