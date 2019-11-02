#!/usr/bin/env python
"""flask02
session过期时间设置
app.permanent_session_lifetime = datetime.timedelta(seconds=30)
session.permanent = True
# 设置session密钥
app.secret_key = '000000'
"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11 21:39
# @Author  : Wind
# @Des     : post login session logout
# @Software: PyCharm
import datetime
from flask import Flask, Markup, render_template, request, session, url_for, redirect

app = Flask(__name__)
app.permanent_session_lifetime = datetime.timedelta(seconds=30)

# 首页
@app.route('/')
def index():
    # 关闭Flask内的自动转义
    return Markup('<div>Hello %s</div>') % '<em>Flask</em>'


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

# 登录
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # user定义在login.html input中
        if request.form['user'] == 'admin':
            # 保存session
            session.permanent = True
            session['user'] = request.form['user']
            session['age'] = 15
            return 'Admin login successfully!'
        else:
            return 'No such user!'
    if 'user' in session:
        return f'Hello {session["user"]},your age is {session["age"]}'
    else:
        title = request.args.get('title', '亲爱的亲')
        return render_template('login.html', title=title)


# 设置session密钥
app.secret_key = '000000'

# 登出
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
