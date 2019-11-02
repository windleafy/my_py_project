#!/usr/bin/env python
"""data_type"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/6 12:15
# @Author  : Wind
# @Des     : 
# @Software: PyCharm

string = ['apple', 'pear', 'orange', 'mellon', 'banana', 'jujube']
print(','.join(string))

string = ('apple', 'pear', 'orange', 'mellon', 'banana', 'jujube')
print(','.join(string))

dict_test = {'apple': 100, 'pear': 200, 'orange': 300, 'mellon': 400, 'banana': 500, 'jujube': 600}
print(','.join(dict_test))

for v in dict_test.keys():
    dict_test[v] = str(dict_test[v])

print(','.join(list(dict_test.values())))

