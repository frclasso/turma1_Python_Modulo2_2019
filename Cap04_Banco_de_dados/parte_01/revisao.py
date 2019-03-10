#!usr/bin/env python3

import sqlite3

conn = sqlite3.connect('revisao.db')

print('Banco de dados revisao.db criado com sucesso.')

# criando tabelas

conn.execute('''CREATE TABLE COMPANY
             (ID INT PRIMARY KEY NOT NULL,
             NAME  TEXT NOT NULL,
             AGE   INT  NOT NULL,
             ADDRESS CHAR(50),
             SALARY REAL);''')

print('Tabela aula criada com sucesso')


conn.close()
