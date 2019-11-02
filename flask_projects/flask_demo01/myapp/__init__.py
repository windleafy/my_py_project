#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""__init__.py"""
# @Time    : 2019/10/25 10:57
# @Author  : Wind
# @Des     : 创建app
# @Software: PyCharm
from flask import Flask
from myapp.admin import admin_bp


app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(admin_bp)

# 需要先实例化应用，再引入视图
from myapp import views
