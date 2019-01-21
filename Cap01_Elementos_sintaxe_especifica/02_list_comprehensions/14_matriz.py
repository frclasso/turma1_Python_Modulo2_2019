#!/usr/bin/env python3

matrix = [[1,2,3],[4,5,6],[7,8,9]]

# Alinhando em um unico nivel
umNivel = [y for x in matrix for y in x]
print(umNivel)


# Naoooo :(
nivelUm = []
for x in matrix:
    for y in x:
        nivelUm.append(y)
print(nivelUm)