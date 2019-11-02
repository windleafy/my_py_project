#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/1 20:16
# @Author  : Wind
# @Des     : 
# @Site    : 
# @File    : excel_test.py
# @Software: PyCharm
import os
from os.path import dirname, abspath, relpath

from base_kit.base_xls import *


class Data:
    pass


data = Data
data.path = './outfile/03.xls'
data.sheet_name = '2003测试表'
data.value = [["名称", "价格", "出版社", "语言"],
              ["如何高效读懂一本书", "22.3", "机械工业出版社", "中文"],
              ["暗时间", "32.4", "人民邮电出版社", "中文"],
              ["拆掉思维里的墙", "26.7", "机械工业出版社", "中文"]]

# 03 写入测试
# write_03_excel(data)

# 03 读取测试
'''
get_03_data = read_03_excel(data.path)
for i in get_03_data:
    print(i)
'''

# 07 写入测试
'''
data.path = './outfile/07.xlsx'
data.sheet_name = '2007测试表'
write_07_excel(data)
'''

# 07 读取测试
data.path = './outfile/07.xlsx'
get_07_data = read_07_excel(data.path)
for i in get_07_data:
    print(i)


