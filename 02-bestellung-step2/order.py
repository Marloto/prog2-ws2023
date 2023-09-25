import csv


class Bestellung:
    def __init__(self, Bestellungsnumer, Datum, Liefer):
        self.Bestellungsnummer = Bestellungsnumer
        self.Datum = Datum
        self.Liefer = Liefer

    def __str__(self):
        return f'{self.Bestellungsnummer}, {self.Datum}, {self.Liefer}'


Bestellung_Liste = []

def save():
    for element in Bestellung_Liste:
        with open("orders.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            spaltenListe = [element.Datum, element.Liefer, element.Bestellungsnummer]
            writer.writerow(spaltenListe)

try:
    with open("orders.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for row in reader:
            Bestellung_Liste.append(Bestellung(row[2], row[0], row[1]))
except FileNotFoundError:
    pass

while True:
    # Den Nutzer zwischen Auflisten und Hinzufügen
    # auswählen lassen?
    print("(1) Auflisten")
    print("(2) Hinzufügen")
    print("(3) Break")
    auswahl = input()

    if auswahl == "1":
        for i in Bestellung_Liste:
            print(str(i))
    elif auswahl == "2":
        Bestellung_Liste.append(Bestellung(
            input('Bestellungsnummer: '),
            input('Datum: '),
            input('Geplante Lieferzeitpunkt: ')))
        save()
    elif auswahl == "3":
        break

