#!/usr/bin/env python3


# template de classes

class MyClass:
    """Definindo a classe MyClass"""
    a = 10  # variavel de classe

    def func(self): # metodo /comportamento
        print('Hello Python')


obj = MyClass()

# Acessando variaveis de classe
print(obj.a)
print(obj.func())
print(MyClass.func(obj))
print(obj.__doc__)