#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/1 10:34
# @Author  : Wind
# @Des     : 
# @Site    : 
# @File    : re01.py
# @Software: PyCharm

import re
r'''
常用
\d  匹配一个数字
\w  匹配一个字母或数字
\s  匹配一个空格
'''
# 0，0，1个数字
re.findall(r"00\d", 'hello word 007 is a hero')

# 1个数字，1个数字，1个数字
re.findall(r"\d\d\d", 'hello word 007 is a hero')

# 1个字母或数字，1个字母或数字，1个字母或数字
re.findall(r"\w\w\d", 'hello word xx7 is a hero')

'''
.表示任意字符
^表示字符串开头
$表示字符串结尾
'''
# 1个任意字符，1个任意字符，1个数字
re.findall(r"..\d", 'hello word 007 is a hero')

# 检测对象是否"hel"开头
re.findall(r"^hel", 'hello word 007 is a hero')
# 输出：['hel']

# 检测对象是否"ero"结尾
print(re.findall(r"ero$", 'hello word 007 is a hero'))
# 输出：['ero']

r'''
数量
*  匹配前面的子表达式零次或多次。要匹配 * 字符，请使用 \*。
+  匹配前面的子表达式一次或多次。要匹配 + 字符，请使用 \+。
?  匹配前面的子表达式零次或一次，或指明一个非贪婪限定符。要匹配 ? 字符，请使用 \?。
{n}  匹配前面的字符n次
{n,}  匹配前面的字符至少n次
{n,m}  匹配前面的字符n-m次
'''
# 3个数字,至少一个空格，3-8个数字
re.findall(r"\d{3}\s+\d{3,8}", 'hello word 007 008 is a hero')

# 3个数字，"-"，3-8个数字
re.findall(r"\d{3}-\d{3,8}", 'hello word 007-008 is a hero')

# 1个字符，可能是数字或英文字母（大小写）或"_"
re.findall(r"[0-9a-zA-Z_]", '_')

# 至少1个字符的字符串，包含数字或英文字母（大小写）或"_"
re.findall(r"[0-9a-zA-Z_]+", '_00) a? 0Xm你好&%')

# 1个字符(大小写字母或'_')，任意个字符(数字或大小写字母或'_')
re.findall(r"[a-zA-Z_][0-9a-zA-Z_]*", '_00) a? 0Xm你好&%')
# 输出：['_00', 'a', 'Xm']

# 目标字符串开头是1至多个数字，目标字符串结尾是任意个0
# ?非贪婪匹配
print(re.match(r'^(\d+?)(0*)$', '102300').groups())
# 输出：('1023', '00')

print(re.findall(r'^\d+?', '102300'))
# 输出：['1']

print(re.findall(r'^\d*?', '102300'))
# 输出：['', '1']

print(re.findall(r'^\d+3', '1023300'))
# 输出：['1023']

# 目标字符串开头是1至多个数字，目标字符串结尾是任意个0
print(re.match(r'^(\d+)(0*)$', '102300').groups())
# 输出：('102300', '')

re.findall(r"00\d", 'hello word 007 is a hero')
re.findall(r"00\d", 'hello word 007 is a hero')
re.findall(r"00\d", 'hello word 007 is a hero')
re.findall(r"00\d", 'hello word 007 is a hero')


tmp = re.findall(r"00\d", 'hello word 007 is a hero')
print(tmp)

# 匹配string 开头，成功返回Match object, 失败返回None，只匹配一个。
tmp = re.match("c", "abcdef")
print(tmp)

# 匹配string 开头，成功返回Match object, 失败返回None，只匹配一个。
tmp = re.search("^cd", "abcdef")
print(tmp)

# 检查字符串任意位置，成功返回Match object, 失败返回None, 只匹配一个。
tmp = re.search("cd", "abcdef")
print(tmp)

# 查找所有 匹配成功的组, 即用括号括起来的部分。返回list对象，每个list item是由每个匹配的所有组组成的list。
tmp = re.findall("cd", "abcdefgabcdeft")
print(tmp)

tmp = re.finditer("cd", "abcdefgabcdeft")
print(tmp)
