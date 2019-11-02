#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""sqlalchemy01"""
# @Time    : 2019/10/31 12:10
# @Author  : Wind
# @Des     : 
# @Software: PyCharm  Python3.7.2
import random

from sqlalchemy import Column, String, create_engine, Integer, VARCHAR
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from base_kit.base_string import generate_random_str

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(VARCHAR(255))
    age = Column(VARCHAR(3))


engine = create_engine('mysql+pymysql://root:root@localhost:3306/my_py_sql')

DBSession = sessionmaker(bind=engine)
session = DBSession()

# 增加一条记录
name = generate_random_str(5)
age = str(random.randint(20, 50))
new_user = Employee(name=name, age=age)
try:
    session.add(new_user)
except Exception as e:
    print(e)

# 提交即保存到数据库:
session.commit()

# 创建Query查询，filter是where条件，
# 最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(Employee).filter(Employee.id == '30').one()
print(user.name, user.id)

user = session.query(Employee).all()
print(user[0].name, user[0].id)

# 删除一条记录
user = session.query(Employee).filter(Employee.id == '8').delete()

# 修改一条记录
user1 = session.query(Employee).filter(Employee.id == '9').one()
print(user1.name)
user1.name = '张三'
session.commit()

# 关闭session:
session.close()
