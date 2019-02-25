#!/usr/bin/env python3

# Heranca multipla

class Pai:

    def __init__(self):
        print("Construtor da classe Pai")
        self.x = 2000

class Mae:

    def __init__(self):
        print('Construtor da classe Mae')
        self.z = 1000

class Filha(Pai):

    def __init__(self):
        Pai.__init__(self)
        Mae.__init__(self)
        print('Construtor da classe Filha')
        self.y = 500


class Neta(Filha):  # heranca

    def __init__(self):
        super().__init__()
        print('Construtor da Classe neta')


f = Filha()
# print(f.x)
# print(f.z)
# print(f.y)

n = Neta()
print(n.x)
print(n.y)

print(Neta.__mro__)
print(Neta.mro())