#!/usr/bin/env python3

import sqlite3

# crud - create,retrieve, update, delete


def insert(db, row):
    """Inserindo dados"""
    db.execute('insert into test(nome,sobrenome,email,cargo)'
               'values(?,?,?,?)', (row['nome'],row['sobrenome'],
                                   row['email'], row['cargo']))


def retrieve(db, nome):
    """Função que recupera dados"""
    cursor = db.execute('select * from test where nome = ?', (nome,))
    return cursor.fetchone()


def update(db, row):
    """Função atualiza os dados"""
    db.execute('update test set email = ?, cargo= ? where nome = ?',
               (row['email'], row['cargo'], row['nome']))


def delete(db, nome):
    """Função que deleta dados"""
    db.execute('delete from test where nome = ?', (nome,))
    db.commit()


def disp_rows(db):
    """Função que exibe os dados"""
    cursor = db.execute('select * from test order by nome')
    for row in cursor:
        print(f"{row['nome']},{row['sobrenome']}, {row['email']}, {row['cargo']}")


def main():
    db = sqlite3.connect('data2.db')
    db.row_factory = sqlite3.Row
    print('Banco data2.db criado com sucesso')
    db.execute('drop table if exists test')
    db.execute('create table test(nome text, sobrenome text, email text,cargo text)')
    print()
    print('INSERT___')
    insert(db, dict(nome='Fabio',sobrenome='Classo',email='fabio@email.com',
                    cargo='developer'))
    insert(db, dict(nome='Peter',sobrenome='Parker',email='pparker@email.com',
                    cargo='fotografo'))
    insert(db, dict(nome='Mary',sobrenome='Jane',email='mjwatson@email.com',
                    cargo='cantora'))
    insert(db, dict(nome='Bruce',sobrenome='Wayne',email='wayne@email.com',
                    cargo='Milionario'))
    insert(db, dict(nome='John',sobrenome='Wicky',email='johnwicky@email.com',
                    cargo='Assassino'))
    insert(db, dict(nome='Sara',sobrenome='Connor',email='saraconnor@email.com',
                    cargo='sobrevivente'))

    disp_rows(db)

    print()
    print('Retrieve_____')
    print(dict(retrieve(db, 'Fabio')))
    print(dict(retrieve(db, 'Bruce')))

    print()
    print('Update_______')
    update(db, dict(nome='John',sobrenome='Wicky',email='johnw@email.com',
                    cargo='Ator'))
    update(db, dict(nome='Sara',sobrenome='Connor',email='sconnor@email.com',
                    cargo='Atriz'))

    disp_rows(db)

    print()
    print('Delete_____')
    delete(db, 'John')
    delete(db, 'Sara')

    disp_rows(db)


if __name__=="__main__":main()