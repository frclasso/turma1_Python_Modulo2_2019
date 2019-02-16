#!/usr/bin/env python3

# map(function, iterable)

import sys


fullname = lambda x: list(map(sys.stdout.write, x))
f=fullname(['Wolfgang ', 'Amadeus ', 'Mozart'])
print(f)
