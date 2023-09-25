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

kunden = []
def save():
    with open("kundendaten.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for kunde in kunden:
            row = []
            for adresse in kunde.Adressen:
                row.append(adresse.Name)
                row.append(adresse.Strasse)
                row.append(adresse.PLZ)
                row.append(adresse.Ort)
            writer.writerow(row)

try:
    with open("Kundendaten.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for row in reader:
            kunde = Kunde()
            for i in range(0, len(row), 4):
                kunde.add_adresse(Adresse(row[i], row[i + 1], row[i + 2], row[i + 3]))
            kunden.append(kunde)
except FileNotFoundError:
    print("Leere Datenbestand")

while True:
    # Den Nutzer zwischen Auflisten und Hinzufügen
    # auswählen lassen?
    print("(1) Auflisten")
    print("(2) Hinzufügen")
    auswahl = input()

    if auswahl == "1":
        for i in kunden:
            print(str(i))
    elif auswahl == "2":
        anzahl = int(input("Adressen: "))

        kunde = Kunde()
        for i in range(0, anzahl):
            adresse = Adresse(
                input('Name: '),
                input('Strasse: '),
                input('PLZ: '),
                input('Ort: '))
            kunde.add_adresse(adresse)

        kunden.append(kunde)
        save()


