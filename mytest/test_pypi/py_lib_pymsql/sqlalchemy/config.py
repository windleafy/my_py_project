#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""tmp"""
# @Time    : 2019/11/1 9:11
# @Author  : Wind
# @Des     : 
# @Software: PyCharm  Python3.7.2
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# 基类
Base = declarative_base()


# 定义表 1
class User(Base):
    """
    定义表结构
    """
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))


# 定义表 2
class Client(Base):
    """
    定义表结构
    """
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(32))
    weight = Column(String(64))


# 定义表 3
class Stu(Base):
    """
    定义表结构
    """
    __tablename__ = 'stu'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(32))
    height = Column(String(64))
