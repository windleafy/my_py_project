#!/usr/bin/env python
"""upload_client"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 10:55
# @Author  : Wind
# @Des     : 
# @Software: PyCharm

import requests

file_data = {'image': open('./res/3.jpg', 'rb')}

user_info = {'info': 'Lenna'}

r = requests.post("http://127.0.0.1:5000/uploads", data=user_info, files=file_data)

print(r.text)
