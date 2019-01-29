#!/usr/bin/env python3


dict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}

dict_comp = {k:v for k,v in dict.items() if v > 2 if v % 2 == 0
if v % 3 == 0}

print(dict_comp)


# em for

triple = {}
for k, v in dict.items():
    if v > 2 and v % 2 == 0 and v % 3 == 0:
        triple[k] = v

print(triple)