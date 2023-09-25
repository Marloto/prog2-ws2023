import csv
from article import Artikel, Elektroartikel, Kleidungsartikel
from customer import Kunde, Adresse

# Ziel: Wir definieren die Schnittstelle zum speichern und laden in unserem System
class Persist:
    # Was für Methoden / Operationen wären für unser Beispiel zum Bestellsystem denkbar?
    def save_article(self, article: Artikel):
        pass

    def load_articles(self) -> list:
        pass

    def save_customer(self, adresses: list):
        pass

    def load_customers(self) -> list:
        pass

    def save_order(self, bestellungsnumer: str, datum: str, lieferzeitpunkt: str):
        pass

    def load_orders(self) -> list:
        pass

class CsvPersist(Persist):
    def __init__(self, article_file: str, customer_file: str):
        self.article_file = article_file
        self.customer_file = customer_file

    def save_article(self, a : Artikel):
        with open("articles.csv", 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            if type(a) == Artikel:
                writer.writerow([a.Artikel_ID, a.Artikel_Name, a.Artikel_Preis, "", ""])
            elif type(a) == Elektroartikel:
                writer.writerow([a.Artikel_ID, a.Artikel_Name, a.Artikel_Preis, a.Artikel_Energieklasse, ""])
            elif type(a) == Kleidungsartikel:
                writer.writerow([a.Artikel_ID, a.Artikel_Name, a.Artikel_Preis, "", a.Artikel_Groesse])

    def load_articles(self) -> list:
        article = []
        try:
            with open(self.article_file, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=';', quotechar='"')
                for row in reader:
                    if row[3]:
                        article.append(Elektroartikel(int(row[0]), row[1], float(row[2]), row[3]))
                    elif row[4]:
                        article.append(Kleidungsartikel(int(row[0]), row[1], float(row[2]), row[4]))
                    else:
                        article.append(Artikel(int(row[0]), row[1], float(row[2])))
        except FileNotFoundError:
            pass
        return article

    def save_customer(self, adresses: list):
        with open(self.customer_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            row = []
            for adresse in adresses:
                row.append(adresse.Name)
                row.append(adresse.Strasse)
                row.append(adresse.PLZ)
                row.append(adresse.Ort)
            writer.writerow(row)

    def load_customers(self) -> list:
        customers = []
        try:
            with open(self.customer_file, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=';', quotechar='"')
                for row in reader:
                    customer = Kunde()
                    for i in range(0, len(row), 4):
                        customer.add_adresse(Adresse(row[i], row[i + 1], row[i + 2], row[i + 3]))
                    customers.append(customer)
        except FileNotFoundError:
            pass
        return customers


# Weitere technische Realisierungen, die aber die selbe Schnittstellen-
# Definition verwenden
class JsonPersist(Persist): # JavaScript Object Notation
    pass

class MySqlPersist(Persist):
    pass