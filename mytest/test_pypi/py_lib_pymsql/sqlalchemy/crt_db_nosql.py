#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""sqlalchemy04"""
# @Time    : 2019/10/31 17:52
# @Author  : Wind
# @Des     : 创建数据库(非sql模式)
# @Software: PyCharm  Python3.7.2
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

uri = 'mysql+pymysql://root:root@localhost:3306/new_db'

engine = create_engine(uri)

if not database_exists(engine.url):
    create_database(engine.url)
    print('数据库创建成功')
else:
    print('数据库已存在')
