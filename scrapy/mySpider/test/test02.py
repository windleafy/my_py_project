#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""test02"""

# @Time    : 2019/10/28 18:25
# @Author  : Wind
# @Des     : 
# @Software: PyCharm

mydict = {'id': '92ee2c56ce5c5f9471c5aa365dd23138',
          'thumb': 'https://p0.ssl.qhimgs1.com/sdr/200_200_/t01b4ceee9274ccd776.jpg',
          'title': '光滑面,陶器,盘子,装饰,厨房用桌,午餐',
          'url': 'https://p0.ssl.qhimgs1.com/t01b4ceee9274ccd776.jpg'}

keys = ', '.join(mydict.keys())
print(keys)

values = ', '.join(['%s'] * len(mydict))
print(values)


tmp = tuple(mydict.values())
print(tmp)

sql ='insert into %s (%s) values (%s)'% ('table_name', keys, values)
print(sql)

