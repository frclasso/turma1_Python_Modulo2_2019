#!/usr/bin/env python3


class Parent:

    parentAttr = 1000

    def __init__(self):
        print('Chamando o construtor de classe')

    def parentMethod(self):
        print('Chamando o método Pai')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print('Atributo Pai: ', Parent.parentAttr)


class Child(Parent):

    def __init__(self): # sobrescreve
        print("Chamando o construtor Filho")

    def childMethod(self):
        print("Chamando o método Filho")

obj = Child()
obj.parentMethod()
obj.childMethod()
print(obj.parentAttr)
obj.setAttr(2000)
obj.getAttr()

