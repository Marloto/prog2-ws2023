from PyQt6.QtCore import Qt,QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QCheckBox
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Widget-Examples")
        widget = QCheckBox()
        widget.setCheckState(Qt.CheckState.Checked)
        widget.stateChanged.connect(self.show_state)
        self.setCentralWidget(widget)
        self.setFixedSize(QSize(200, 40))
    def show_state(self, state):
        print(state)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()