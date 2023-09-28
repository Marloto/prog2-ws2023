from PyQt6.QtCore import Qt,QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QRadioButton, QHBoxLayout, QButtonGroup, QWidget,QLabel
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        box = QHBoxLayout()
        group = QButtonGroup()
        for i in range(1,4):
            button = QRadioButton(f'#{i}')
            group.addButton(button)
            box.addWidget(button)
            button.toggled.connect(self.handle_changed)

        self.setWindowTitle("Widget-Examples")
        widget = QWidget()
        widget.setLayout(box)
        self.setCentralWidget(widget)
        self.setFixedSize(QSize(400, 40))
    def handle_changed(self, value):
        button = self.sender()
        print(f'{button.text()}: {button.isChecked()}')

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()