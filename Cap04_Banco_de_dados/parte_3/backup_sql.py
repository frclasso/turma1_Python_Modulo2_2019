#!/usr/bin/env python3

# -*- conding:utf-8 -*-

import sqlite3
import io

conn = sqlite3.connect('clientes_DataBases.db')


with io.open('clientes_dump.sql', 'w') as f:
    for linha in conn.iterdump():
        f.write('{}\n'.format(linha))

print('Backup realizado com sucesso')
conn.close()
