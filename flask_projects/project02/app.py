#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""__init__.py"""
# @Time    : 2019/10/22 10:02
# @Author  : Wind
# @Des     : 蓝图测试
# @Software: PyCharm
from flask import Flask, url_for
from admin.admin_module import admin_bp
from lang.lang_module import lang_bp
from view.view_module import view_bp


app = Flask(__name__)
# 注册蓝图
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(lang_bp)
app.register_blueprint(view_bp)


app.secret_key = '123456'


@app.route('/')
def hello_world():
    print(url_for('static', filename='style.css'))
    return 'Hello World!'


@app.route('/login/')
def login():
    return "Hi man I'm app.py's login"


if __name__ == '__main__':
    app.run()
