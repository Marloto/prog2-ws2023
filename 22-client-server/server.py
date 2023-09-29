import json

from flask import Flask

class Address:
    def __init__(self, name: str, street: str, zipcode: str, city: str):
        self.name = name
        self.street = street
        self.zipcode = zipcode
        self.city = city

    def to_json(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def from_json(d: dict):
        return Address(d["name"], d["street"],
                       d["zipcode"],
                       d["city"])

app = Flask(__name__)

# localhost -> 127.0.0.1
# http://localhost:5000/test
@app.route('/test')
def test():
    return "Hello, World!"

# http://localhost:5000/address
# HTTP definiert mehrere "Methoden" GET / POST
# zur vereinfachung ist das folgende nur ein "GET" ohne Daten, daher wird ein Dummy Eintrag erzeugt
@app.route('/address')
def address():
    address = Address("Ich", "Dort 1", "12345", "Irgendwoe")
    result = address.to_json()
    return result
# Ergebnis wäre etwas der Form: {"name": "Ich", "street": "Dort 1", ...}


# http://localhost:5000/addresses
# Ebenfalls GET
@app.route('/addresses')
def addresses():
    address1 = Address("Ich", "Dort 1", "12345", "Irgendwoe")
    address2 = Address("Du", "Sonstwo 2", "99999", "Anderswo")
    result = json.dumps([address1.__dict__, address2.__dict__])
    return result
# Ergebnis wäre etwas der Form: [{"name": "Ich", "street": "Dort 1", ...}, {"name": "Du", "street": "Sonstwo 2", ...}]

if __name__ == '__main__':
   app.run(port=5000, debug=True)
