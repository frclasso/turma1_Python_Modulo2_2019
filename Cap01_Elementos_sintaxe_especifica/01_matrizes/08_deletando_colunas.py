#!/usr/bin/env python3

from numpy import *

alunos = array(
    [
        ['Roy',80,75,85,90,95],
        ['John',75,80,75,85,100],
        ['Dave', 80,80,80,90,95]
    ]
)

alunos = delete(alunos, s_[1::2], 1) # axis=0
print(alunos)