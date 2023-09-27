
# Python-Module sind Singleton's
# -> "datei.py"
# -> Warum ist das eine Art Singleton? Weil Module nur einmal "Ausgeführt werden", danach immer nur auf Methoden zugriffen

# import a
# import b

# Klasse mit nur einer Objekt-Instanz
# -> Statische Methoden

class ExampleClass:
    def normalMethod(self):
        print("Normal!")
    @staticmethod
    def doSomething(): # <- self fehlt!
        print("Hello, World!")

# Statische Methoden sind methoden, die ohne Objekt-Referenzen
# aufgerufen werden können und sollen


ExampleClass.doSomething() # Aufruf einer statischen Methode

ref1 = ExampleClass() # Normaler Aufruf mit Objekt-Referenz
ref1.normalMethod()