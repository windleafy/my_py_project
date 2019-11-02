#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""decorator02"""


# @Time    : 2019/10/24 9:42
# @Author  : Wind
# @Des     :
# @Software: PyCharm
# 类静态方法和类方法
class A(object):
    var1 = 1
    var2 = 2
    def func(self):
        print(self.var1)
        return

    @staticmethod
    def static_func():
        print(A.var1)
        return

    @classmethod
    def class_func(cls):
        print(cls.var2)
        cls().func()
        return


a = A
a.static_func()
print('='*10)
a.class_func()
