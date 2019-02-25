#!/usr/bin/env python3

# re - regular expressions
# r => raw string
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

# print('\tTab')
# print(r'\tTab')
# <re.Match object; span=(1, 4), match='abc'>  span (inicio/fim)

#pattern = re.compile(r'abc')
#pattern = re.compile(r'\.')
#pattern = re.compile(r'codecla\.com\.br')
#pattern = re.compile(r'\d')# digitos 0-9
#pattern = re.compile(r'\D')# nao digitos
#pattern = re.compile(r'\w')# word caracters[a-zA-Z0-9]
#pattern = re.compile(r'\W')# Not Word caracters
#pattern = re.compile(r'\s')# (space, tab, newline)
#pattern = re.compile(r'\S')# contrario de \s
#pattern = re.compile(r'\bHa')# boundary
#pattern = re.compile(r'\BHa')# boundary

# ^ => inicio , $ => fim

#pattern = re.compile(r'^Start')  # pesquisa no inicio
# pattern = re.compile(r'end$')  # pesquisa no fim da string
#matches = pattern.finditer(sentence)


# pattern = re.compile(r'')  # pesquisa no inicio
#
# with open('data.txt', 'r') as file:
#     contents = file.read()
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)


#pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
#pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d') # *
#pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')  # 800 900
#pattern = re.compile(r'[a-zA-Z0-9]') # intervalos
#pattern = re.compile(r'[^a-zA-Z0-9]') # ^ inverte
#pattern = re.compile(r'[^b]at') # negando 'b'

# quantificadores ( *, +, ? {nr} , {n- nm}
#pattern = re.compile(r'\d{3}.\d{3}.\d{4}') # {numero exato}
pattern = re.compile(r'M(r|rs|s)\.?\s[A-Z]\w*') # grupo ()


matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


#print(text_to_search[1:4])