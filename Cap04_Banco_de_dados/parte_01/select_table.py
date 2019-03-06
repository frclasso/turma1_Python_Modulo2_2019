import sqlite3

conn = sqlite3.connect('teste.db')

cursor = conn.execute("SELECT ID, NAME,AGE, ADDRESS, SALARY FROM COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("AGE = ", row[2])
    print("ADDRESS = ", row[3])
    print("SALARY = ", row[4], '\n')

print('Feito')
conn.close()