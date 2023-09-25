import csv
from customer import Adresse, Kunde
from article import Artikel

# Bestellung braucht jetzt eine Rechnungsadresse, eine Lieferadresse, einen Verweisen auf den Kunden und je Bestellung mehrere Positionen, die Artikel verweisen

class BestellPosition:
    def __init__(self, anzahl: int, artikel: Artikel):
        self.anzahl = anzahl
        self.artikel = artikel

class Bestellung:
    def __init__(self, Bestellungsnumer, Datum, Liefer, Kunde : Kunde, Lieferadresse : Adresse, Rechnungsadresse : Adresse):
        self.Bestellungsnummer = Bestellungsnumer
        self.Datum = Datum
        self.Liefer = Liefer
        self.Lieferadresse = Lieferadresse
        self.Kunde = Kunde
        self.Rechnungsadresse = Rechnungsadresse
        self.Positionen = []

    def add_position(self, bestell_position: BestellPosition):
        self.Positionen.append(bestell_position)

    def __str__(self):
        return f'{self.Bestellungsnummer}, {self.Datum}, {self.Liefer}'


Bestellung_Liste = []

def save():
    # ToDo bisher ungetestet
    for element in Bestellung_Liste:
        with open("orders.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            spaltenListe = [element.Datum, element.Liefer, element.Bestellungsnummer,
                            element.Lieferadresse.Name, element.Lieferadresse.Strasse, element.Lieferadresse.PLZ, element.Lieferadresse.Ort,
                            element.Rechnungsadresse.Name, element.Rechnungsadresse.Strasse, element.Rechnungsadresse.PLZ, element.Rechnungsadresse.Ort]
            for pos in element.Positionen:
                spaltenListe.append(pos.anzahl)
                spaltenListe.append(pos.artikel.Artikel_Name)
            writer.writerow(spaltenListe)

with open("orders.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in reader:
        kunde = None # ToDo wie Kunden wiederfinden?
        lieferadresse = Adresse(row[3], row[4], row[5], row[6])
        rechnungsadresse = Adresse(row[7], row[8], row[9], row[10])
        bestellung = Bestellung(row[2], row[0], row[1], kunde, lieferadresse, rechnungsadresse)
        for i in range(11, len(row), 2):
            artikel = None # ToDo wie Artikel wiederfinden?
            bestellung.add_position(BestellPosition(row[i], artikel))
        Bestellung_Liste.append(bestellung)

while True:
    print("(1) Auflisten")
    print("(2) Hinzufügen")
    print("(3) Break")
    auswahl = input()

    if auswahl == "1":
        for i in Bestellung_Liste:
            print(str(i))
    elif auswahl == "2":
        # ToDo: Kunde auswählen
        # ToDo: Adressen von ausgewählten Kunden auswählen
        # ToDo: BestellPosition

        Bestellung_Liste.append(Bestellung(
            input('Bestellungsnummer: '),
            input('Datum: '),
            input('Geplante Lieferzeitpunkt: ')))
        save()
    elif auswahl == "3":
        break

