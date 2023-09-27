# Klassen sollten für die Erweiterung offen sein, aber für Änderungen geschlossen werden

# Abstrakte Klasse Figure
class Figure:
    def draw(self):
        pass

class Circle(Figure):
    def __init__(self):
        pass
    def draw(self):
        print("Zeichen :D")

class Rectangle(Figure):
    def __init__(self):
        pass
    def draw(self):
        print("Rechteckig...")

class Triangle(Figure):
    def __init__(self):
        pass
    def draw(self):
        print("Dreickig...")

class GraphicEditor:
    def draw(self, figure: Figure):
        figure.draw()

graphics = GraphicEditor()
graphics.draw(Circle())
graphics.draw(Rectangle())
graphics.draw(Triangle())


# class GraphicEditor:
#     def drawCircle(self):
#         # ...
#         pass
#     def drawRectangle(self):
#         pass
# graphics = GraphicEditor()
# graphics.drawCircle()
# graphics.drawRectangle()