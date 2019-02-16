#!/usr/bin/env python3


import itertools

# isslice

# result = itertools.islice(range(20),1,20, 5) # start, stop, step
# for item in result:
#     print(item)


with open("test.log", 'r') as f:
    header = itertools.islice(f, 3)

    for line in header:
        print(line, end='')



