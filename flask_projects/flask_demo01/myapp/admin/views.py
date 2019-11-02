#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""admin"""
# @Time    : 2019/10/25 10:59
# @Author  : Wind
# @Des     : 创建admin蓝图视图
# @Software: PyCharm
from myapp.admin import admin_bp


@admin_bp.route('/')
def index():
    return 'Hello my app admin'
