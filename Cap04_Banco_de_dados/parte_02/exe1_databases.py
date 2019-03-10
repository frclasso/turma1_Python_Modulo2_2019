#!/usr/bin/env python3


# sqlite3
import sqlite3

def main():

    db =sqlite3.connect(('data1.db'))
    db.row_factory = sqlite3.Row
    # deleta a tabale se já existir
    db.execute('drop table if exists test')
    # cria a tabela 'test'
    db.execute('create table test(Nome text, idade int)')
    # insere  campos
    db.execute('insert into test(Nome, idade) values (?, ?)', ('Fabio',44))
    db.execute('insert into test(Nome, idade) values (?, ?)', ('Juli',40))
    db.execute('insert into test(Nome, idade) values (?, ?)', ('Erick',10))
    db.execute('insert into test(Nome, idade) values (?, ?)', ('Giovanna',6))
    # salva
    db.commit()
    # lendo
    cursor = db.execute('select idade, Nome from test order by idade')
    for row in cursor:
        print(row['Nome'], '=>', row['idade'])


if __name__=='__main__':main()

