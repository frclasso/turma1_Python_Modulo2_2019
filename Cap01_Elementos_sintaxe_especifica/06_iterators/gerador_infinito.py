#!/usr/bin/env python3


# gerador de numeros infinitos

def infinity_gen(start):
    current = start
    while True:
        yield current
        current += 1


i = infinity_gen(1)
for num in i:
    print(num)