import csv

class Artikel:
    def __init__(self, Artikel_ID: int, Artikel_Name: str, Artikel_Preis: float):
        self.Artikel_ID = Artikel_ID
        self.Artikel_Name = Artikel_Name
        self.Artikel_Preis = Artikel_Preis
        print("Artikel angelegt")
    def auflistung(self):
        pass

    def __str__(self):
        return f"Der Artikel {self.Artikel_Name} mit der ID {self.Artikel_ID} hat einen Preis von  {self.Artikel_Preis} €"


def Speicher():
    def __init__ (self):
        pass



article = []
try:
    with open("articles.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for row in reader:
            article.append(Artikel(int(row[0]), row[1], float(row[2])))
except FileNotFoundError:
    pass

while True:
    # Den Nutzer zwischen Auflisten und Hinzufügen
    # auswählen lassen?
    print("(1) Auflisten")
    print("(2) Hinzufügen")
    auswahl = input()

    if auswahl == "1":
        for i in article:
            print(str(i))
    elif auswahl == "2":
        article.append(Artikel(
            input('ID: '),
            input('Name: '),
            input('Preis: ')))
        with open("articles.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            [writer.writerow([a.Artikel_ID, a.Artikel_Name, a.Artikel_Preis]) for a in article]



