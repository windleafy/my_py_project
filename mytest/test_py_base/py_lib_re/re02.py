#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/1 14:33
# @Author  : Wind
# @Des     : Python re模块
# @Site    : 
# @File    : re02.py
# @Software: PyCharm

import re

'''
Python中常用re方法：
py_lib_re.search
py_lib_re.match
py_lib_re.sub
py_lib_re.compile
py_lib_re.split
'''

# re.search实例  从字符串中匹配出字典
s = '1102231990xxxxxxxx'
res = re.search(r'(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})', s)
print(res.groupdict())

phone = "2004-959-559 # 这是一个国外电话号码"
# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print("电话号码是: ", num)

# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print("电话号码是 : ", num)

# 一般正则匹配写法
my_string = 'one12twothree34four'
print(re.match(r'one', my_string))

# 定义匹配模式的正则写法
pattern = re.compile(r'one')
print(pattern.match(my_string))

tmp = re.split(r'\W+', r'runoob, runoob, runoob.')
print(tmp)

# 定义分割次数为1
tmp = re.split(r'\W+', ' runoob, runoob, runoob.', 1)
print(tmp)

r'''
py_lib_re.I 忽略大小写
py_lib_re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
py_lib_re.M 多行模式
py_lib_re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
py_lib_re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
py_lib_re.X 为了增加可读性，忽略空格和 # 后面的注释
'''

# 没有匹配成功的，re.search（）返回None
a = "123abc456"
print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(0))  # 123abc456,返回整体
print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(1))  # 123
print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(2))  # abc
print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(3))  # 456
