#!/usr/bin/env python3

# Metodos especiais / Metodos Magicos

# __init__ construtor
# __repr__ representação nao ambigua do objeto(debugging,logging)
# __str__ representação mais legível do objeto

class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@email.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first,
                                                self.last,
                                                self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Fabio', 'Classo', 30000)
dev_1 = Employee('Peter', 'Parker', 2000)
dev_2 = Employee('Mary', 'Jane', 2000)

#print(emp_1)
#
# print(repr(emp_1))
# print(str(emp_1))

# __add__
# print(1+2)
# print(int.__add__(1,2))
#
# print('a' + 'b')
# print(str.__add__('a', 'b'))
#print(emp_1 + dev_2)

# __len__

# print(len('teste'))
# print('teste'.__len__())

#print(len(dev_2))
