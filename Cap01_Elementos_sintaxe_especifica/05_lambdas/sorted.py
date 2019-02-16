#!/usr/bin/env python3

# sorting

death = [
    ('John', 'Lennon', 40),
    ('James', 'Dean', 24),
    ('Jimi', 'Hendrix', 27),
    ('George', 'Gershwin', 38)
]

s = sorted(death, key=lambda age:age[2], reverse=False)
for x in s:
    print(x)

