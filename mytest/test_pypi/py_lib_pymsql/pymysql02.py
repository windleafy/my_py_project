#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pymysql02"""
# @Time    : 2019/10/28 16:38
# @Author  : Wind
# @Des     : 增、删、改、查
# @Software: PyCharm
import pymysql

db_name = 'my_py_sql'
# 创建数据库连接
conn = pymysql.connect(
    host='localhost', user='root', password='root', db=db_name)
print('数据库连接完成')

# 创建游标
cursor = conn.cursor()
print('游标创建完成')

# 插入数据
name = "hello"
age = "27"
sql = "insert into employee (name,age) values ('%s', '%s')" % (name, age)
# param = (name, age)
cursor.execute(sql)
print('数据插入完成')

conn.commit()
print('提交数据')

# 读取数据
sql = 'select * from employee;'
cursor.execute(sql)
result = cursor.fetchall()
print(result)

# 关闭数据库
cursor.close()
print('关闭游标完成')

# 关闭数据库连接
conn.close()
print('关闭连接完成')
