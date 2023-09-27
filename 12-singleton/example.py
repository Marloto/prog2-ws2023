# Singleton > einzeln = eine Objekt instanz
# -> im gesamten System eine einzige Objekt Instanz von der Klasse geben soll
# -> sicherstellen das man nur ein Objekt erzeugt
# -> einen eleganten Weg finden, damit man schnell an diese eine Instanz heran kommt


# Was wären Ideen, wenn ich Methode hätte, die ohne Objekt-Referenz
# genutzt werden können?

class SingletonExample:
    @staticmethod
    def get_instance():
        return ref

ref = SingletonExample()