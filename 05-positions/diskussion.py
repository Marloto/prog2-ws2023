from math import sqrt


class Position:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x} / {self.y}"


class Polyline:
    def __init__(self):
        self.positions = [] #referenziert ein Objekt vom Typ liste

    def add_position(self, p: Position):
        self.positions.append(p) # Je Element in der Liste (self.positions[0], usw.) steckt ein Objekt vom Typ Position

    def length(self):
        if len(self.positions) < 2:
            return 0

        overall = 0
        for i in range(0, len(self.positions) - 1):
            p1 = self.positions[i]  # Objekt von der Klasse Position
            p2 = self.positions[i + 1]
            x = p1.x - p2.x
            y = p1.y - p2.y
            distance = sqrt(x * x + y * y)
            overall = overall + distance

        return overall

    def __str__(self):
        # Alle Positionen und die Länge der Polyline (über length)
        current_length = self.length()
        return f'{str([str(p) for p in self.positions])}, Länge: {current_length}'

        # current_length = self.length()
        # res = ""
        # for p in self.positions:
        #     res = f'{res}\n  {str(p)}'
        # return f'Position:{res}\nLänge: {current_length}'


poly = Polyline()
poly.add_position(Position(0, 0))
poly.add_position(Position(10, 0))
poly.add_position(Position(10, 10))
print(poly)