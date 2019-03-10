#!/usr/bin/env python3

# -*- conding:utf-8 -*-

import sqlite3

conn = sqlite3.connect('clientes_DataBases.db')
cursor = conn.cursor()
nome_tabela = 'clientes'

cursor.execute("PRAGMA table_info ({})".format(nome_tabela))

colunas = [tupla[1] for tupla in cursor.fetchall()]
print('Colunas:', colunas)

# listando as tabelas do bd
cursor.execute("""
    SELECT name FROM sqlite_master WHERE type='table' ORDER BY name
""")

print('Tabela(s):')
for tabela in cursor.fetchall():
    print("{}".format(tabela))

# obtendo o schema da tabela
cursor.execute("""
    SELECT sql FROM sqlite_master WHERE type='table' AND name=?
""", (nome_tabela,))

print('Schema:')
for schema in cursor.fetchall():
    print('{}'.format(schema))

conn.close()