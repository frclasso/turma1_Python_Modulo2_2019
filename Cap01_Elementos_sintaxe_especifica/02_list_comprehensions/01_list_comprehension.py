#!/usr/bin/env python3


# criando uma lista e populando usando um range
numbers = []
for i in range(10):
    numbers.append(i)
print(numbers)


# fazendo o mesmo com list_comprehension
new_numbers = [i for i in range(10)]
print(new_numbers)

print()
# Operacao matematica
numbers_multiplied = [i * 2 for i in range(10)]
print(numbers_multiplied)

# condicionais
numPar = [i for i in range(20) if i % 2 == 0]
print()

fish_tuples = ('catfish', 'blowfish', 'clownfish', 'octopus')
fish_list = [fish for fish in fish_tuples if fish.endswith('pus')]
print(fish_list)

# fish_list2 = []
# for f in fish_tuples:
#     if f != 'octopus':
#         fish_list2.append(f)
# print(fish_list2)