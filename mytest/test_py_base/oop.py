#!/usr/bin/env python
"""oop"""

# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 16:38
# @Author  : Wind
# @Des     : 
# @Software: PyCharm
from types import MethodType


class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'  # 动态给实例绑定一个属性
print(s.name)


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


# 给实例动态加方法，只能本实例使用
s.set_age = MethodType(set_age, s)
s.set_age(25)  # 调用实例方法
print(s.age)  # 测试结果


def set_score(self, score):
    self.score = score


# 给类动态加方法，对所有实例都有效
# PyCharm有警告
Student.set_score = set_score
s.set_score(100)
print(s.score)

s2 = Student()
s2.set_score(101)
print(s2.score)

