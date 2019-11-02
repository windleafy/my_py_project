#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""crt_tb_mvp"""
# @Time    : 2019/11/1 10:57
# @Author  : Wind
# @Des     : 
# @Software: PyCharm  Python3.7.2

from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base

# 定义基类
Base = declarative_base()


# 定义表的类
class User(Base):
    """
    定义表结构
    """
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))


# 定义引擎
engine = create_engine('mysql+pymysql://root:root@localhost:3306/new_db')

# 创建表
Base.metadata.create_all(engine)



