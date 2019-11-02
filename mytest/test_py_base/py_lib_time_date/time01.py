#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/1 16:49
# @Author  : Wind
# @Des     : 
# @Site    : 
# @File    : time01.py
# @Software: PyCharm

import time
import datetime

# 当前日期与时间未格式化
print('1: ', datetime.datetime.now())

# 当前日期
print('2: ', datetime.datetime.now().date())

# 当前日期与时间格式化
print('3: ', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 与指定时间点的时间差
print('4: ', (datetime.datetime.now() - datetime.datetime(2019, 2, 23, 15, 0, 0)).total_seconds())

# 时间差测试
time0 = (datetime.datetime.now())
i = 0
while i < 5:
    time.sleep(0.1)
    i += 1
time1 = (datetime.datetime.now())
duration = time1 - time0
print('5: ', duration)

# 13位时间戳
millis = int(round(time.time() * 1000))
print('6: ', millis)
