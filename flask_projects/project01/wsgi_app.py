#!/usr/bin/env python
"""wsgi最小应用"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 10:05
# @Author  : Wind
# @Des     : 
# @Software: PyCharm


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']
