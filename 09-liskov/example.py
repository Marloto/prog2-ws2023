class A:
    pass

class B(A):
    pass

class C(B):
    pass

class Parent:
    def calculate(self, a: B, b: B) -> B:
        return None

class Child(Parent):
    def calculate(self, a: A, b: A) -> B:
        return None


var1 = Parent()
var2 = Child()

def usage(parent : Parent):
    erg = parent.calculate(2^31, 2^31) # int wertebereich ist anzunehmen...!


usage(var2)

# 1. Liskov: Wertebereiche für Rückgabeergebnisse sollten nicht den Wertebereich der Elternklasse sprengen, maximal kleiner werden
#            da an beliebigen Stellen, wo die Funktionalität genutzt wird, man nicht erwarten kann das man mit größeren Wertebereich
#            umgehen kann
#            -> Bei Klassenhierarchien kann der Datentyp des Rückgabewertes nicht genereller werden, maximal spezieller
# 2. Liskov: Wertebereiche der Parameter dürfen sich nicht verkleinern, sie müssen mindestens den Bereich verarbeiten können,
#            den auch die Eltern schon verarbeiten konnten. Eine Vergrößerung ist möglich.
#            -> Bei Klassenhierarchien können die Datentypen der Parameter nicht spezieller werden, maximal genereller

