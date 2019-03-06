import sqlite3

conn = sqlite3.connect('teste.db')

# Inserir valores

conn.execute("INSERT INTO COMPANY(ID, NAME, AGE, ADDRESS, SALARY)"
             "VALUES(1, 'Paul', 32, 'California', 20000.00)");

conn.execute("INSERT INTO COMPANY(ID, NAME, AGE, ADDRESS, SALARY)"
             "VALUES(2, 'Allen', 25, 'Texas', 15000.00)");

conn.execute("INSERT INTO COMPANY(ID, NAME, AGE, ADDRESS, SALARY)"
             "VALUES(3, 'Teddy', 23, 'Norway', 20000.00)");

conn.execute("INSERT INTO COMPANY(ID, NAME, AGE, ADDRESS, SALARY)"
             "VALUES(4, 'Mark', 25, 'Rich-Mond', 65000.00)");

conn.execute("INSERT INTO COMPANY VALUES(5, 'David', 27,"
             " 'Texas', 85000.00)");

conn.execute("INSERT INTO COMPANY VALUES(6, 'Kim', 22,"
             " 'South-Hall', 45000.00)");

conn.execute("INSERT INTO COMPANY VALUES(7, 'James', 24,"
             " 'Houston', 10000.00)");

conn.commit() # salvar
print('Dados salvos com sucesso')
