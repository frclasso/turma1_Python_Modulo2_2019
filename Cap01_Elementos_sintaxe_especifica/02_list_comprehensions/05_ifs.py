#!/usr/bin/env python3

# Façam isso!
numDivBy3and5 = [x for x in range(100) if x % 3 == 0 if x % 2 == 0]
print(numDivBy3and5)


# Nao façam mais isso!
div3e2 = []
for x in range(100):
    if x % 3 == 0:
        if x % 2 == 0:
            div3e2.append(x)
print(div3e2)