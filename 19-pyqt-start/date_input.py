from PyQt6.QtCore import QDate, QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QDateEdit
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Widget-Examples")
        widget = QDateEdit()
        widget.dateChanged.connect(self.handle_input)
        self.setCentralWidget(widget)
        self.setFixedSize(QSize(200, 40))
    def handle_input(self, value:QDate):
        print(f'{str(value.day())}.{str(value.month())}.{str(value.year())}')

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()