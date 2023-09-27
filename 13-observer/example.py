
# Abstrakte Klasse
class Observer:
    def update(self):
        pass

class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self):
        for o in self.observers:
            o.update()


class Schalter(Subject):
    def __init__(self):
        Subject.__init__(self)
        self.state = False

    def toggle(self):
        if self.state:
            print("Ausschalten")
            self.state = False
            self.notify() # irgendwo muss notify aufgerufen, typischer weise immer
                          # wenn sich attribute ändern
        else:
            print("Eingeschaltet")
            self.state = True
            self.notify()


class Lampe:
    def __init__(self):
        self.staerke = 0.0

    def set_staerke(self, staerke: float):
        self.staerke = staerke
        print(str(self))

    def __str__(self):
        return f"Lampe leuchtet mit {self.staerke}"


class Heizungssteuerung:
    def __init__(self):
        self.temperatur = 20

    def set_temperatur(self, value: float):
        self.temperatur = value
        print(str(self))

    def __str__(self):
        return f"Temperatur ist bei {self.temperatur}"


class SimpleLampSwitchObserver(Observer):
    def __init__(self, schalter: Schalter, lampe: Lampe):
        self.schalter = schalter
        self.lampe = lampe
        self.schalter.attach(self)

    def update(self):
        if self.schalter.state:
            self.lampe.set_staerke(1)
        else:
            self.lampe.set_staerke(0)


class SimpleHeizungsSwitchObserver(Observer):
    def __init__(self, schalter: Schalter, heizung: Heizungssteuerung):
        self.schalter = schalter
        self.heizung = heizung
        self.schalter.attach(self)

    def update(self):
        if self.schalter.state:
            self.heizung.set_temperatur(25)
        else:
            self.heizung.set_temperatur(20)

schalter1 = Schalter()
schalter2 = Schalter()

lampe1 = Lampe()
lampe2 = Lampe()

temperatur1 = Heizungssteuerung()

SimpleLampSwitchObserver(schalter1, lampe1)
SimpleLampSwitchObserver(schalter2, lampe1)
SimpleHeizungsSwitchObserver(schalter1, temperatur1)

SimpleLampSwitchObserver(schalter1, lampe2)
SimpleLampSwitchObserver(schalter2, lampe2)

schalter1.toggle()
schalter1.toggle()
schalter2.toggle()
schalter2.toggle()

# Mögliche Erweiterung: Lampe und Heizungssteuerung werden ebenfalls Subjects
# -> dann könnte man auch beliebiger auf Veränderungen reagieren