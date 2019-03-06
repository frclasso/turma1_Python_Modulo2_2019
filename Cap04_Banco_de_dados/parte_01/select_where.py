import sqlite3

conn = sqlite3.connect('teste.db')

# cursor = conn.execute("SELECT * FROM COMPANY WHERE AGE >= 25 "
#                       "AND SALARY >= 65000.00")
# cursor = conn.execute("SELECT * FROM COMPANY WHERE NAME LIKE 'ki%'") # ou _

#cursor = conn.execute("SELECT * FROM COMPANY WHERE AGE IN (25, 27)")
#cursor = conn.execute("SELECT * FROM COMPANY WHERE AGE BETWEEN 25 AND 27")
# cursor = conn.execute("SELECT * FROM COMPANY WHERE AGE >= 25 "
#                       "OR SALARY >= 65000.00")

# cursor = conn.execute("SELECT * FROM COMPANY ORDER BY NAME,  SALARY DESC")

cursor = conn.execute("SELECT NAME, SUM(SALARY) FROM COMPANY GROUP BY NAME")


for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1],'\n')

print('Feito')
conn.close()