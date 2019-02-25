#!/usr/bin/env python3

# @property => permite acessar métodos/funções como se fossem atributos
# @ setter => setar valores


class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split()
        self.first = first
        self.last = last

vendedor = Employee('Fabio', 'Classo', 5000)

#vendedor.fullname = 'Peter Parker'

print(vendedor.first)
print(vendedor.fullname)
print(vendedor.email)