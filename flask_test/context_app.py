#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""context_app"""
# @Time    : 2019/10/24 16:01
# @Author  : Wind
# @Des     : 
# @Software: PyCharm
from flask import Flask, current_app

app = Flask('MainApp')
sub_app = Flask('SubApp')

with app.app_context():
    print(current_app.name)
    with sub_app.app_context():
        print(sub_app.name)


@app.route('/')
def index():
    return 'Hello, %s!' % current_app.name


@app.teardown_appcontext
def teardown_db(exception):
    print('teardown application')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
