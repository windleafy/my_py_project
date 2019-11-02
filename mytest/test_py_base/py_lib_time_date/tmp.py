#!/usr/bin/env python
"""tmp"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/7 21:15
# @Author  : Wind
# @Des     : 
# @Software: PyCharm
from datetime import datetime

# 当前时间
print(datetime.now().today())
print(datetime.now().today().strftime('%Y-%m-%d %H:%M:%S'))
# 输出
# 2019-10-09 13:47:15.313482
# 2019-10-09 13:47:15

# 年月日时分秒输出方式一
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)
print(datetime.now().hour)
print(datetime.now().minute)
print(datetime.now().second)
# 输出
# 2019
# 10
# 9
# 13
# 47
# 15

# 年月日时分秒输出方式二
print(datetime.now().strftime('%Y'))
print(datetime.now().strftime('%m'))
print(datetime.now().strftime('%d'))
print(datetime.now().strftime('%H'))
print(datetime.now().strftime('%M'))
print(datetime.now().strftime('%S'))

#  输出
#  2019
# 10
# 09
# 13
# 47
# 15
