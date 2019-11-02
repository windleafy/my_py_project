#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""base_metadata"""
# @Time    : 2019/11/1 17:22
# @Author  : Wind
# 参考     : https://blog.csdn.net/xie_0723/article/details/84901502
# @Software: PyCharm  Python3.7.2
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base

# 定义基类
Base = declarative_base()


# 定义表的类
class User1(Base):
    """
    定义表结构
    """
    __tablename__ = 'user1'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))


# 定义表的类
class User2(Base):
    """
    定义表结构
    """
    __tablename__ = 'user2'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(32))
    age = Column(String(64))


# 定义表的类
class User3(Base):
    """
    定义表结构
    """
    __tablename__ = 'user3'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(32))
    height = Column(String(64))


# 定义引擎
engine = create_engine('mysql+pymysql://root:root@localhost:3306/new_db')


# 本地Base类中的所有表(immutabledict格式)
print(Base.metadata.tables)

# 取出本地Base类中所有表名
print(Base.metadata.tables.keys())

# 本地所有表名 + 从engine位置取回mysql数据库中的所有表名
Base.metadata.reflect(bind=engine)
print(Base.metadata.tables.keys())

# 取出指定表，并输出指定表的字段名
table_info = Base.metadata.tables['user1']
print(table_info.columns.keys)

# 取出指定表，并输出指定表的字段名
table_info = Table('user2', Base.metadata, autoload=True)
print(table_info.columns.keys())

# 创建指定表
tables = [Base.metadata.tables['user1'], Base.metadata.tables['user2']]
# 如没有tables参数，Base类中的所有表，都会被创建。
Base.metadata.create_all(engine, tables)


# -----------------------------
Base = automap_base()
print(Base)
# 从engine位置取回mysql数据库中的所有表名
Base.prepare(engine, reflect=True)
print(Base.classes.keys())
