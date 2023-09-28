from persist import Persist

class Adresse:
    def __init__(self, Name, Strasse, PLZ, Ort):
        self.Name = Name
        self.Strasse = Strasse
        self.PLZ = PLZ
        self.Ort = Ort
    def __str__(self):
        return f'{self.Name}, {self.Strasse}, {self.PLZ} {self.Ort}'

class Kunde:
    def __init__(self):
        self.Adressen = []

    def add_adresse(self, adresse):
        self.Adressen.append(adresse)

    def __str__(self):
        return f'{[str(a) for a in self.Adressen]}'

class CustomerRepository:
    def create_customer(self, customer: Kunde):
        """Creates the provided customer"""
        pass

    def list_customers(self) -> list:
        """Lists all existing customers"""
        pass

class SimpleCustomerRepository(CustomerRepository):
    def __init__(self, persister: Persist):
        self.persister = persister
    def create_customer(self, customer: Kunde):
        addresses = []
        for ad in customer.Adressen:
            addresses.append((ad.Name, ad.Strasse, ad.PLZ, ad.Ort))
        self.persister.save_customer(addresses)

    def list_customers(self) -> list:
        customerRows = self.persister.load_customers()
        customers = []
        for customerRow in customerRows:
            customer = Kunde()
            for addressData in customerRow:
                customer.add_adresse(Adresse(addressData[0],addressData[1],addressData[2],addressData[3]))
            customers.append(customer)
        return customers