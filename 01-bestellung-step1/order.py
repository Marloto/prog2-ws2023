class Bestellung:
    def __init__(self, Bestellungsnumer, Datum, Liefer):
        self.Bestellungsnummer = Bestellungsnumer
        self.Datum = Datum
        self.Liefer = Liefer
    def __str__(self):
        return f'{self.Bestellungsnummer}, {self.Datum}, {self.Liefer}'

Bestellung_Liste = []

# Bestellung_Liste.append(Bestellung(12, '09.09.22', '10.09.22'))
# Bestellung_Liste.append(Bestellung(13, '10.09.22', '11.09.22'))
while True:
    # Den Nutzer zwischen Auflisten und Hinzufügen
    # auswählen lassen?
    print("(1) Auflisten")
    print("(2) Hinzufügen")
    auswahl = input()

    if auswahl == "1":
        for i in Bestellung_Liste:
            print(str(i))
    elif auswahl == "2":
        Bestellung_Liste.append(Bestellung(
            input('Bestellungsnummer: '),
            input('Datum: '),
            input('Geplante Lieferzeitpunkt: ')))
