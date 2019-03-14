#!usr/bin/env python3

import sqlite3

conn = sqlite3.connect('revisao.db')

conn.execute("INSERT INTO COMPANY(ID, NAME, AGE, ADDRESS, SALARY)VALUES(1, 'Paul', 32, 'California', 20000.00 )");

conn.commit() # salvar
print('Valores inseridos com sucesso')