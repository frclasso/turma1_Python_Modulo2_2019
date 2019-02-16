#!/usr/bin/env python3

# Classes e instancias

# definindo uma classe
class Birds:
    #atributos de classe
    species = 'bird'
    size = 'grande'

    # atributos de instancia
    def __init__(self, name, age):
        self.name = name
        self.age =age

    # métodos
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

# intanciando objetos
blue = Birds('Papagaio', 10)
green = Birds('Arara', 15)
ze = Birds('Ze Carioca', 20)

# acessando atributos de intancia
print(blue.name)
print(blue.age)
print()
#acessando atributos de classe
print('Blue is a {} and size {}'.format(blue.__class__.species,
                                        blue.__class__.size))

# Acesando atrb de objetos
print("{} is {} years old".format(blue.name, blue.age))
print("{} is {} years old".format(green.name, green.age))
print("{} is {} years old".format(ze.name, ze.age))

# Acesando os metodos
print(blue.sing('Oh Happy Day'))
print(green.dance())
