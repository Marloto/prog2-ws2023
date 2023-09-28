# Start der Anwendung und Konfiguration von Schnittstellen-Implementierungen

from persist import CsvPersist
from article import SimpleArticleRepository
from customer import SimpleCustomerRepository
from console import start_article_console, start_customer_console
from app import start_app

persister = CsvPersist("articles.csv", "customers.csv")


articleRepository = SimpleArticleRepository(persister)
customerRepository = SimpleCustomerRepository(persister)

start_app(articleRepository, customerRepository)

# while True:
#     print("(1) Artikel")
#     print("(2) Kunden")
#     mode = input()
#     if mode == "1":
#         start_article_console(articleRepository)
#     elif mode == "2":
#         start_customer_console(customerRepository)
