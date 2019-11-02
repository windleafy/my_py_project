#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""views"""
# @Time    : 2019/10/25 11:00
# @Author  : Wind
# @Des     : myapp下的视图文件
# @Software: PyCharm
from myapp import app


@app.route('/')
def index():
    return 'Hello my app'
