import json

class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
        self.any_other_thing = 42
    # def to_json(self):
    #     return f'{{ "name": "{self.name}", "alter": {self.alter} }}'

    def to_json(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def from_json(dict):
        return Person(dict["name"], dict["alter"])

example = Person('Peter Maier', 25)
result = example.to_json()
print(result)

retransformed = json.loads(result) # dict
example3 = Person.from_json(retransformed)
print(example3)

# example2 = Person(retransformed["name"], retransformed["alter"])
# print(retransformed)
# print(type(retransformed))
# print(example2)
# print(type(example2))

# Ziel: generieren eines Strings, der genau so aufgebaut ist, wie es JSON vorgibt
# ToDo: { "name": "Peter Maier", "alter": 25 }
