from PyQt6.QtCore import QDateTime, QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QDateTimeEdit
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Widget-Examples")
        widget = QDateTimeEdit()
        widget.dateTimeChanged.connect(self.handle_input)
        self.setCentralWidget(widget)
        self.setFixedSize(QSize(200, 40))
    def handle_input(self, value:QDateTime):
        print(f'{str(value.time().hour())}:{str(value.time().minute())}:{str(value.time().second())} {str(value.date().day())}.{str(value.date().month())}.{str(value.date().year())}')

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()