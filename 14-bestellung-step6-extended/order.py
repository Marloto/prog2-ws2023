import csv
from customer import Adresse, Kunde
from article import Artikel

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
