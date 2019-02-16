#!/usr/bin/env python3

my_list = [4,7,0,5]

my_iter = iter(my_list)

# print(next(my_iter))
# print(next(my_iter))
# print(my_iter.__next__())
# print(my_iter.__next__())
#print(next(my_iter))

for c in my_iter:
    print(c)

print(next(my_iter))