#!/usr/bin/env python3

kilometer = [39.2, 36.5, 37.3, 37.8]

feet = [3280.8399 * x for x in kilometer]
print(feet)

num = [x + 1 if x >= 120000 else x + 5 for x in feet]
print(num)
