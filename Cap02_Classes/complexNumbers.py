#!/usr/bin/env python3


# template de classes

class ComplexNumber:

    def __init__(self, r=0, i=0):
        self.real = r
        self.imag  = i  # imaginario

    def getData(self):
        print("{}+{}j".format(self.real, self.imag))

# instanciando objetos
c1 = ComplexNumber(2,3)
c1.getData()

c2 = ComplexNumber(5)
c2.getData()
c2.attr = 10

#print(c2.real, c2.imag, c2.attr)
#print(c1.attr)  AttributeError

# Deletar atributos
# del c1.getData
# c1.getData()

#del ComplexNumber.getData
#c2.getData()

# deletar o objeto
# del c1
# print(c1) # NameError: name 'c1' is not defined
