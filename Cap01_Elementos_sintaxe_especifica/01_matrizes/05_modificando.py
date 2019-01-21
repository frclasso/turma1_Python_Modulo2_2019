#!/usr/bin/env python3

alunos = [
    ['Roy',80,75,85,90,95],
    ['John',75,80,75,85,100],
    ['Dave', 80,80,80,90,95]
]

b = alunos[0]
b[1] = 75
#print(alunos)


# alunos[2] = ['Sam', 82,79,88,97,99]
# print(alunos)

# adicionar
from numpy import *
alunos = append(alunos, [['Sam', 82,79,88,97,99]], axis=0)
print(alunos)
print()

# axis => dimensoes\
# axis = 0 ==> linhas

alunos = insert(alunos,[6],[[73], [80], [85],[90]], axis=1)
print(alunos)

# axis = 1 ==> colunas

