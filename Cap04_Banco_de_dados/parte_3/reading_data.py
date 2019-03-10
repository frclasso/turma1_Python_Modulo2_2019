#!/usr/bin/env python3

# -*- conding:utf-8 -*-

import sqlite3

conn = sqlite3.connect('clientes_DataBases.db')

cursor = conn.cursor()

# lendo dados
cursor.execute("""
    SELECT * FROM clientes;
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()