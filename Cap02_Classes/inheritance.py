#!/usr/bin/env python3


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


class Developer(Employee):
    raise_amount = 1.10  # aumento diferenciado pros Dev

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        # employees=None - lista de empregados
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp): # Adiciona employees
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp): # remove employees
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self): # imprime nome completo dos employees
        for emp in self.employees:
            print('===>', emp.fullname())



emp_1 = Employee('Fabio', 'Classo', 30000)
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)


dev_1 = Developer('Peter', 'Parker', 2000, 'Python')
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

dev_2 = Developer('Mary', 'Jane', 30000,'Django')


mgr_1 = Manager('JJ', 'Jameson', 400000, [dev_1])
#print(mgr_1.email)
# adicionando dev_2 e emp_1
mgr_1.add_emp(dev_2)
mgr_1.add_emp(emp_1)

# removendo subordinados
mgr_1.remove_emp(emp_1)

#print(mgr_1.print_emp())


# Para verificar instancias
# print(isinstance(mgr_1, Manager))
# print(isinstance(mgr_1, Employee))
# print(isinstance(mgr_1, Developer))

# Para veiricar as subclasses
print(issubclass(Developer, Employee)) # subclasse, classe
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))