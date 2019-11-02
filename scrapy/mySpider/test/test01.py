#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""test01"""
# @Time    : 2019/10/27 15:56
# @Author  : Wind
# @Des     : 
# @Software: PyCharm
from urllib.parse import urlencode
data = {'ch': 'photography', 'listtype': 'new'}
base_url = 'https://image.so.com/zjl?'
for page in range(0, 5):
    data['sn'] = page * 30
    params = urlencode(data)
    url = base_url + params
    print(url)


