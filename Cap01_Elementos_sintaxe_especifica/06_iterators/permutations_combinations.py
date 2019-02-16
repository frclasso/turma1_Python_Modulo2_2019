#!/usr/bin/env python3

import itertools

letters = ['a', 'b', 'c','d','f']

numbers = [1,2,3,4,5]

names = ['Jane', 'Doe']
DNA = ['A','C','G','T']

# combinations a ordem nao importa  e nao se repetem as comninacoes
# result =itertools.combinations(letters, 2)
# for item in result:
#     print(item)

# permutations a ordem importa e se repetem as combinacoes
result =itertools.permutations(DNA, 4)
for item in result:
    print(item)