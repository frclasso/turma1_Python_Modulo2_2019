import sqlite3

conn = sqlite3.connect('teste.db')

# criar tabelas

conn.execute("""CREATE TABLE COMPANY(
            ID INT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
            AGE INT NOT NULL,
            ADDRESS CHAR(50),
            SALARY REAL);""")


print('Tabela criada com sucesso')


conn.close()