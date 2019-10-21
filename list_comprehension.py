nick = {
    'name': 'nick',
    'auto': 'fiat'
}

den = {
    'name': 'den',
    'auto': 'opel'
}

users = [nick, den]
"""

option N1

"""
autos = [person['auto'] for person in users]

print(autos)
"""

option N2

"""

cars = []
for person in users:
    cars.append(person['auto'])

print(cars)

"""

good option N3

"""
new_cars = [person.get('auto', '') for person in users]

print(new_cars)