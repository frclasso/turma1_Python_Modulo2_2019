#!/usr/bin/env python3

# Classes e instancias

# definindo uma classe
class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+ last +'@company.com'

        Employee.num_of_emps += 1 # contador

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # pode ser Employee.raise...


# instancia de classe/objeto
emp_1 = Employee('Fabio', 'Classo', 120000)
emp_2 = Employee('User', 'Test', 50000)
emp_3 = Employee('Jane','Done', 0)


# print(Employee.teste)
#
print(emp_1.fullname())
print(emp_1.first)
print(emp_1.pay)
#emp_1.raise_amount = 1.05
emp_1.apply_raise()
print(emp_1.pay)
print()

print(emp_2.fullname())
print(emp_2.first)
print(emp_2.last)
print(emp_2.email)
print(emp_2.pay)
emp_2.raise_amount = 1.05
emp_2.apply_raise()
print(emp_2.pay)
#
# print(Employee.num_of_emps)

# print(emp_1.__dict__)
# print(emp_2.__dict__)