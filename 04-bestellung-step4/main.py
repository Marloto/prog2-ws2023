from order import Bestellung, BestellPosition
from article import Artikel, Elektroartikel, Kleidungsartikel
from customer import Adresse, Kunde


adresse1 = Adresse("Max Musterman", "Musterstraße 1", 12345, "Musterstadt")
adresse2 = Adresse("Max Musterman", "Sonstwo 2", 99999, "Musterdorf")

kunde = Kunde()
kunde.add_adresse(adresse1)
kunde.add_adresse(adresse2)

artikel1 = Artikel(1, "Milch", 2.00)
artikel2 = Elektroartikel(2, "Kühlschrank", 400.00)
artikel3 = Kleidungsartikel(3, "T-Shirt", 19.99)

order = Bestellung("123", "09.09.2022", "14.09.2022", kunde, adresse1, adresse2)
order.add_position(BestellPosition(1, artikel2))
order.add_position(BestellPosition(10, artikel1))
order.add_position(BestellPosition(2, artikel3))