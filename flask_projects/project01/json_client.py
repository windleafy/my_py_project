#!/usr/bin/env python
"""client"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 9:16
# @Author  : Wind
# @Des     : 
# @Software: PyCharm
import requests

json_str = {'value1': 10, 'value2': 20}
url = 'http://localhost:5000/'
r = requests.get(url, json=json_str)
print(r.headers)
print(f'服务器计算结果:{r.text}')
