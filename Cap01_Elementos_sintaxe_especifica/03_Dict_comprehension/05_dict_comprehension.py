#!/usr/bin/env python3

# if /else

dict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}

# Identificando pares e impares
double_condition = {k:('par' if v % 2 == 0 else 'impar') for (k,v) in
                    dict.items()}


print(double_condition)
