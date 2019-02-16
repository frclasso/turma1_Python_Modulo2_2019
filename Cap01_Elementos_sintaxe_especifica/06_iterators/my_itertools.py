#!/usr/bin/env python3

import itertools

counter = itertools.count()
#
# for x in counter:
#     print(x)



#zip
data = [100,200,300,400]
dailydata = list(zip(range(10), data))
print(dailydata)
print()

data = [100,200,300,400]
dailydata = list(itertools.zip_longest(range(10), data))
print(dailydata)


