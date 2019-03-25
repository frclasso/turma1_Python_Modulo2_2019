#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('pessoas.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE pessoas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    cidade_id INTEGER,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(cidade_id) REFERENCES cidade(id));
""")

print('Tabela  pessoas criadas com sucesso')

conn.close()
