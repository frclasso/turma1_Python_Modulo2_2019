#!/usr/bin/env python3

# -*- conding:utf-8 -*-

import sqlite3

conn = sqlite3.connect('clientes_DataBases.db')

cursor = conn.cursor()

# lista de dados

lista = [
    ('Peter', 23,'444444444444', 'peter@email.com','(48)1233-4567', 'New York','NY', '2014-06-09'),
    ('Mary', 20,'444444444444', 'mjane@email.com','(48)1233-4455', 'Los Angeles','LA', '2014-06-09'),
    ('Bruce', 32,'77777777777', 'bwayne@email.com','(48)1233-4567', 'Gothan','GT', '2014-06-09'),
]

# Inserindo dados na tabela
cursor.executemany("""
    INSERT INTO clientes(nome, idade, cpf, email,fone, cidade, uf, criado_em)
    VALUES(?,?,?,?,?,?,?,?)
""", lista)


conn.commit()
print('Dados inseridos com sucesso')