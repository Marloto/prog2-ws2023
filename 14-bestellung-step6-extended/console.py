# Implementierung der Nutzerinteraktion über die Konsole

from article import Artikel, Elektroartikel, Kleidungsartikel, ArticleRepository
from customer import Kunde, Adresse, CustomerRepository


def start_article_console(repository : ArticleRepository):
    while True:
        print("(1) Auflisten")
        print("(2) Hinzufügen")
        print("(3) Zurück")
        selection = input()

        if selection == "1":
            for i in repository.list_article(): # <- verwendung von persist für laden
                print(str(i))
        elif selection == "2":
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
        elif selection == "3":
            return

def start_customer_console(repository: CustomerRepository):
    while True:
        print("(1) Auflisten")
        print("(2) Hinzufügen")
        print("(3) Zurück")
        selection = input()

        if selection == "1":
            for i in repository.list_customers():
                print(str(i))
        elif selection == "2":
            count = int(input("Adressen: "))

            customer = Kunde()
            for i in range(0, count):
                address = Adresse(
                    input('Name: '),
                    input('Strasse: '),
                    input('PLZ: '),
                    input('Ort: '))
                customer.add_adresse(address)

            repository.create_customer(customer)
        elif selection == "3":
            return