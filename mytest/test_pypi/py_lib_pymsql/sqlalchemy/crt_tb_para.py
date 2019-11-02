#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""sqlalchemy02"""
# @Time    : 2019/10/31 14:29
# @Author  : Wind
# @Des     : 创建数据表
# @Software: PyCharm  Python3.7.2
import re
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine(
    'mysql+pymysql://root:root@localhost:3306/new_db',
    max_overflow=2,  # 超过连接池大小外最多创建的数量,
    pool_size=5,  # 连接池的大小
    pool_timeout=30,  # 池中没有线程最多等待的时间
    pool_recycle=-1,  # 多久之后对线程中的线程进行一次连接的回收(重置)
)

# 创建数据表
table_name = 'user'


class User(Base):
    """
    定义表结构
    """
    __tablename__ = table_name
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))


def crt_tb(tb_name):
    """
    根据表名，创建表。会判断数据库是否存在，表是否存在。
    """
    try:
        metadata = MetaData(engine)
        # 通过反射，判断表是否已存在
        Table(tb_name, metadata, autoload=True)
    except Exception as e:
        # print(e)
        if re.search('Unknown database', str(e)):
            print('数据库不存在!')
        elif str(e) == f'`{tb_name}`':  # 数据表不存在时，返回的是表名
            Base.metadata.create_all(engine)
            print('数据表创建成功！')
        else:
            print(e)
    else:
        print('数据表已存在！')


def del_tb(tb_name):
    """
    根据表名，创建表。会判断数据库是否存在，表是否存在。
    """
    try:
        metadata = MetaData(engine)
        # 通过反射，判断表是否已存在
        Table(tb_name, metadata, autoload=True)
    except Exception as e:
        if re.search('Unknown database', str(e)):
            print('数据库不存在!')
        elif str(e) == f'`{tb_name}`':  # 数据表不存在时，返回的是表名
            print('数据表不存在！')
        else:
            print(e)
    else:
        Base.metadata.drop_all(engine)
        print('删除数据表成功！')


crt_tb(table_name)


