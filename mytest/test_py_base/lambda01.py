#!/usr/bin/env python
"""lambda01"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/6 11:21
# @Author  : Wind
# @Des     : 
# @Software: PyCharm

# 案例1


# lambda用法
test_list = [('two', 2), ('three', 3), ('one', 1), ('five', 5), ('four', 4)]
sorted_list = sorted(test_list, key=lambda x: x[1])
print(sorted_list)
print(test_list)


# 案例2
def square(x):
    return x**2


test_list = [2, 3, 5, 7, 11, 13, 19, 17]
print(list(map(square, test_list)))

# lambda用法
map_list = list(map(lambda x: x ** 2, test_list))
print(map_list)


test_list1 = [1, 3, 5, 7, 9]
test_list2 = [2, 4, 6, 8, 10]
map_list = list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
print(map_list)

import functools

test_list = list(range(1, 101))
init = 0
print(functools.reduce(lambda x, y: x + y, test_list, init))

test_list = list(range(1, 6))
init = 1
print(functools.reduce(lambda x, y: x * y, test_list, init))

test_list = list(range(1, 15))
filter_list = list(filter(lambda x: x % 3 == 0, test_list))
print(filter_list)