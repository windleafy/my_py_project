#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""post_server2"""
# @Time    : 2019/10/21 11:31
# @Author  : Wind
# @Des     : https://www.letianbiji.com/python-flask/py-flask-post-data.html
# @Des     : request.form示例
# @Software: PyCharm

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/register', methods=['POST'])
def register():
    print(request.headers)
    # print(request.stream.read()) # 不要用，否则下面的form取不到数据
    print(request.form)
    print(request.form['name'])
    print(request.form.get('name'))
    print(request.form.getlist('name'))
    print(request.form.get('nickname', default='little apple'))
    return 'welcome'


if __name__ == '__main__':
    app.run(port=5000, debug=True)
