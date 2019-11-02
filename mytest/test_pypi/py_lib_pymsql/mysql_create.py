#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""mysql_create"""
# @Time    : 2019/10/30 12:30
# @Author  : Wind
# @Des     : 
# @Software: PyCharm  Python3.7.2

from test_pypi.py_lib_pymsql.config import mysql_cfg
from base_kit.base_mysql import MysqlPython
from test_pypi.py_lib_pymsql.config.tables import students

tmp = MysqlPython(
    host=mysql_cfg.host,
    port=mysql_cfg.port,
    user=mysql_cfg.user,
    pwd=mysql_cfg.pwd,
)

'''
db_name = 'wind_create'
tmp.create_db(db_name)
tmp.close()
'''

# 设定要建表的数据库
db_name = 'wind_create'
# 创建表
target_table = students
tmp.create_table(db_name, target_table)
tmp.close()
