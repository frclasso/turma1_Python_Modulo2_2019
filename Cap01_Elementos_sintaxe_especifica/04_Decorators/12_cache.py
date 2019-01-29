#!/usr/bin/env python3

import functools


@functools.lru_cache(maxsize=4)
def fibonacci(num):
    print(f'Calculating Fibonacci ({num})')
    if num < 2:
        return num
    else:
        return fibonacci(num -1) + fibonacci(num - 2)


fibonacci(10)
print('-' * 30)
fibonacci(5)
print('-' * 30)
fibonacci(8)
print('-' * 30)
fibonacci(5)

print(fibonacci.cache_info())