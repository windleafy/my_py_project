#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""admin_module"""
# @Time    : 2019/10/22 10:03
# @Author  : Wind
# @Des     : 
# @Software: PyCharm
from flask import Blueprint, url_for

# 创建蓝图对象
# 'admin'是蓝图名称，__name__是模块名称
admin_bp = Blueprint('admin', __name__, url_prefix='/admin', static_folder='static')
# 创建蓝图的路由
@admin_bp.route('/')
def index():
    print(admin_bp.root_path)
    print(url_for('.index'))
    print(url_for('admin.index'))

    print(url_for('.static', filename='style.css'))
    print(url_for('admin.static', filename='style.css'))
    return 'Hello, this is admin blueprint'
