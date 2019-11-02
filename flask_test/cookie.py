#!/usr/bin/env python
"""cookie测试
xxx = Response('html_txt')
xxx.set_cookie(key='name', value='letian', expires=time.time()+6*60)
xxx.set_cookie(key='name', value='letian', max_age=30)
request.cookies.__str__()
"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 15:31
# @Author  : Wind
# @Des     :
# @Software: PyCharm

from flask import Flask, request, Response, make_response
import time

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/add')
def login():
    # 返回给web页面的文本
    res = Response('test')
    # cookies时长的两个参数:max_age  expires
    # res.set_cookie(key='name', value='letian', expires=time.time()+30)
    res.set_cookie(key='name0', value='letian0', max_age=30)
    res.set_cookie(key='name1', value='letian1', max_age=30)
    return res


@app.route('/show')
def show():
    # 返回cookie值
    return request.cookies.__str__()


@app.route('/del_0')
def del_cookie0():
    res = Response('delete cookie0')
    res.set_cookie('name0', expires=0)
    return res


@app.route('/del_1')
def del_cookie2():
    response = make_response('delete cookie1')
    response.delete_cookie('name1')
    return response


if __name__ == '__main__':
    app.run(debug=True)
