#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""auth"""
# @Time    : 2019/10/21 14:28
# @Author  : Wind
# @Des     : 安全认证
# @Software: PyCharm

# pip install flask-httpauth
from flask import make_response, jsonify, Flask, g
from flask_httpauth import HTTPBasicAuth
app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):
    # 待验证账号
    if username == 'wind':
        # 待验证密码
        return 'welcome'
    return None

# 用户名、密码输入界面，点击“取消”，返回以下内容。
@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

# 访问根节点弹出用户名密码输入框
@app.route('/', methods=['GET'])
@auth.login_required
def index():
    return 'hello wind!'

# 登出
@app.route('/logout')
def logout():
    g.user = None
    return 'Logout', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
