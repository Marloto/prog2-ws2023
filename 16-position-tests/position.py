import math


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

    def length(self) -> float:
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


class SimplePolylineRepository(PolylineRepository):
    def __init__(self):
        PolylineRepository.__init__(self)
        self.polylines = {} # enthält alle Polyline-Objekte, als Key kommt die ID zum Einsatz, als Value die Objekt-Referenzen

    def add_position(self, id: int, pos: Position):
        """Fügt eine Position zur Polyline mit der ID hinzu, wenn die ID nicht existiert, dann soll eine neue Polyline entstehen"""
        if not self.polylines.get(id):
            newInstance = Polyline(id) # Konstruktor
            self.polylines[id] = newInstance # Referenz im Dict hinterlegen
        poly = self.polylines[id]
        poly.add_position(pos)
        self.notify()

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
