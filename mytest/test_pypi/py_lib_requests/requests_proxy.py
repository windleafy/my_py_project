#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/2 18:34
# @Author  : Wind
# @Des     : requests设置代理访问
# @Site    : 
# @File    : requests_proxy.py
# @Software: PyCharm
import requests


# 设置访问代理
proxies = {
           "http": "http://10.10.1.10:3128",
           "https": "http://10.10.1.100:4444",
          }
r = requests.get('http://m.ctrip.com', proxies=proxies)

# 如果代理需要用户名和密码，则需要这样：
proxies = {
    "http": "http://user:pass@10.10.1.10:3128/",
}
r = requests.get('http://m.ctrip.com', proxies=proxies)
