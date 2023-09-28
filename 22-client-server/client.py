import requests
import json

class Address:
    def __init__(self, name: str, street: str, zipcode: str, city: str):
        self.name = name
        self.street = street
        self.zipcode = zipcode
        self.city = city

    @staticmethod
    def from_json(d: dict):
        return Address(d["name"], d["street"],
                       d["zipcode"],
                       d["city"])


# r = requests.get('https://online-lectures-cs.thi.de/resources/addresses.json')
r = requests.get('http://127.0.0.1:5000/addresses')

print(r.status_code) # der Status Code von HTTP
print(r.headers)     # Header Daten als Dict, man könnte also alle Header-Parameter abrufen
print(r.headers["Server"])
print(r.text) # ist eine Zeichenkette der abgefragten Daten

# entpackt = json.loads(r.text) # transformation von JSON-Str in dict
# obj = Address.from_json(entpackt)
# print(obj)

# Ziel: Beispiel so modifizieren, dass wir eine Mengen von Adressen verarbeiten können
entpackt = json.loads(r.text) # da JSON-Antwort mit [ beginnt, kommt kein Dict, sondern eine Liste (bzw. Array)
print(type(entpackt))

result = []
for element in entpackt:
    obj = Address.from_json(element)
    result.append(obj)

print(str(result))
