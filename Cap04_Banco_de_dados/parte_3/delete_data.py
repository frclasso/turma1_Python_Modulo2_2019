#!/usr/bin/env python3

# -*- conding:utf-8 -*-

import sqlite3

conn = sqlite3.connect('clientes_DataBases.db')
cursor = conn.cursor()

id_cliente = 6

cursor.execute("""
    DELETE FROM clientes WHERE id=?
""", (id_cliente,))

conn.commit()
print('Resgistro excluido com sucesso')
conn.close()