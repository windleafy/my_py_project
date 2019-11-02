#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""exception"""


# @Time    : 2019/10/29 12:29
# @Author  : Wind
# @Des     : 
# @Software: PyCharm

class MyException(Exception):
    def __init__(self, length, atleast):
        self.length = length
        self.atleast = atleast


def input_check():
    try:
        s = input('pls input:')
        if len(s) < 3:
            raise MyException(len(s), 3)
    except MyException as e:
        print(f'输入字符数是{e.length}个，不能小于{e.atleast}个。')
        return input_check()
    else:
        print('Bye')


# input_check()

class Test:
    def __init__(self, switch):
        self.switch = switch

    def calc(self, a, b):
        try:
            return a / b
        except ZeroDivisionError as e:
            if self.switch:
                print(f"捕获异常，内容如下：\n{e}")
            else:
                raise



# noinspection PyBroadException
try:
       pass
except Exception as e:
        pass