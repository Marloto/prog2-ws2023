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

@app.route('/test')
def test():
    return "Hello, World!"

@app.route('/address')
def address():
    address = Address("Ich", "Dort 1", "12345", "Irgendwoe")
    result = address.to_json()
    return result


@app.route('/addresses')
def addresses():
    address1 = Address("Ich", "Dort 1", "12345", "Irgendwoe")
    address2 = Address("Du", "Sonstwo 2", "99999", "Anderswo")
    result = json.dumps([address1.__dict__, address2.__dict__])
    return result

if __name__ == '__main__':
   app.run(port=5000, debug=True)
