#!/usr/bin/env python3

# Python2.7 ==> import RegularExpressions
# r ==> raw string

import re
text_to_search="""
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha  HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

codecla.com.br

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
"""

emails = """
FabioClasso@gmail.com
fabio.classo@codecla.edu
fabio-74-classo@my-work.net
"""

urls = """
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
https://codecla.com.br
"""

sentence = 'Start a sentence and then bring it to an end'
# print('\tTAB')
# print(r'\tTAB')
#pattern = re.compile(r'abc')
#pattern = re.compile(r'\.') # ponto corresponde qq coisa menos \n
#pattern = re.compile(r'codecla\.com\.br')
#pattern = re.compile(r'\d') # digitos
#pattern = re.compile(r'\D') # Nao digitos
#pattern = re.compile(r'\w') # Word caracters, letras e numeros
#pattern = re.compile(r'\W') # No Word caracters
#pattern = re.compile(r'\bHa') # boundary
# pattern = re.compile(r'\BHa') # boundary

# ^ = start(inicio da string) , $ = end(final da string)
#pattern = re.compile(r'^Start') # procura no inicio
#pattern = re.compile(r'end$') # procura no fim

# Telofone
#pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
# pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
#
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

# telefones em data.txt
# with open('data.txt', 'r') as file:
#     contents = file.read()
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)


# ranges - intervalos
#pattern = re.compile(r'[a-zA-Z0-9]')

# negar
#pattern = re.compile(r'[^a-zA-Z]')
#pattern = re.compile(r'[^b]at')


# QUANTIFICADORES
"""
* - 0 ou mais de um
+ - 1 ou mais de um
? - 0 ou 1
{nr} - numero extato de vezes
{n,m} - intervalo
"""
#pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
#pattern = re.compile(r'Mr\.?') # ponto opcional
#pattern = re.compile(r'Mr\.?\s[A-Z]')
#pattern = re.compile(r'Mr\.?\s[A-Z]\w+')
#pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w+')  # Mr T
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')  # Mr T

# emails
#pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com')
#pattern = re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)')
# pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')


# urls
# pattern = re.compile(r'https?://(www\.)?\w+\.\w+(\.br)?')
#
# matches = pattern.finditer(urls)
# for match in matches:
#     print(match)

# findall
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
#
# matches = pattern.findall(text_to_search)
# for match in matches:
#     print(match)


# search
# pattern = re.compile(r'sentence')
# match =pattern.search(sentence)
# print(match)


# flags  re.IGNORECASE  re.I
pattern = re.compile(r'start', re.I)
match =pattern.search(sentence)
print(match)



# matches = pattern.search(sentence)
# for match in matches:
#     print(match)



#print(text_to_search[1:4])