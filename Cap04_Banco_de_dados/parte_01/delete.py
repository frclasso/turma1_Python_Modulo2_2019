import sqlite3

conn = sqlite3.connect('teste.db')


ursor = conn.execute("DELETE FROM COMPANY WHERE ID = 2")
conn.commit()
print('Quntidades de linhas alteradas: ', conn.total_changes)

cursor = conn.execute("SELECT ID, NAME, ADDRESS, SALARY FROM COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], '\n')

print('Feito')
conn.close()