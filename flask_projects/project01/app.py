#!/usr/bin/env python
"""flask测试"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 9:57
# @Author  : Wind
# @Des     : wsgi demo
# @Software: PyCharm

from flask import Flask, render_template, redirect, url_for, request, session, make_response, Response, jsonify
import time
import json
from base_kit.secret_key import *


app = Flask(__name__)


@app.route('/')
def index():
    """基础路由"""
    # print(request.args.get('name'))
    # return 'hello flask!'
    # print(request.headers)

    # result = {'key1': 'value1', 'key2': 'value2'}
    # return Response(json.dumps(result), mimetype='application/json')
    # return jsonify(result)

    print(type(request.json))
    print(request.json)
    result = request.json['value1']+request.json['value2']
    return str(result)


@app.route('/welcome')
def welcome():
    """
    request.path、request.full_path、request.args.__str__()
    """
    print(request.path)
    print(request.full_path)
    # 如果name取值为None,返回''
    print(request.args.get('name', ''))
    return request.args.__str__()


@app.route('/login', methods=['POST', 'GET'])
def login():
    """
    post方法、get方法、cookie、session
    """
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            # 这里用到了session
            session['user'] = request.form['user']
            response = make_response('Admin login successfully!')
            # 这里用到了cookie，设定了cookie有效时间max_age=20秒，类似参数expires=20
            response.set_cookie('login_time', time.strftime('%Y-%m-%d %H:%M:%S'), max_age=20)
        else:
            response = make_response('No such user!')
    else:
        if ('user' in session) and (request.cookies.get('login_time') is not None):
            print(request.cookies.get('login_time'))
            login_time = request.cookies.get('login_time')
            response = make_response(f'Hello {session["user"]}, you logged in on {login_time}')
            # 输出cookie内容 request.cookies.__str__()
            print(request.cookies.__str__())
        else:
            title = request.args.get('title', 'Default')
            response = make_response(render_template('login.html', title=title), 200)

    return response


@app.route('/logout')
def logout():
    """
    清理session、重定向
    """
    session.clear()
    return redirect(url_for('login'))


# 设定session密钥
app.secret_key = generate_secret_key()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, processes=True)
