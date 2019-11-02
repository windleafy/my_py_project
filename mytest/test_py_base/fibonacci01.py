#!/usr/bin/env python
"""fibonacci01"""


# -*- coding: utf-8 -*-
# @Time    : 2019/10/6 14:06
# @Author  : Wind
# @Des     : 
# @Software: PyCharm


def fib_loop(n):
    a, b = 0, 1
    for j in range(n):
        a, b = b, a + b
    return a


for i in range(20):
    print(fib_loop(i), end=" ")
print('\n')


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b, ',', end='')
        a, b = b, a + b
        n += 1
    return 'done'


fib(10)
print('\n')


def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield (b)
        a, b = b, a + b
        n += 1
    return 'done'


print(fib1(10))
for i in fib1(10):
    print(i, ',', end='')
