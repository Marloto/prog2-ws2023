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
        if not self.polylines.get(id):
            newInstance = Polyline(id) # Konstruktor
            self.polylines[id] = newInstance # Referenz im Dict hinterlegen
        poly = self.polylines[id]
        poly.add_position(pos)

    def list_positions(self, id: int) -> list:
        """Gibt alle Positionen zu der Polyline mit der passenden ID zurück"""
        if not self.polylines.get(id):
            return [] # etwas als "Default" zurückgegeben, z.B. None, [], usw.
        poly = self.polylines[id]
        positions_list = poly.positions
        return positions_list

    def length(self, id: int) -> float:
        """Gibt die Länge der Polyline mit der ID zurück"""
        pass
        # Was passiert, wenn die ID nicht existiert?
        if not self.polylines.get(id):
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

        if selection == "4":
            return

        id = input('ID: ')
        if selection == "1":
            positions = repo.list_positions(id)  # <- ToDo: Get list of all?
            if len(positions) == 0:
                print("Keine Einträge vorhanden")
            for i in positions:
                print(str(i))
        elif selection == "2":
            x = input('X: ')
            y = input('Y: ')
            pos = Position(float(x), float(y))
            # <- ToDo: add new position?
            repo.add_position(id, pos)
        elif selection == "3":
            length = repo.length(id) # <- ToDo: how to get length?
            if length == 0:
                print("Keine Länge vorhanden")
            else:
                print(f"Länge der Polyline: {length}")


# ------- Init Part ---------

repository = SimplePolylineRepository() # <- ToDo: Create Repository
run(repository)