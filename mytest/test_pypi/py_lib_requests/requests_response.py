#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/2 19:05
# @Author  : Wind
# @Des     : 
# @Site    : 
# @File    : requests_response.py
# @Software: PyCharm
import requests


# response
r = requests.get('https://github.com/timeline.json')

print('json\n', r.json(), '\n')  # 返回json
print('url\n', r.url, '\n')  # 返回url编码
print('text\n', r.text, '\n')  # 返回页面内容

print('header\n', r.headers, '\n')  # 返回response头部
print('headerContent-Type\n', r.headers['Content-Type'], '\n')  # 返回response头部
print('headerContent-Type\n', r.headers.get('content-type'), '\n')

print('cookies\n', r.cookies, '\n')  # 返回cookies
print('history\n', r.history, '\n')
print('encoding\n', r.encoding)  # 返回页面编码
