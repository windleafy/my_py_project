#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""tmp"""
# @Time    : 2019/10/30 11:05
# @Author  : Wind
# @Des     : 自动登录github测试
# @Software: PyCharm  Python3.7.2
# 参考文档https://www.cnblogs.com/wuzdandz/p/9338543.html

import requests
from bs4 import BeautifulSoup
# 第一步：发送第一次请求，获取csrftoken
r1 = requests.get(
    url='https://github.com/login'
)
r1_cookie = r1.cookies.get_dict()
print(r1_cookie)

# 对获取到的文本对象解析获取token值
bs1 = BeautifulSoup(r1.text, 'html.parser')
obj_token = bs1.find(
    name='input',
    attrs={'name': 'authenticity_token'}
)
# token = obj_token.attrs.get('value')  # 获取token值的两种方式
token = obj_token.get('value')
print(token)

# 第二步：发送post请求，携带用户名密码并伪造请求头
r2 = requests.post(
    url='https://github.com/session',
    data={
        'commit': 'Sign in',
        'utf8': '✓',
        'authenticity_token': token,
        'login': 'ydfwind@163.com',
        'password': '?96!;{w*bX&kiR-+'
    },
    cookies=r1_cookie  # 带入第一次的cookie做验证
)
r2_cookie = r2.cookies.get_dict()
print(r2_cookie)
# print(r2.text)
print(f'status_code:{r2.status_code}')

r1_cookie.update(r2_cookie)  # 更新到第一次response的cookie字典里
print(r1_cookie)

# 第三步：访问个人页面，携带cookie
r3 = requests.get(
    url='https://github.com/settings/repositories',
    cookies=r1_cookie  # 带入cookie肆意妄为
)
# print(r3.text)
