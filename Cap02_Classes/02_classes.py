#!/usr/bin/env python3


# Classes e instancias

# definindo uma classe
class Employee:
    # costrutor de classe
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+ last +'@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


# instancia de classe/objeto
emp_1 = Employee('Fabio', 'Classo', 120000)

emp_2 = Employee('User', 'Test', 50000)

print(emp_1.fullname())
#print(Employee.fullname(emp_1))
print(emp_1.first)
print(emp_1.pay)
print()

print(emp_2.fullname())
print(emp_2.first)
print(emp_2.last)
print(emp_2.email)