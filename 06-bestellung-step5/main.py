# Start der Anwendung und Konfiguration von Schnittstellen-Implementierungen

from persist import CsvPersist, JsonPersist, MySqlPersist
from console import start_article_console

persister = CsvPersist("articles.csv", "customers.csv")
# persister = JsonPersist()
# persister = MySqlPersist()

# ToDo wechsel zwischen Modus "Artikel", "Customer" und "Order"

start_article_console(persister)
