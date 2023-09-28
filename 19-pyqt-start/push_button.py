from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Widget-Examples")
        widget = QPushButton("Button")
        widget.clicked.connect(self.handle_clicked)

        widget2 = QPushButton("Button2")
        widget2.clicked.connect(self.handle_clicked)

        self.setCentralWidget(widget)
        self.setCentralWidget(widget2)

    def handle_clicked(self):
        print('Clicked!')

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()