#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/1 19:32
# @Author  : Wind
# @Des     : 
# @Site    : 
# @File    : sort01.py
# @Software: PyCharm
import operator

test_list = [5, 2, 3, 1, 4]
# sorted(list)
# 可以接受任何可迭代对象
# 返回新的已排序列表，不改变原列表
print(sorted(test_list))
print(test_list)

# list.sort()
# 修改原列表（并返回 None 以避免混淆）
# 只为列表定义
print(test_list.sort())
print(test_list)

# 元组列表排序，指定元素的第几个元素，进行排序
print('元组列表排序', '-' * 50)
random = [('a', 2, 6), ('b', 4, 8), ('c', 1, 4), ('d', 3, 2)]
print(sorted(random, key=lambda x: x[2]))
random.sort(key=lambda x: x[1], reverse=False)
print(random)

# 字典列表排序，指定字典的某个关键字排序
print('字典列表排序', '-' * 50)
array = [{"age": 20, "name": "z"}, {"age": 25, "name": "b"}, {"age": 10, "name": "c"}]
array = sorted(array, key=lambda x: x["name"], reverse=True)
print(array)

# 列表排序
print('列表排序', '-' * 50)
aList = ["123", 'Google', 'Runoob', 'Taobao', 'Facebook']
aList.sort(reverse=True)
print("List : ", aList)

# 原始形式
print('字符串长度排序', '-' * 50)


test_list = [('a', 2, 6), ('b', 4, 8), ('c', 1, 4), ('d', 3, 2)]
print(sorted(test_list, key=operator.itemgetter(1)))


