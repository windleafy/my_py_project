#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""sqlalchemy02"""
# @Time    : 2019/10/31 14:29
# @Author  : Wind
# @Des     : 创建数据表
# @Software: PyCharm  Python3.7.2
import re
from sqlalchemy import create_engine, MetaData, Table
from test_pypi.py_lib_pymsql.sqlalchemy.config import *


def crt_tb(base, engine):
    """
    判断数据库是否存在，表是否已存在。
    :param base: 待创建表
    :param engine: 数据库引擎参数
    """
    try:
        metadata = MetaData(engine)
        # 通过反射，判断数据库与数据表是否存在
        Table(base.tb_name, metadata, autoload=True)
    except Exception as e:
        if re.search('Unknown database', str(e)):
            print('数据库不存在！')

        elif str(e) == f'`{base.tb_name}`':
            base.metadata.create_all(engine)
            print('数据表创建成功！')

        else:
            print(e)
    else:
        print('数据表已存在！')


def init_db_eg():
    # 数据引擎初始化
    db_uri = 'mysql+pymysql://root:root@localhost:3306/'
    db_name = 'new_db'
    eg = create_engine(
        db_uri + db_name,
        max_overflow=2,  # 超过连接池大小外最多创建的数量,
        pool_size=5,  # 连接池的大小
        pool_timeout=30,  # 池中没有线程最多等待的时间
        pool_recycle=-1,  # 多久之后对线程中的线程进行一次连接的回收(重置)
    )
    return eg


crt_tb(Stu, init_db_eg())
