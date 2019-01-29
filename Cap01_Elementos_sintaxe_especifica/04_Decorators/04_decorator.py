#!/usr/bin/env python3


def make_pretty(func): # decoradora
    def inner():
        print('I got decorated')
        func()
    return inner


def ordinary():  # funcao decorada
    print("I am ordinary")

# print(ordinary())
# print()

# decorando ordinary()
pretty = make_pretty(ordinary)
print(pretty())