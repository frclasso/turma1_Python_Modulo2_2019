#!/usr/bin/env python3

# -*- conding:utf-8 -*-

import sqlite3

conn = sqlite3.connect('clientes_DataBases.db')
cursor = conn.cursor()

# adicionar nova coluna 'bloqueado'
cursor.execute("""
    ALTER TABLE clientes ADD COLUMN bloqueado BOOLEAN;
""")
conn.commit()
print('Coluna bloqueado inserida com sucesso')
conn.close()