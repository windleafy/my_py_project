#!/usr/bin/env python
"""session测试
xxx = Response('html_txt')
xxx.set_cookie(key='name', value='letian', expires=time.time()+6*60)
xxx.set_cookie(key='name', value='letian', max_age=30)
request.cookies.__str__()
"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11 21:39
# @Author  : Wind
# @Des     : post login session logout
# @Software: PyCharm
import datetime
from flask import Flask, Markup, request, session, url_for, redirect

app = Flask(__name__)
app.permanent_session_lifetime = datetime.timedelta(seconds=30)
# 设置session密钥
app.secret_key = '000000'

# 首页
@app.route('/')
def index():
    return Markup('<div>Hello %s</div>') % '<em>Flask</em>'


# 登录
@app.route('/login', methods=['POST', 'GET'])
def login():
    session.permanent = True
    session['user'] = 'mike'
    session['age'] = 15
    return f'姓名{session["user"]}年龄{session["age"]}'

# 显示cookie
@app.route('/show')
def show():
    # 返回cookie值
    return request.cookies.__str__()

# 登出
@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('age', None)
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
