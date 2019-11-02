#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""mytest"""
# @Time    : 2019/10/23 17:03
# @Author  : Wind
# @Des     : 在蓝图中读取config.py配置信息
#  @Des    : 蓝图中url_for取函数名时，需要加"."，比如url_for('.login')，url_for('.index')
# @Software: PyCharm
from flask import Blueprint, render_template, redirect, request, session, url_for, g, flash
import sqlite3
import config

mytest_bp = Blueprint('mytest', __name__, url_prefix='/mytest',
                      template_folder='templates',
                      static_folder='static')

mytest_bp.config = config


@mytest_bp.before_request
def before_request():
    g.db = sqlite3.connect(mytest_bp.config.DATABASE)


@mytest_bp.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


@mytest_bp.route('/')
def index():
    if 'user' in session:
        return render_template('hello.html', name=session['user'])
    else:
        return redirect(url_for('.login'))


@mytest_bp.route('/login', methods=['POST', 'GET'])
def login():
    print('/login')
    if request.method == 'POST':
        print('method=post')
        name = request.form['user']
        print(name)
        passwd = request.form['passwd']
        cursor = g.db.execute('select * from users where name=? and password=?', [name, passwd])
        if cursor.fetchone() is not None:
            session['user'] = name
            flash('Login successfully!')
            return redirect(url_for('.index'))
        else:
            flash('No such user!', 'error')
            return redirect(url_for('.login'))
    else:
        print('method=get')
        return render_template('login.html')


@mytest_bp.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('.login'), 302)
