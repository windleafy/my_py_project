#!/usr/bin/env python
"""session01"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 16:56
# @Author  : Wind
# @Des     : 
# @Software: PyCharm
import os
from datetime import timedelta

from flask import Flask, render_template_string, \
    session, request, redirect, url_for

app = Flask(__name__)

app.permanent_session_lifetime = timedelta(minutes=20)
app.permanent_session_lifetime = timedelta(seconds=20)
app.secret_key = r'F12Zr47j\3yX R~X@H!jLwf/T'


@app.route('/')
def hello_world():
    return f'hello {os.path.basename(__file__)}'


@app.route('/login')
def login():
    page = '''
    <form action="{{ url_for('do_login') }}" method="post">
        <p>name: <input type="text" name="user_name" /></p>
        <input type="submit" value="Submit" />
    </form>
    '''
    return render_template_string(page)


@app.route('/do_login', methods=['POST'])
def do_login():
    name = request.form.get('user_name')
    session['user_name'] = name
    return 'success'


@app.route('/show')
def show():
    if 'user_name' in session:
        return session['user_name']
    else:
        return 'time out!'


@app.route('/logout')
def logout():
    session.pop('user_name', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(port=5000, debug=True)
