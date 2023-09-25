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

class Elektroartikel(Artikel):
    def __init__(self, Artikel_ID: int, Artikel_Name: str, Artikel_Preis: float, Artikel_Energieklasse: str):
        Artikel.__init__(self, Artikel_ID, Artikel_Name, Artikel_Preis)
        self.Artikel_Energieklasse = Artikel_Energieklasse

class Kleidungsartikel(Artikel):
    def __init__(self, Artikel_ID: int, Artikel_Name: str, Artikel_Preis: float, Artikel_Groesse: str):
        Artikel.__init__(self, Artikel_ID, Artikel_Name, Artikel_Preis)
        self.Artikel_Groesse = Artikel_Groesse

article = []
with open("articles.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in reader:
        if row[3]:
            article.append(Elektroartikel(int(row[0]), row[1], float(row[2]), row[3]))
        elif row[4]:
            article.append(Kleidungsartikel(int(row[0]), row[1], float(row[2]), row[4]))
        else:
            article.append(Artikel(int(row[0]), row[1], float(row[2])))

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

        print("(1) Default")
        print("(2) Kleidung")
        print("(3) Elektro")
        typ = input()

        if typ == "1":
            article.append(Artikel(
                input('ID: '),
                input('Name: '),
                input('Preis: ')))
        elif typ == "2":
            article.append(Kleidungsartikel(
                input('ID: '),
                input('Name: '),
                input('Preis: '),
                input('Groesse: ')))
        elif typ == "3":
            article.append(Elektroartikel(
                input('ID: '),
                input('Name: '),
                input('Preis: '),
                input('Energieklasse: ')))

        with open("articles.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            #[writer.writerow([a.Artikel_ID, a.Artikel_Name, a.Artikel_Preis]) for a in article]
            # [writer.writerow([a]) for a in article]
            for a in article:
                if type(a) == Artikel:
                    writer.writerow([a.Artikel_ID, a.Artikel_Name, a.Artikel_Preis, "", ""])
                elif type(a) == Elektroartikel:
                    writer.writerow([a.Artikel_ID, a.Artikel_Name, a.Artikel_Preis, a.Artikel_Energieklasse, ""])
                elif type(a) == Kleidungsartikel:
                    writer.writerow([a.Artikel_ID, a.Artikel_Name, a.Artikel_Preis, "", a.Artikel_Groesse])





