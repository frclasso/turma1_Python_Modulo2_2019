#!/usr/bin/env python3

with open('clientes.txt', 'r') as f:
    for line in f.readlines():
        print(line,end='')

print()
print()
print('Feito...')