#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/2 17:20
# @Author  : Wind
# @Des     : 
# @Site    : https://blog.csdn.net/lihao21/article/details/51857385
# @File    : requests_post.py
# @Software: PyCharm
import requests
import json

# 最基本的不带参数的get请求
# r = requests.get('https://github.com/Ranxf')
# print(r.status_code)
# print(r.text)

# url传入参数
search_item = {'wd': '李白'}
# r1 = requests.get(url='http://baidu.com/s', params=search_item)
# print(r1.url)  # 返回url编码
# print(r1.text)  # 返回页面内容
# print(r1.headers, '\n')  # 返回response头部
# print(r1.cookies, '\n')  # 返回cookies
# print(r1.history, '\n')
# print(r1.encoding)  # 返回页面编码


headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,und;q=0.6,zh-TW;q=0.5,ru;q=0.4",
    "Content-Length": "0",
    "Dnt": "1",
    "Host": "httpbin.org",
    "Origin": "http://httpbin.org",
    "Referer": "http://httpbin.org/",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
}

# post数据中有中文时，处理方法
# data1 = 'username=张三&password=123'
# data = bytes(json.dumps(data1, ensure_ascii=False), encoding="utf-8")

# data = '{username:amy, password:123}'

data = '{"username": "amy", "password": "12345"}'

my_para = {'para1': 'value1', 'para2': 'value2', 'para3': 'value3'}

r = requests.post('https://httpbin.org/post', headers=headers, data=data, timeout=10, params=my_para)
print(r.url)
print(r.text)
print(r.encoding)
