#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""mysql_conn"""
# @Time    : 2019/10/29 21:45
# @Author  : Wind
# @Des     : 数据库连接类
# @Software: PyCharm Python 3.7.2
from test_pypi.py_lib_pymsql.config import mysql_cfg
from base_kit.base_mysql import MysqlPython
from test_pypi.py_lib_pymsql.config.tables import this_is_new_table

# Mysql对象实例化
tmp = MysqlPython(
    host=mysql_cfg.host,
    port=mysql_cfg.port,
    user=mysql_cfg.user,
    pwd=mysql_cfg.pwd,
)

# 连接Mysql服务器
tmp.get_conn_info()

# 打开已有数据库
db_name = 'my_py_sql'
tmp.open_db(db_name)


# 创建新库
# db_name = 'this_is_new_db'
# tmp.create_db(db_name)

# 创建新表
# db_name = 'this_is_new_db'
# table_name = this_is_new_table
# tmp.create_table(db_name, table_name)

# 插入数据(增)
# name = "蜘蛛人"
# age = "20"
# sql = "insert into employee (name, age) values ('%s','%s')" % (name, age)
# tmp.exec_non_query(sql)

# 修改数据(改)
# name = '王小二'
# sql = "UPDATE employee SET name='%s' WHERE name='sdfsdfs';" % name
# tmp.exec_non_query(sql)

# 删除数据(删)
# sql = "DELETE FROM employee WHERE name='hello';"
# tmp.exec_non_query(sql)

# 数据查寻(查)
# sql = 'select * from employee;'
# result = tmp.exec_query(sql)
# for i in result:
#     print(i)

# 关闭表和库
tmp.close()
