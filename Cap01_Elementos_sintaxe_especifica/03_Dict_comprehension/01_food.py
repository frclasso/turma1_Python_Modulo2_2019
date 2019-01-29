#!/usr/bin env python3

food = {'apple':'fruit', 'beetroot':'vegetable', 'cake':'dessert'}

#updating
food['doughnut']='snack'
#print(food)

# delete
# del food['apple']
# print(food)
# #
# food.pop('cake')
# print(food)
#
# # deletando todos os elementos
# food.clear()
# print(food)
#
# # excluindo o dicionario
# del food
# print(food)

# for k, v in food.items():
#     print(k, v)

#print({k:v for k,v in food.items()})

# acessando as chaves
print(food['apple'])
print(food.keys()) # retorma um dicionario de todas as chaves
print(food.values()) # retorna um dicionario de todas os valores
print(food.items()) # rertorna os pares em tuplas