#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""list_comprehension"""
# @Time    : 2019/10/29 10:52
# @Author  : Wind
# @Des     : 
# @Software: PyCharm
# test_list = [m + n for m in 'ABC' for n in 'XYZ']

test_list = []
for i in range(10):
    test_list.append(i)

print(test_list)


my_list = [(1, 2, 3, 4, 5)]
try:
    for i, j in my_list:
        print(i)
        print(j)
except ValueError:
    print('出错了')

a = 1/0
