class Artikel:
    def __init__(self, Artikel_ID: int, Artikel_Name: str, Artikel_Preis: float):
        self.Artikel_ID = Artikel_ID
        self.Artikel_Name = Artikel_Name
        self.Artikel_Preis = Artikel_Preis
    def auflistung(self):
        pass

    def __str__(self):
        return f"Der Artikel {self.Artikel_Name} mit der ID {self.Artikel_ID} hat einen Preis von  {self.Artikel_Preis} €"

class Elektroartikel(Artikel):
    def __init__(self, Artikel_ID: int, Artikel_Name: str, Artikel_Preis: float, Artikel_Energieklasse: str):
        Artikel.__init__(self, Artikel_ID, Artikel_Name, Artikel_Preis)
        self.Artikel_Energieklasse = Artikel_Energieklasse

class Kleidungsartikel(Artikel):
    def __init__(self, Artikel_ID: int, Artikel_Name: str, Artikel_Preis: float, Artikel_Groesse: str):
        Artikel.__init__(self, Artikel_ID, Artikel_Name, Artikel_Preis)
        self.Artikel_Groesse = Artikel_Groesse

# Repositories
# -> Software-Entwicklungswerkzeugen, Git / Svn "Repository" Quellcode-Repository, das nicht!
# -> Sammlung von bestimmten Daten darstellen in Form eines "Repositories"
#    -> CRUD (Create, Read, Update, Delete)
class ArticleRepository:
    def create_article(self):
        pass
    def get_article(self):
        pass
    def list_article(self):
        pass

class CsvArticleRepository(ArticleRepository):
    pass