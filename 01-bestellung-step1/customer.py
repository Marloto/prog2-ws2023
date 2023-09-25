class Kunden:

    def __init__(self, Name, Strasse, PLZ, Ort):
        self.Name = Name
        self.Strasse = Strasse
        self.PLZ = PLZ
        self.Ort = Ort

kunden = []
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