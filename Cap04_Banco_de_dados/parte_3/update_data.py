#!/usr/bin/env python3

# -*- conding:utf-8 -*-

import sqlite3

conn = sqlite3.connect('clientes_DataBases.db')
cursor = conn.cursor()

id_cliente = 1
novo_fone = '(11)555-100-2000'
novo_cridado_em = '2016-06-11'

# Atualizando
cursor.execute("""
    UPDATE clientes SET fone = ?, criado_em = ? WHERE id=?
""", (novo_fone, novo_cridado_em, id_cliente))

conn.commit()

print('Dados atualizados com sucesso')
conn.close()
