from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Widget-Examples")
        widget = QLabel("Hello")
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        # ToDo: 0x0001 | 0x0010 => 0x0011; 0x0001 & 0x0010 => 0x0000
        widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.setCentralWidget(widget)
        self.setFixedSize(QSize(200, 40))

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()