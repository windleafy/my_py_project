#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/2 19:56
# @Author  : Wind
# @Des     : 
# @Site    : 
# @File    : requests_01_header.py
# @Software: PyCharm

import requests

print(dir(requests))

# url = 'http://www.w3school.com.cn/i/movie.mp4'
url = 'http://ftp-idc.pconline.com.cn/ceff57a41e12f1cd0a46706630efa2c5/pub/download' \
      '/201010/HD.Club-4K-Chimei-inn-20mbps.rar'

# 只加载头部
response = requests.head(url)
print(response)
print(response.status_code)
print(response.headers)
print(int(response.headers['Content-Length'])/1000000, 'MB')
