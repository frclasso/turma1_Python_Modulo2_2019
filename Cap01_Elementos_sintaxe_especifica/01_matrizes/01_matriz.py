#1/usr/bin/env python3

# Matriz
a = [
    ['Roy',80,75,85,90,95],
    ['John',75,80,75,85,100],
    ['Dave', 80,80,80,90,95]
]

# Lista aninhada
b = [['Roy',80,75,85,90,95],
     ['John',75,80],
     ['Dave', 80,80,80,90,95]
     ]


n = 3
m = 4
a = [0] * n
for i in range(n):
    a[i] = [0] * m
print(a)