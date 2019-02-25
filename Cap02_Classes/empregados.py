#!/usr/bin/env python3


# getattr, setattr, hasattr, delattr

class Empregados:

    empCount = 0

    def __init__(self, nome, salario):
        self.nome =nome
        self.salario = salario

        Empregados.empCount +=1

    def displayCount():
        print(f'Total de empregados:{Empregados.empCount}')

    def displayEmpregado(self):
        print(f'Nome: {self.nome} - Salario: US${self.salario}.')

emp_1 = Empregados('Peter', 2000)
emp_2 = Empregados('Mary', 3000)

# acessando atributos
emp_1.displayEmpregado()
emp_2.displayEmpregado()

#print(Empregados.empCount)
Empregados.displayCount()

# Verificar atributos dos objetos
print(hasattr(emp_1, 'salario'))
print(hasattr(emp_2, 'idade'))
print(getattr(emp_1, 'salario'))

setattr(emp_2, 'salario', 4000)
print(getattr(emp_2, 'salario'))

delattr(emp_1, 'salario')
print(hasattr(emp_1,'salario'))

# Verificando atributos de classe
print()
print(f'Dicionario de classe:{Empregados.__dict__}')
print(f'Noma da classe: {Empregados.__name__}')
print(f'Modulos disponiveis:{Empregados.__module__}')
print(f'Bases - tipo:{Empregados.__bases__}')