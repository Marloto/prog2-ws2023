import math


class Position:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x} / {self.y}'


class Polyline:
    def __init__(self):
        self.positions = []

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
        return f'Positionen:{res}\nLänge: {self.length()}'


poly = Polyline()
poly.add_position(Position(0, 0))
poly.add_position(Position(10, 0))
poly.add_position(Position(10, 10))
print(poly)