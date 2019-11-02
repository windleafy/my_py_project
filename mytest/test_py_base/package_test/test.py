#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""test"""
# @Time    : 2019/10/29 15:51
# @Author  : Wind
# @Des     : 
# @Software: PyCharm

# 引入inner1.py中的一个函数
from test_py_base.package_test.packages.inner1 import inner1_1fun

# 引入inner2.py整个模块
# from test_py_base.package_test.packages import inner2
from test_py_base.package_test.packages.inner2 import inner2_1fun, inner2_2fun



inner1_1fun()
inner2_1fun()
inner2_2fun()

