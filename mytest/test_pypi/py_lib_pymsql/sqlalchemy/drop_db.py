#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""drop_db"""
# @Time    : 2019/10/31 20:4:16
# @Author  : Wind
# @Des     : 删除数据库
# @Software: PyCharm  Python3.7.2
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, drop_database

uri = 'mysql+pymysql://root:root@localhost:3306/wind_test1'
engine = create_engine(uri)

if not database_exists(engine.url):
    print('数据库不存在')
else:
    drop_database(uri)
    print('数据库已删除')
