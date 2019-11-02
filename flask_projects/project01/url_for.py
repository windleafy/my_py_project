#!/usr/bin/env python
"""url_for"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 16:29
# @Author  : Wind
# @Des     : 
# @Software: PyCharm
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    pass


@app.route('/user/<name>')
def user(name):
    pass


@app.route('/page/<int:num>')
def page(num):
    pass


@app.route('/test')
def test():
    print(url_for('hello_world'))
    print(url_for('user', name='letian'))
    print(url_for('page', num=1, q='hadoop mapreduce 10%3'))
    print(url_for('static', filename='uploads/01.jpg'))
    return 'Hello'


if __name__ == '__main__':
    app.run(debug=True)
