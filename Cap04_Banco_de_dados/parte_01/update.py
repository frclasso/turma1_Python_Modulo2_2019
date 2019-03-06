import sqlite3

conn = sqlite3.connect('teste.db')

cursor = conn.execute("UPDATE COMPANY SET SALARY = 25000.00 WHERE ID = 1")
conn.commit()
print('Linhas alteradas: ', conn.total_changes)

cursor = conn.execute("SELECT ID, NAME, ADDRESS, SALARY FROM COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("AGE = ", row[2])
    print("ADDRESS = ", row[3])
    print("SALARY = ", row[4], '\n')

print('Feito')
conn.close()