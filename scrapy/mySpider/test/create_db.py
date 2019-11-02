# encoding:utf8
# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""create_db"""
# @Time    : 2019/10/27 20:29
# @Author  : Wind
# @Des     : 
# @Software: PyCharm
import pymysql


# 创建数据库连接
conn = pymysql.connect(
    host='localhost', user='root', password='root', charset='utf8mb4')
print('数据库连接完成')

# 创建游标
cursor = conn.cursor()
print('游标创建完成')

# 创建数据库
db_name = 'images360'
sql = f"CREATE DATABASE IF NOT EXISTS {db_name} DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci"
cursor.execute(sql)
print('数据库my_py_sql创建完成')

# 打开指定数据库
cursor.execute(f"use {db_name}")
print('打开数据库my_py_sql完成')

# 创建表
sql_2 = '''CREATE TABLE  IF NOT EXISTS `images` (
  `id` VARCHAR(255) NULL PRIMARY KEY, 
  `url` VARCHAR(255) NULL , 
  `title` VARCHAR(255) NULL , 
  `thumb` VARCHAR(255) NULL
)
'''
cursor.execute(sql_2)
print('数据表employee创建完成')

# 关闭数据库
cursor.close()
print('关闭游标完成')

# 关闭数据库连接
conn.close()
print('关闭连接完成')
