#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 21:40
# @Author  : Wind
# @Des     : 
# @Site    : 
# @File    : re_test.py
# @Software: PyCharm

import re

regular_v1 = re.findall(r"docs", "https://docs.python.org/3/whatsnew/3.6.html")
print(regular_v1)
# ['docs']

regular_v2 = re.findall(r"^https", "https://docs.python.org/3/whatsnew/3.6.html")
print(regular_v2)
# ['https']

regular_v3 = re.findall(r"html$", "https://docs.python.org/3/whatsnew/3.6.html")
print(regular_v3)
# ['html']

regular_v4 = re.findall(r"[t,w]h", "https://docs.python.org/3/whatsnew/3.6.html")
print(regular_v4)
# ['th', 'wh']

regular_v5 = re.findall(r"\d", "https://docs.python.org/3/whatsnew/3.6.html")
print(regular_v5)
# ['3', '3', '6']

regular_v6 = re.findall(r"\d\d\d", "https://docs.python.org/3/whatsnew/3.6.html/1234")
print(regular_v6)
# ['123']

regular_v7 = re.findall(r"\D", "https://docs.python.org/3/whatsnew/3.6.html")
print(regular_v7)
# 匹配非数字

regular_v8 = re.findall(r"\w", "https://docs.python.org/3/whatsnew/3.6.html")
print(regular_v8)
# 匹配单词字符，匹配字母或数字或下划线或汉字 等价于 ‘[A-Za-z0-9_]’

regular_v9 = re.findall(r"\W", "https://docs.python.org/3/whatsnew/3.6.html")
print(regular_v9)
# 匹配非单词字符


# py_lib_re.S实例
a = '''asdfsafhellopass:
    234455
    worldafdsf
    '''

b = re.findall('hello(.*?)world', a)
c = re.findall('hello(.*?)world', a, re.S)
print('b is ', c)


def check_password(passwd):
    if re.match(r'^(?=.*[A-Za-z])(?=.*[0-9])\w{6,}$', passwd):
        print("password %s correct" % passwd)
        return True
    else:
        print("password %s is invalid" % passwd)
        return False


passwd = "1dsfsdfaAXDSF"
check_password(passwd)
