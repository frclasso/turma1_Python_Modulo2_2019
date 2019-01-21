#!/usr/bin/env python3

# slicing com numpy
from numpy import *

a = array(
    [
    ['Roy',80,75,85,90,95],
    ['John',75,80,75,85,100],
    ['Dave', 80,80,80,90,95]
]
)

print(a[:, [0,1]])