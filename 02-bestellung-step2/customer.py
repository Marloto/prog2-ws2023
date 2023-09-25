import csv

class Kunden:

    def __init__(self, Name, Strasse, PLZ, Ort):
        self.Name = Name
        self.Strasse = Strasse
        self.PLZ = PLZ
        self.Ort = Ort

kunden = []
def save():
    with open("kundendaten.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for kunde in kunden:
            writer.writerow([kunde.Name, kunde.Strasse, kunde.PLZ, kunde.Ort])

try:
    with open("Kundendaten.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for row in reader:
            kunden.append(Kunden(row[0], row[1], row[2], row[3], row[4]))
except FileNotFoundError:
    pass

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
        kunden.append(Kunden(
            input('Name: '),
            input('Strasse: '),
            input('PLZ: '),
            input('Ort: ')))


