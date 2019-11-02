#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/1 16:51
# @Author  : Wind
# @Des     : 
# @Site    : 
# @File    : date01.py
# @Software: PyCharm

from datetime import datetime, date, timedelta

# 获取明天的日期值
tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
print(tomorrow)
tomorrow = (date.today() + timedelta(days=1)).strftime("%m")
print(int(tomorrow))
tomorrow = (date.today() + timedelta(days=1)).strftime("%d")
print(tomorrow)


# 返回明天的星期值
def get_day(day_offset):
    # @ day_offset = 0，今天的星期，1是明天，-1是昨天
    day_of_week = (date.today() + timedelta(days=day_offset)).weekday()
    if day_of_week == 0:
        return '星期一'
    if day_of_week == 1:
        return '星期二'
    if day_of_week == 2:
        return '星期三'
    if day_of_week == 3:
        return '星期四'
    if day_of_week == 4:
        return '星期五'
    if day_of_week == 5:
        return '星期六'
    if day_of_week == 6:
        return '星期日'


my_day = -1
print(get_day(my_day))

from datetime import datetime
print(datetime.now().date())
print(datetime.now().strftime("%Y-%m-%d"))

print(datetime.now().year)
print(datetime.now().strftime('%Y'))

print(datetime.now().month)
print(datetime.now().strftime('%m'))

print(datetime.now().day)
print(datetime.now().strftime('%d'))

print(datetime.now().hour)
print(datetime.now().strftime('%H'))

print(datetime.now().minute)
print(datetime.now().strftime('%M'))

print(datetime.now().second)
print(datetime.now().strftime('%M'))


print(date.today().strftime("%Y"))
print(date.today().strftime("%m"))
print(date.today().strftime("%d"))


