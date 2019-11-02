#!/usr/bin/env python
"""Iterator01"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/6 11:59
# @Author  : Wind
# @Des     : 
# @Software: PyCharm
from itertools import islice
from collections.abc import Iterable


def is_irator(x):
    try:
        next(x)
    except StopIteration:
        return True
    except TypeError:
        return False
    else:
        return True


my_list = [1, 2, 3, 4, 5]
if is_irator(my_list):
    print('是迭代器啊!')
else:
    print('不是迭代器！')


# 对象类型
print(type(my_list))
# 是否可迭代
print(isinstance(my_list, Iterable))

a = iter(my_list)
print(type(a))
for i in a:
    print(i)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        a, b = b, a + b
        n += 1
        yield a


a = fib(5)
print(a)


def my_fun():
    print('test_pypi')
    yield


b = my_fun()

# print(b)
print(f'next(b){next(b)}')
for i in b:
    print(i)

if is_irator(b):
    print('是迭代器啊!')
else:
    print('不是迭代器！')