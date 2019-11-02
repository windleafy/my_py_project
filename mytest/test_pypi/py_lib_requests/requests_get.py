#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/2 19:08
# @Author  : Wind
# @Des     : 
# @参考    : https://blog.csdn.net/lihao21/article/details/51857385
# @File    : requests_get.py
# @Software: PyCharm
import requests
from contextlib import closing


headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,und;q=0.6,zh-TW;q=0.5,ru;q=0.4",
    "Dnt": "1",
    "Host": "httpbin.org",
    "Referer": "https://httpbin.org/",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
    "cookies": '{}'
}

my_para = {'para1': 'value1', 'para2': 'value2', 'para3': 'value3'}

r = requests.get('https://httpbin.org/get', headers=headers, timeout=10, params=my_para, stream=False, verify=False)
print(r.url)
# print(r.text)
print(r.encoding)

