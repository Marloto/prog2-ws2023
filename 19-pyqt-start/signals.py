from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        self.n = 0
        self.button = QPushButton(f"Klicks: {self.n}")
        self.button.clicked.connect(self.wurde_geklickt)
        self.button.pressed.connect(self.wurde_gedrueckt)
        self.button.released.connect(self.wurde_loesgelassen)
        self.button.toggled.connect(self.wurde_gewechselt)
        # self.button.setCheckable(True)
        self.setCentralWidget(self.button)

    def wurde_geklickt(self):
        # jedes mal, wenn man den button klickt, soll der Inhalt von PushButton raufgezählt werden
        print("Geklickt")
        self.n = self.n + 1
        self.button.setText(f"Klicks: {self.n}")

    def wurde_gedrueckt(self):
        print("Gedrueckt")

    def wurde_loesgelassen(self):
        print("Losgelassen")

    def wurde_gewechselt(self):
        print("Gewechselt")



window = MainWindow()
window.show()

app.exec()
