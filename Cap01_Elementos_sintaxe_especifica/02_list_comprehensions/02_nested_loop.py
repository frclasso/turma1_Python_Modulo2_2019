#!/usr/bin./env python3

lista = []
for i in range(3):
    for j in range(3):
        lista.append((i, j))
print(lista)


lista2 = [(i, j) for i in range(3) for j in range(3)]
print(lista2)