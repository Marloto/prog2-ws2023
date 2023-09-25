import csv

class Adresse:
    def __init__(self, Name, Strasse, PLZ, Ort):
        self.Name = Name
        self.Strasse = Strasse
        self.PLZ = PLZ
        self.Ort = Ort
    def __str__(self):
        return f'{self.Name}, {self.Strasse}, {self.PLZ} {self.Ort}'

class Kunde:
    def __init__(self):
        self.Adressen = []

    def add_adresse(self, adresse):
        self.Adressen.append(adresse)

    def __str__(self):
        return f'{str(self.Adressen)}'
