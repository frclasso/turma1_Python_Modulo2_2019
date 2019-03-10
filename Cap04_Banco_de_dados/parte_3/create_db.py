#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('clientes_DataBases.db')

cursor = conn.cursor()

cursor.execute("""
    create table clientes(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    cpf VARCHAR(11) NOT NULL,
    email TEXT NOT NULL,
    fone TEXT,
    cidade TEXT,
    uf VARCHAR(2) NOT NULL,
    criado_em DATE NOT NULL);
""")

print('Tabela clientes criada com sucesso')

conn.close()
