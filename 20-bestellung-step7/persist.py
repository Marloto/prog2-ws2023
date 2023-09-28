import csv

# Ziel: Wir definieren die Schnittstelle zum speichern und laden in unserem System
class Persist:
    # Was für Methoden / Operationen wären für unser Beispiel zum Bestellsystem denkbar?
    def save_article(self, id: int, name: str, price: float, electro_class: str = "", size: str = ""):
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

    def save_article(self, id: int, name: str, price: float, electro_class: str = "", size: str = ""):
        with open("articles.csv", 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([id, name, price, electro_class, size])

    def load_articles(self) -> list:
        article = []
        try:
            with open(self.article_file, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=';', quotechar='"')
                for row in reader:
                    article.append(row)
        except FileNotFoundError:
            pass
        return article

    def load_customers(self) -> list:
        customers = []
        try:
            with open(self.customer_file, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=';', quotechar='"')
                for row in reader:
                    customer = []
                    for i in range(0, len(row), 4):
                        customer.append((row[i], row[i + 1], row[i + 2], row[i + 3]))
                    customers.append(customer)
        except FileNotFoundError:
            pass
        return customers

    def save_customer(self, adresses: list):
        with open(self.customer_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            row = []
            for adresse in adresses:
                row.append(adresse[0])
                row.append(adresse[1])
                row.append(adresse[2])
                row.append(adresse[3])
            writer.writerow(row)


# Weitere technische Realisierungen, die aber die selbe Schnittstellen-
# Definition verwenden
class JsonPersist(Persist): # JavaScript Object Notation
    pass

class MySqlPersist(Persist):
    pass