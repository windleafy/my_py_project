#!/usr/bin/env python
"""config"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 11:51
# @Author  : Wind
# @Des     : 
# @Software: PyCharm
SECRET_KEY = 'flaskMysql'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:port/flask'
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True