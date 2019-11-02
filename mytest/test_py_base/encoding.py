#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/1 16:24
# @Author  : Wind
# @Des     : 
# @Site    : 
# @File    : encoding.py
# @Software: PyCharm

# unicode字符串
s1 = '\u0061\u4e5d\u9f8d\u65fa\u89d2\u5f4c\u6566\u9053628\u865f\u74ca\u83ef\u4e2d\u5fc310\u6a13\u5168\u5c64'
print(s1)
print(s1.encode('utf-8'))
print(s1.encode('utf-8').decode('utf-8'))

# 字符串
s1 = r'\u4e5d\u9f8d\u65fa\u89d2\u5f4c\u6566\u9053628\u865f\u74ca\u83ef\u4e2d\u5fc310\u6a13\u5168\u5c64'
print('\n')
print(s1)
print(s1.encode('utf-8'))
print(s1.encode('utf-8').decode('unicode_escape'))

# 字符串
s2 = "\\u4e5d\\u9f8d\\u65fa\\u89d2\\u5f4c\\u6566\\u9053628\\u865f\\u74ca\\u83ef\\u4e2d\\u5fc310\\u6a13\\u5168" \
     "\\u5c64"
print('\n')
print(s2)
print(s2.encode('utf-8'))
print(s2.encode('utf-8').decode('unicode_escape'))

# unicode字符串
s1 = "23.11.93 | From Lucca |\n\ud83d\udd39\ufe0fMaster's in Molecular Biotechnology \ud83c\uddee\ud83c\uddf9\n" \
     "\ud83d\udd39\ufe0f#travel around Europe\n\ud83d\udd39\ufe0flove #writing \n\u27a1\ufe0f\ud83c\uddec\ud83c" \
     "\udde7 \ud83c\udde8\ud83c\uddff \ud83c\uddee\ud83c\uddea \ud83c\uddeb\ud83c\uddf7 \ud83c\udde9\ud83c\uddea " \
     "\ud83c\uddea\ud83c\uddf8 \ud83c\udde6"
s2 = "\u2022Name \u9673\u53ef\u9821(\u3110\u3127\u311d\u02ca)\n\u2022\u6d6aLive\ud83d\udcacID1246759\n\u2022\u4ee3" \
     "\u8a00\u3001\u5de5\u4f5c\u9080\u7d04Instagram\u5c0f\u76d2\u5b50\n\ud83d" \
     "\uded2Ootd Closet Instagram/Shopee @migi_ootd \ud83d\uded2"

# 有非标准utf-8字符，需要ignore参数忽略，否则报错
print(s1.encode('utf-8', 'ignore').decode('utf-8'))
print('\n')
print(s2.encode('utf-8', 'ignore').decode('utf-8'))

print('\n')
print('a' == '\u0061')
# 输出：True

# 字符串转utf-8编码
print('abc中文100'.encode('utf-8', 'ignore'))
# 输出：b'abc\xe4\xb8\xad\xe6\x96\x87100'

# utf-8解码
print(b'abc\xe4\xb8\xad\xe6\x96\x87100'.decode('utf-8'))
# 输出：abc中文100

# utf-8解码
print(b'\xc2\xbb'.decode('utf-8'))
# 输出：»


''''''
# 字符串转二进制形式的unicode编码
print('abc中文100'.encode('unicode_escape'))
# 输出：b'abc\\u4e2d\\u6587100'

# 二进制形式的unicode编码解码
print(b'abc\\u4e2d\\u6587100'.decode('unicode_escape'))
# 输出：abc中文100


''''''
# 字符串形式的unicode编码转utf-8编码
print('abc\u4e2d\u6587100'.encode('utf-8', 'ignore'))
# 输出：b'abc\xe4\xb8\xad\xe6\x96\x87100'

# utf-8解码
print(b'abc\xe4\xb8\xad\xe6\x96\x87100'.decode('utf-8'))
# 输出：abc中文100


''''''
# 字符串形式的unicode编码可以直接输出
print('abc\u4e2d\u6587100')

# 如果有不可识别的unicode字符，可以先编码，并忽略不认识的字符，再解码。
print('abc\u4e2d\u6587100\u0000'.encode('utf-8', 'ignore').decode('utf-8'))

s = '中文'
s = s.encode('gbk')
print(s)
