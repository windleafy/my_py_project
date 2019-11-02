#!/usr/bin/env python
"""post_test"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 17:32
# @Author  : Wind
# @Des     : https://www.letianbiji.com/python-flask/py-flask-post-data.html
# @Software: PyCharm
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/register', methods=['POST'])
def register():
    print(request.headers)
    print(request.stream.read())
    return 'welcome'


if __name__ == '__main__':
    app.run(port=5000, debug=True)
