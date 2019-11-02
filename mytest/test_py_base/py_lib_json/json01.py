#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/1 15:31
# @Author  : Wind
# @Des     : 
# @Site    : 
# @File    : json01.py
# @Software: PyCharm

import json

# 字典转字符串(两种写法)
my_json = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
my_json2string1 = json.dumps(my_json)
my_json2string2 = json.JSONEncoder().encode(my_json)

# 字典增加元素
my_json['f'] = 6

# 字典删除元素
del my_json['c']

# 字符串转字典(两种写法)
my_string = '{ "a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5 }'
my_string2json1 = json.loads(my_string)
my_string2json2 = json.JSONDecoder().decode(my_string)

# 字典遍历
for k in my_json.keys():
    # print(k)
    pass

for i in my_json:
    # print(i)
    pass

for v in my_json.values():
    # print(v)
    pass
