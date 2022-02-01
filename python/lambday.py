person = [
    {"name": "mbemba", "house": "turkey" },
    {"name": "sonko", "house": "italia"},
    {"name": "prof", "house": "kombo"}
]

person.sort(key=lambda person: person["house"])

print(person)
