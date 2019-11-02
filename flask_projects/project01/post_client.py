#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""post_client"""
# @Time    : 2019/10/21 11:04
# @Author  : Wind
# @Des     : https://www.letianbiji.com/python-flask/py-flask-post-data.html
# @Software: PyCharm

import requests

user_info = {'name': 'letian', 'password': '123'}
r = requests.post("http://127.0.0.1:5000/register", data=user_info)

print(r.text)
