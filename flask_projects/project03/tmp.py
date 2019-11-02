#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""tmp"""
# @Time    : 2019/10/23 17:02
# @Author  : Wind
# @Des     : 与mytest一起，实现在蓝图中登录数据库
# @Software: PyCharm
from flask import Flask, url_for
from mytest.mytest import mytest_bp

app = Flask(__name__)
# 注册蓝图
app.register_blueprint(mytest_bp)

app.secret_key = '123456'


@app.route('/')
def hello_world():
    print(url_for('static', filename='style.css'))
    return 'Hello World!'


@app.route('/login/')
def login():
    return "Hi man I'm tmp.py's login"


def my_route():
    print('my_route')
    return 'welcome to my route!'


app.add_url_rule('/my_route', view_func=my_route)

if __name__ == '__main__':
    app.run()
