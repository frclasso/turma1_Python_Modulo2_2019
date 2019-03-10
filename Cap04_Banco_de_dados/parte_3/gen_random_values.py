import random
import rstr
import datetime


# gerar valores age, cpf, fone, timestamp, city


def gen_age():
    return random.randint(15,99)


def gen_cpf():
    return rstr.rstr('1234567890', 11)


def gen_fone():
    return '({0}) ({1})-({2})'.format(
        rstr.rstr('1234567890', 2),
        rstr.rstr('1234567890', 4),
        rstr.rstr('1234567890', 5)
    )


def gen_timestamp(): # datetime
    year = random.randint(1980, 2019)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    hour = random.randint(1, 23)
    minute = random.randint(1,59)
    seconds = random.randint(1,59)
    microseconds = random.randint(1, 999999)
    date = datetime.datetime(
        year,month, day, hour, minute, seconds, microseconds).isoformat(" ")
    return date

def gen_city():
    list_city = [
        [u'Sao Paulo', 'SP'],
        [u'Belem', 'PA'],
        [u'Rio de Janeiro', 'RJ'],
        [u'Goiania', 'GO'],
        [u'Salvador', 'BA'],
        [u'Guarulhos', 'SP'],
        [u'Brasilia', 'DF'],
        [u'Campinhas', 'SP'],
        [u'Fotaleza', 'CE'],
        [u'São Luís', 'MA']
    ]
    return random.choice(list_city)

