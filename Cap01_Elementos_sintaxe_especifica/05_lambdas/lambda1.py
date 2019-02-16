#!/usr/bin/env python3

#
# def func(x):
#     return x ** 3
#
#
# l = lambda x: x ** 3
#
# print(func(5))
# print(l(5))

# Usando argumentos
# mz = (lambda a='Wolfgangus ', b='Theophilus', c='Mozart': a+b+c)
# print(mz('Wolfgang ', 'Amadeus '))


# key
# key = 'quadratic'
#
# print({'square': lambda x: x ** 2,
#       'cubic':lambda x:x**3,
#       'quadratic':lambda x:x**4}
#       [key](10))

min = lambda x,y: x if x < y else y

print(min(100,200))
print(min(300,200))
