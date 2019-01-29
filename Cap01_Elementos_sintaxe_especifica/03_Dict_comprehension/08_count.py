#!/usr/bin/env oython3

# contando letras
fruits = ['apple', 'mango', 'banana', 'cherry']

contador = {f:len(f) for f in fruits}
print(contador)

print()
# capitalize
capitalize = {f:f.capitalize() for f in fruits}
print(capitalize)

print()

# enumerando
enum = {f:i for i, f in enumerate(fruits)}
print(enum)

# invertendo chaves e valores
inverted = {v:k for k,v in enum.items()}
print(inverted)
print()

# deletando items
remove_this = {'apple', 'cherry'}
removed = {key:capitalize[key] for key in capitalize.keys() - remove_this}
print(removed)