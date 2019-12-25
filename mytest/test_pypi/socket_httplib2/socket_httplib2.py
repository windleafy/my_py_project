#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""tmp"""
# @Time    : 2019/10/30 11:05
# @Author  : Wind
# @Des     : 
# @Software: PyCharm  Python3.7.2
import socket
import httplib2
from httplib2 import socks

print(socket.getaddrinfo('www.baidu.com', 'http'))
print(socket.getaddrinfo('www.baidu.com', 'https'))

# 根据域名，获取IP地址
print(socket.getaddrinfo('www.baidu.com', 'http')[0][4][0])

h = httplib2.Http()
response, content = h.request('https://www.baidu.com/')

# 设置代理访问
h = httplib2.Http(proxy_info=httplib2.ProxyInfo(socks.PROXY_TYPE_SOCKS5, 'localhost', 1080), timeout=60)
# h = httplib2.Http(proxy_info=httplib2.ProxyInfo(2, '127.0.0.1', 1080), timeout=60)
r, c = h.request("https://www.google.com/")
print(r)
