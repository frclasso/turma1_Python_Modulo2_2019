#!/usr/bin/env python3

clientes = []

novos_clientes =[]

def add_clientes():
    nome = input('Digite nome: ')
    s_nome = input('Digite sobrenome: ')
    idade = input('Digite idade: ')
    novos_clientes.append(nome)
    novos_clientes.append(s_nome)
    novos_clientes.append(idade)


add_clientes()


clientes.append(novos_clientes)

with open('clientes.txt', 'a') as f:
    for line in clientes:
        f.write('\n')
        f.write(str(line) + ',')


print()
print(clientes)
print('Feito...')