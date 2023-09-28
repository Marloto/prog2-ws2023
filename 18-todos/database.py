class DatabaseAccess:
    def save(self, id: int, title: str, done: bool):
        """Speichert einen ToDo, dieser könnte bereits existieren und muss in diesem Fall aktualisiert werden"""
        pass
    def load(self) -> list:
        """Lädt alle ToDos, liefert eine Liste. Jeder Eintrag ist ein Tupel mit (id, titel, done)"""
        pass