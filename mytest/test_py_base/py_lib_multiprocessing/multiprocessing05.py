#!/usr/bin/env python
"""multiprocessing05"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/3 14:46
# @Author  : Wind
# @Des     : 与multiprocessing04比较的文件，文件读取数量在3000左右时，时间差0.1秒
# @Software: PyCharm

from test_py_base.py_lib_multiprocessing.multiprocessing04 import *


if __name__ == "__main__":
    path = r'G:\PycharmProjects\mytest\res\files'
    print('顺序执行测试开始')
    start_time = time.time()
    files_init = get_file(path)
    result_list = []
    for i in files_init:
        result_list.append(open_file(i))

    writeFilePath = r"G:\PycharmProjects\mytest\outfile\res.txt"
    out(result_list, writeFilePath)
    end_time = time.time()
    print('顺序执行测试结束')
    print('used time is ', end_time - start_time)
