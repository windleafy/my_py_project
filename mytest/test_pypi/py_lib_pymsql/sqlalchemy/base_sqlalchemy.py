#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""base_sqlalchemy"""
# @Time    : 2019/10/31 21:26
# @Author  : Wind
# @Des     :
# @Software: PyCharm  Python3.7.2
from base_kit.base_sqlalchemy import MySqlAlchemy
from test_pypi.py_lib_pymsql.sqlalchemy.config import *


if __name__ == '__main__':
    db_test_obj = MySqlAlchemy(
        host='localhost',
        port='3306',
        user='root',
        pwd='root',
        db_name='new_db',
    )

    # db_test_obj.crt_db()       # 创建数据库
    # db_test_obj.drop_db()      # 删除数据库
    # db_test_obj.crt_tb(Client)    # 创建数据表
    # db_test_obj.drop_tb(Stu)  # 删除数据表

    # 数据表增、删、改、查
    '''
    session = db_test_obj.crt_session(User)
    if session:

        # 插入一条数据
        new_stu = User(name='小五', password='123')
        try:
            session.add(new_user)
        except Exception as e:
            print(e)
        else:
            print('数据插入成功！')

        # 查寻&修改一条数据
        try:
            user = session.query(User).filter(User.id == '1').one()
        except Exception as e:
            err = e
            print('没查寻到')
        else:
            user.name = '愉快'

        # 查寻&删除一条数据
        try:
            user = session.query(User).filter(User.id == '1').delete()
        except Exception as e:
            err = e
            print('没查寻到')

        # 提交数据
        session.commit()

        # 关闭数据库
        try:
            session.close()
        except Exception as e:
            err = e
        else:
            print('数据库已关闭！')
        '''