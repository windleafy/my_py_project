#!/usr/bin/env python
"""debug_test"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/3 17:06
# @Author  : Wind
# @Des     : 
# @Software: PyCharm


def sum_demo(x, y):
    """

    :param x:
    :param y:
    :return:
    """
    for _ in range(10):
        x += 1
        y += 1
        r = x + y
    return r


if __name__ == '__main__':
    print()
    result = sum_demo(1, 1)
    print()
    print(result)

