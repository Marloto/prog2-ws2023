from PyQt6.QtCore import Qt,QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, \
    QWidget, QGridLayout
import sys

from article import ArticleRepository, Artikel
from customer import CustomerRepository

def start_app(article_repo: ArticleRepository, customer: CustomerRepository):

    class ArticleListWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Artikelliste")
            self.refresh_view()

        def refresh_view(self):

            main = QGridLayout()
            # main.addWidget(widget, row, col)

            article_list = article_repo.list_article()

            main.addWidget(QLabel("ID"), 0, 0)
            main.addWidget(QLabel("Name"), 0, 1)
            main.addWidget(QLabel("Preis"), 0, 2)

            i = 1
            for article in article_list:
                id_label = QLabel(str(article.get_id()))
                name_label = QLabel(str(article.get_name()))
                preis_label = QLabel(str(article.get_preis()))

                # ToDo: Wie könnte das in das GridLayout hinzugefügt werden?
                main.addWidget(id_label, i, 0)
                main.addWidget(name_label, i, 1)
                main.addWidget(preis_label, i, 2)
                i = i + 1

            open_add_window = QPushButton("Hinzufügen")
            open_add_window.clicked.connect(self.handle_add)
            main.addWidget(open_add_window, i, 0, 1, 3)

            widget = QWidget()
            widget.setLayout(main)
            self.setCentralWidget(widget)

        def handle_add(self):
            self.add_window = ArticleAddWindow(self)
            self.add_window.show()


    class ArticleAddWindow(QMainWindow):
        def __init__(self, list: ArticleListWindow):
            super().__init__()
            self.list = list
            self.setWindowTitle("Artikel hinzufügen")

            # Widgets
            idLabel = QLabel("ID")
            idLabel.setMinimumWidth(50)
            nameLabel = QLabel("Name")
            nameLabel.setMinimumWidth(50)
            preisLabel = QLabel("Preis")
            preisLabel.setMinimumWidth(50)

            self.idInput = QLineEdit()
            self.nameInput = QLineEdit()
            self.preisInput = QLineEdit()

            saveButton = QPushButton("Speichern")
            saveButton.clicked.connect(self.handle_save)

            # Layout
            main = QVBoxLayout()
            hl1 = QHBoxLayout()
            hl2 = QHBoxLayout()
            hl3 = QHBoxLayout()
            hl4 = QHBoxLayout()

            # Verknüpfen
            main.addLayout(hl1)
            main.addLayout(hl2)
            main.addLayout(hl3)
            main.addLayout(hl4)

            hl1.addWidget(idLabel)
            hl1.addWidget(self.idInput)

            hl2.addWidget(nameLabel)
            hl2.addWidget(self.nameInput)

            hl3.addWidget(preisLabel)
            hl3.addWidget(self.preisInput)

            hl4.addWidget(saveButton)

            widget = QWidget()
            widget.setLayout(main)
            self.setCentralWidget(widget)

        def handle_save(self):
            id = int(self.idInput.text())
            name = self.nameInput.text()
            preis = float(self.preisInput.text())
            # Hinweis: das kann schiefgehen, wenn der Nutzer keine Zahlen eingibt
            #  -> Spezielle Widgets für Zahleneingaben, oder man müsste mit try-expect

            a1 = Artikel(id, name, preis)
            article_repo.create_article(a1)

            self.list.refresh_view()

            self.close()

    app = QApplication(sys.argv)

    window = ArticleListWindow()
    window.show()

    app.exec()