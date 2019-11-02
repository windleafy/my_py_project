#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""jinjia2-2"""
# @Time    : 2019年10月19日15:0:33
# @Author  : Wind
# @Des     : http://www.bjhee.com/jinja2-context.html
# @Software: PyCharm
from flask import Flask, render_template, session, g, flash
import time
from flask import current_app
import config

app = Flask(__name__)
# 因为要用session
app.secret_key = '123456'


@app.route('/')
def index():
    session['user'] = 'guest'
    g.db = 'mysql'
    g.debug = config.DEBUG
    g.db_pos = config.DATABASE
    info = 'wind access at ' + time.time().__str__()
    flash(info)
    return render_template('hello-2.html')

# 自定义上下文变量
@app.context_processor
def appinfo():

    return dict(appname=current_app.name)

# 自定义上下文函数
@app.context_processor
def get_current_time():

    def get_time(time_format="%b %d, %Y - %H:%M:%S"):
        return time.strftime(time_format)

    return dict(current_time=get_time)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
