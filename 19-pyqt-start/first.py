from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys

# QApplication -> ist Anwendung
app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        button = QPushButton("Do Something...")
        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(button)


# Ein Fenster erzeugen mittels "irgend ein Widget"
window = MainWindow()
# das erzeugte Widget als Fenster starten
window.show()

# Haupt-Schleife zur Verarbeitung von Nutzerereignissen gestartet werden
# -> while True: holt irgendwie vom System "ereignisse"
app.exec()
