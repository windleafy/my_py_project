#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pymysql01"""
# @Time    : 2019/10/27 18:07
# @Author  : Wind
# @Des     : 创建数据库、创建表
# @Software: PyCharm
import pymysql

# 创建数据库连接
conn = pymysql.connect(
    host='localhost', user='root', password='root')
print('数据库连接完成')

# 创建游标
cursor = conn.cursor()
print('游标创建完成')


# 创建数据库
db_name = 'my_py_sql'
sql = f"CREATE DATABASE {db_name};"
try:
    cursor.execute(sql)
except Exception as e:
    print(e)
else:
    print('数据库my_py_sql创建完成')

# 打开指定数据库
cursor.execute(f"use {db_name}")
print('打开数据库my_py_sql完成')

# 创建表
sql_2 = '''CREATE TABLE  `employee`(
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255),
  `age` VARCHAR(2),
  PRIMARY KEY (`id`)
);
'''

try:
    cursor.execute(sql_2)
except Exception as e:
    print(e)
else:
    print('数据表employee创建完成')

# 关闭数据库
cursor.close()
print('关闭游标完成')

# 关闭数据库连接
conn.close()
print('关闭连接完成')
