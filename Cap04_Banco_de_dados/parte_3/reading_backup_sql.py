#!/usr/bin/env python3

# -*- conding:utf-8 -*-

import sqlite3
import io

conn = sqlite3.connect('clientes_recuperado.db')
cursor = conn.cursor()

f = io.open('clientes_dump.sql', 'r')
sql = f.read()

cursor.executescript(sql)   # executescript

print('Banco de dados recuperado com sucesso')
conn.close()