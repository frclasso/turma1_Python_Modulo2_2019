#!/usr/bin/env python3


def star(func):
    def inner(*args, **kwargs):
        print('*' * 30)
        func(*args, **kwargs)
        print('%' * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print('*' * 30)
        func(*args, **kwargs)
        print('%' * 30)
    return inner



@percent
@star
def printer(msg):
    print(msg)


print(printer('Hello World'))
