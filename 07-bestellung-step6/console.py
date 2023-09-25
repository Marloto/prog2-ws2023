# Implementierung der Nutzerinteraktion über die Konsole

from article import Artikel, Elektroartikel, Kleidungsartikel, ArticleRepository


def start_article_console(repository : ArticleRepository):
    while True:
        # Den Nutzer zwischen Auflisten und Hinzufügen
        # auswählen lassen?
        print("(1) Auflisten")
        print("(2) Hinzufügen")
        auswahl = input()

        if auswahl == "1":
            for i in repository.list_article(): # <- verwendung von persist für laden
                print(str(i))
        elif auswahl == "2":

            print("(1) Default")
            print("(2) Kleidung")
            print("(3) Elektro")
            typ = input()

            article = None
            if typ == "1":
                article = Artikel(
                    input('ID: '),
                    input('Name: '),
                    input('Preis: '))
            elif typ == "2":
                article = Kleidungsartikel(
                    input('ID: '),
                    input('Name: '),
                    input('Preis: '),
                    input('Groesse: '))
            elif typ == "3":
                article = Elektroartikel(
                    input('ID: '),
                    input('Name: '),
                    input('Preis: '),
                    input('Energieklasse: '))
            repository.create_article(article) # <- verwendung von persist für speichern
