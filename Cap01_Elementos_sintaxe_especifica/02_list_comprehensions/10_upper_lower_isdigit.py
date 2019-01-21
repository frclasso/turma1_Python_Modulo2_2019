#!/usr/bin/env python3

print([x.lower() for x in ['A','B', 'C','D', 'E']])
print()
print([x.upper() for x in ['a', 'b', 'c', 'd', 'e']])
print()

string = 'Hello 12345 World'
numbers = [x for x in string if x.isdigit()]
print(numbers)