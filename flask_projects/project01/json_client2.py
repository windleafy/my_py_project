#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""json_client2"""
# @Time    : 2019/10/21 16:24
# @Author  : Wind
# @Des     : 
# @Software: PyCharm

import requests

url = 'http://localhost:5000/'
r = requests.get(url)
print(r.headers)
print(type(r.json()))
print(r.json())
