# Implementierung der Nutzerinteraktion über die Konsole

from persist import Persist
from article import Artikel, Elektroartikel, Kleidungsartikel


def start_article_console(persister : Persist):
    while True:
        # Den Nutzer zwischen Auflisten und Hinzufügen
        # auswählen lassen?
        print("(1) Auflisten")
        print("(2) Hinzufügen")
        auswahl = input()

        if auswahl == "1":
            for i in persister.list_articles(): # <- verwendung von persist für laden
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
                    size = input('Energieklasse: '))
            persister.save_article(article) # <- verwendung von persist für speichern


def start_consumer_console(persister : Persist):
    pass


def start_order_console(persister : Persist):
    pass