#!/usr/bin/env python3

fh = open('texto.txt', 'r')
result = [i for i in fh if 'terceira linha' in i]
print(result)