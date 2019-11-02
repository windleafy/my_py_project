#!/usr/bin/env python
"""wsgi"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 9:57
# @Author  : Wind
# @Des     : wsgi demo
# @Software: PyCharm

# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:
from wsgi_app import *


def application0(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, WSGI</h1>']


# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
# make_server是以函数为参数，创建了一个httpd服务
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()
