#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""views"""
# @Time    : 2019/10/25 10:59
# @Author  : Wind
# @Des     : 创建main蓝图视图
# @Software: PyCharm
from myapp_fac.main import main_bp_fac


@main_bp_fac.route('/')
def index():
    return 'Hello my app main of fac!'
