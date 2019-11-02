#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""sqlalchemy03"""
# @Time    : 2019/10/31 15:33
# @Author  : Wind
# @Des     : 反射是否已存在表
# 参考     : https://blog.csdn.net/xie_0723/article/details/84901502
# @Software: PyCharm  Python3.7.2
from sqlalchemy import MetaData, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base

uri = 'mysql+pymysql://root:root@localhost:3306/wind_test'

engine = create_engine(uri, echo=False)

# 方法一
metadata = MetaData(engine)
try:
    apply_info = Table('aa', metadata, autoload=True)
    # apply_info = metadata.tables['bb']
    # 获取字段名
    print(apply_info.columns.keys())
except Exception as e:
    print(f'没有找到表:{e}')

# 方法二
Base = declarative_base()
try:
    apply_info = Base.metadata.tables['cc']
except Exception as e:
    print(f'没有找到表:{e}')
