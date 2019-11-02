#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""sqlalchemy05"""
# @Time    : 2019/10/31 18:09
# @Author  : Wind
# @Des     : 创建数据库(sql模式)
# @Software: PyCharm  Python3.7.2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import re

engine = create_engine('mysql+pymysql://root:root@localhost:3306')
DBSession = sessionmaker(bind=engine)
session = DBSession()
# 创建数据库
try:
    sql = 'create database new_db'
    session.execute(sql)
except Exception as e:
    if re.search('database exists', str(e)):
        print('数据库已存在！')
else:
    print('数据库创建成功!')
session.close()
