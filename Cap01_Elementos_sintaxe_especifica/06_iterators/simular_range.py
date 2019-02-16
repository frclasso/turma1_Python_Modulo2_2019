#!/usr/bin/env python3

#
nums = range(1, 10)
print(list(nums))

class myRange():

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


numeros = myRange(1,10)
for n in numeros:
    print(n, end=', ')


print()

# generator / yield
def other_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


n = other_range(1, 10)
for num in n:
    print(num, end=', ')

