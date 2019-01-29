#!/usr/bin/env python3

def make_pretty(func): # decoradora
    def inner():
        print('I got decorated')
        func()
    return inner

@make_pretty
def ordinary():  # funcao decorada
    print("I am ordinary")

print(ordinary())