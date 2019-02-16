#!/usr/bin/env python3

# Herança

# definindo uma classe
class Birds:  # classe Pai/Super Classe

    def __init__(self):
        print('Birds are ready!!')

    #metodos
    def whoIsThis(self):
        print('Birds...')

    def fly(self):
        print('Fly faster')


# classe filha/subclasse/child classe
class Penguin(Birds): # herda de Birds atributos e metodos

    def __init__(self): # construtor da classe Penguin
        super().__init__() # super classe
        print('Penguin is ready!!')

    def whoIsThis(self):
        print("Penguin...")

    def swin(self):
        print("Swin faster")

blue = Birds()
blue.whoIsThis()
blue.fly()
#blue.swin() # AttributeError: 'Birds' object has no attribute 'swin'
print()

peggy = Penguin()
peggy.whoIsThis()
peggy.swin()
peggy.fly()

