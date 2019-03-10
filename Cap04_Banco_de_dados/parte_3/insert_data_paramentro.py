#!/usr/bin/env python3

# -*- conding:utf-8 -*-

import sqlite3

conn = sqlite3.connect('clientes_DataBases.db')

cursor = conn.cursor()

# INPUTS
p_nome = input('Nome: ')
p_idade = input('Idade: ')
p_cpf = input('CPF: ')
p_email = input('email: ')
p_fone = input('Telefone: ')
p_cidade = input('Cidade: ')
p_uf = input('UF: ')
p_criado_em = input('Criado em: ')


# inserindo dados na tabela
cursor.execute("""
    INSERT INTO clientes(nome,idade,cpf,email,fone,cidade,uf,criado_em)
    VALUES(?,?,?,?,?,?,?,?)
""", (p_nome, p_idade, p_cpf,p_email,p_fone, p_cidade, p_uf, p_criado_em))

conn.commit()
print('Dados inseridos com sucesso')

conn.close()