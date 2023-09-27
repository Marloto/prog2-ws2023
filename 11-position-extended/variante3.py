import math

# ------- Business Logic Part ---------

class Position:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x} / {self.y}'


class Polyline:
    def __init__(self, id: int):
        self.positions = []
        self.id = id

    def add_position(self, pos: Position):
        self.positions.append(pos)

    def length(self):
        if len(self.positions) < 2:
            return 0
        overall = 0
        for i in range(1, len(self.positions)):
            p1 = self.positions[i - 1]
            p2 = self.positions[i]
            distance = math.sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y))
            overall = overall + distance
        return overall

    def __str__(self):
        res = ""
        for p in self.positions:
            res = f'{res}\n  {str(p)}'
        return f'Positions from {self.id}:{res}\nLength: {self.length()}'


class PolylineRepository:
    def add_position(self, id: int, pos: Position):
        """Fügt eine Position zur Polyline mit der ID hinzu, wenn die ID nicht existiert, dann soll eine neue Polyline entstehen"""
        pass
    def list_positions(self, id: int) -> list:
        """Gibt alle Positionen zu der Polyline mit der passenden ID zurück"""
        pass
    def length(self, id: int) -> float:
        """Gibt die Länge der Polyline mit der ID zurück"""
        pass

# <- ToDo: Implement InMemory-Solution for PositionRepository-Interface

# Schnittstellen sollen nur Operationen definieren, keine Konstruktoren und keine Attribute
# -> in PolylineRepository initialisieren und vererben
# -> in SimplePolylineRepository initialisieren, wo? im Konstruktor!

class SimplePolylineRepository(PolylineRepository):
    def __init__(self):
        self.polylines = {} # enthält alle Polyline-Objekte, als Key kommt die ID zum Einsatz, als Value die Objekt-Referenzen

    def add_position(self, id: int, pos: Position):
        """Fügt eine Position zur Polyline mit der ID hinzu, wenn die ID nicht existiert, dann soll eine neue Polyline entstehen"""
        if not self.polylines[id]:
            newInstance = Polyline(id) # Konstruktor
            self.polylines[id] = newInstance # Referenz im Dict hinterlegen
        poly = self.polylines[id]
        poly.add_position(pos)

    def list_positions(self, id: int) -> list:
        """Gibt alle Positionen zu der Polyline mit der passenden ID zurück"""
        if not self.polylines[id]:
            return [] # etwas als "Default" zurückgegeben, z.B. None, [], usw.
        poly = self.polylines[id]
        positions_list = poly.positions
        return positions_list

    def length(self, id: int) -> float:
        """Gibt die Länge der Polyline mit der ID zurück"""
        pass
        # Was passiert, wenn die ID nicht existiert?
        if not self.polylines[id]:
            return 0
        # Wie kommt man an die Instanz mit passenden ID
        poly = self.polylines[id]
        # Wo kommt die Länge her? Methode length -> poly.length()
        length = poly.length()
        return length

# ------- Console Part ---------

def run(repo: PolylineRepository):
    while True:
        print("(1) Auflisten")
        print("(2) Erweitern")
        print("(3) Länge ausgeben")
        print("(4) Beenden")
        selection = input()

        if selection == "1":
            id = input('ID: ')
            posisitions = []  # <- ToDo: Get list of all?
            for i in posisitions:
                print(str(i))
        elif selection == "2":
            id = input('ID: ')
            x = input('X: ')
            y = input('Y: ')
            pos = Position(float(x), float(y))
            # <- ToDo: add new position?
        elif selection == "3":
            length = 0 # <- ToDo: how to get length?
            print(f"Länge der Polyline: {length}")
        elif selection == "4":
            return


# ------- Init Part ---------

repository = SimplePolylineRepository() # <- ToDo: Create Repository
run(repository)