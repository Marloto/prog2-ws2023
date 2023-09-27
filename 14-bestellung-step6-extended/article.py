from persist import Persist

class Artikel:
    def __init__(self, Artikel_ID: int, Artikel_Name: str, Artikel_Preis: float):
        self.__Artikel_ID = Artikel_ID
        self.__Artikel_Name = Artikel_Name
        self.__Artikel_Preis = Artikel_Preis

    def get_id(self):
        return self.__Artikel_ID

    def get_name(self):
        return self.__Artikel_Name

    def set_name(self, name):
        self.__Artikel_Name = name

    def get_preis(self):
        return self.__Artikel_Name

    def __str__(self):
        return f"Der Artikel {self.__Artikel_Name} mit der ID {self.__Artikel_ID} hat einen Preis von  {self.__Artikel_Preis} €"

class Elektroartikel(Artikel):
    def __init__(self, Artikel_ID: int, Artikel_Name: str, Artikel_Preis: float, Artikel_Energieklasse: str):
        Artikel.__init__(self, Artikel_ID, Artikel_Name, Artikel_Preis)
        self.__Artikel_Energieklasse = Artikel_Energieklasse
    def get_energieklasse(self):
        return self.__Artikel_Energieklasse

class Kleidungsartikel(Artikel):
    def __init__(self, Artikel_ID: int, Artikel_Name: str, Artikel_Preis: float, Artikel_Groesse: str):
        Artikel.__init__(self, Artikel_ID, Artikel_Name, Artikel_Preis)
        self.__Artikel_Groesse = Artikel_Groesse
    def get_groesse(self):
        return self.__Artikel_Groesse

# Repositories
# -> Software-Entwicklungswerkzeugen, Git / Svn "Repository" Quellcode-Repository, das nicht!
# -> Sammlung von bestimmten Daten darstellen in Form eines "Repositories"
#    -> CRUD (Create, Read, Update, Delete)
class ArticleRepository:
    def create_article(self, article: Artikel):
        pass
#    def get_article(self):
#        pass
    def list_article(self) -> list:
        pass

class SimpleArticleRepository(ArticleRepository):
    def __init__(self, persister : Persist):
        self.persister = persister
    def create_article(self, a: Artikel):
        if type(a) == Artikel:
            self.persister.save_article(a.get_id(), a.get_name(), a.get_preis())
        elif type(a) == Elektroartikel:
            self.persister.save_article(a.get_id(), a.get_name(), a.get_preis(), electro_class = a.get_energieklasse())
        elif type(a) == Kleidungsartikel:
            self.persister.save_article(a.get_id(), a.get_name(), a.get_preis(), size = a.get_groesse())
    def list_article(self) -> list:
        articles = []
        article_rows = self.persister.load_articles()
        for article_row in article_rows:
            if article_row[3]:
                articles.append(Elektroartikel(int(article_row[0]), article_row[1], float(article_row[2]), article_row[3]))
            elif article_row[4]:
                articles.append(Kleidungsartikel(int(article_row[0]), article_row[1], float(article_row[2]), article_row[4]))
            else:
                articles.append(Artikel(int(article_row[0]), article_row[1], float(article_row[2])))
        return articles