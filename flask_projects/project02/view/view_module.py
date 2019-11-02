#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""view_bp"""
# @Time    : 2019/10/22 16:21
# @Author  : Wind
# @Des     : URL集中映射，将url放在一个文件中，集中管理。
# @Software: PyCharm
from flask import Blueprint, request, render_template, session, url_for, redirect
import view.views


view_bp = Blueprint('view', __name__, url_prefix='/view',
                    template_folder='templates',
                    static_folder='static')


@view_bp.route('/')
def index():
    return 'welcome to view'


view_bp.add_url_rule('/foo', view_func=view.views.foo)
view_bp.add_url_rule('/bar', view_func=view.views.bar)


@view_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            session['user'] = request.form['user']
            return 'Admin login successfully!'
        else:
            return 'No such user!'
    if 'user' in session:
        return 'Hello %s!' % session['user']
    else:
        title = request.args.get('title', 'Default')
        return render_template('/login.html', title=title)


@view_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('view.login'))
