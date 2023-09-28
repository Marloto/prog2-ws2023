class ToDo:
    pass

class ToDoRepository:
    def create(self, title: str):
        """Erzeugt eine neue ToDo-Objekten mit einer noch nicht vergegebenen ID"""
        pass
    def get_all(self) -> list:
        """Liefert eine Liste mit allen ToDo-Objekten"""
        pass
    def get_by_id(self, id: int) -> ToDo:
        """Liefert ein ToDo mit der entsprechenden ID, liefert None, wenn die ID nicht existiert"""
        pass
    def mark_as_done(self, id: int):
        """Sucht nach dem ToDo mit der entsprechenden ID und setzt done auf True"""
        pass