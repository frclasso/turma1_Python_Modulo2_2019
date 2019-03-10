#!/usr/bin/env python3

# -*- conding:utf-8 -*-

import sqlite3

conn = sqlite3.connect('clientes_DataBases.db')

cursor = conn.cursor()

# inserir dados

cursor.execute("""
    INSERT INTO clientes(nome,idade,cpf,email,fone, cidade, uf, criado_em)
    VALUES('Regis',35,'01234567891','regis@email.com', '(11)9886-7654','Sao Paulo','SP', '2019-03-08')
""")
cursor.execute("""
    INSERT INTO clientes(nome,idade,cpf,email,fone, cidade, uf, criado_em) 
    VALUES('Aloisio',45,'01231117891','aloisio@email.com', '(11)9886-7654','Porto Alegre',
    'RS', '2019-03-08')
""")
cursor.execute("""
    INSERT INTO clientes(nome,idade,cpf,email,fone, cidade, uf, criado_em) 
    VALUES('Bruna',25,'01232222291','bruna@email.com', '(11)9886-7654','Rio de Janeiro',
    'RJ', '2019-03-08')
""")
cursor.execute("""
    INSERT INTO clientes(nome,idade,cpf,email,fone, cidade, uf, criado_em) 
    VALUES('Matheus',15,'01233367891','matheus@email.com', '(11)9886-7654','Campinas',
    'SP', '2019-03-08')
""")


conn.commit()
print('Dados inseridos com sucesso')
conn.close()