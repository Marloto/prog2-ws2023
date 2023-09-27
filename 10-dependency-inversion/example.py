# Schnittstelle
class LampenSteuerung:
    def leuchtStaerke(self, wert: float):
        pass

class Lampe(LampenSteuerung):
    def __init__(self):
        pass
    def leuchtStaerke(self, wert: float):
        print(f'Lampe ist auf {wert}')

class Schalter:
    def __init__(self, lampe : LampenSteuerung):
        self.lampe = lampe
        self.status = False
    def toggle(self):
        if not self.status:
            self.status = True
            self.lampe.leuchtStaerke(1.0)
        else:
            self.status = False
            self.lampe.leuchtStaerke(0.0)


lampe1 = Lampe()
schalter1 = Schalter(lampe1)
schalter1.toggle()
schalter1.toggle()