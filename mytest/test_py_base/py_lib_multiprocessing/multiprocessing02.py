#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/3 11:04
# @Author  : Wind
# @Des     : 创建多个进程并发处理与顺序执行处理同一数据，比较处理时间。
# @Site    : 
# @File    : multiprocessing02.py
# @Software: PyCharm
import multiprocessing
from multiprocessing.dummy import Pool
import time


def run(fn):
    """
    :param fn:测试队列中的元素
    :return:
    """
    # fn: 函数参数是数据列表的一个元素
    time.sleep(1)
    return fn * fn


if __name__ == "__main__":
    testFL = [1, 2, 3, 4, 5, 6]
    print('shun_xu:')  # 顺序执行(也就是串行执行，单进程)
    s = time.time()
    for i in testFL:
        print(run(i), '  ', end='')

    e1 = time.time()
    print("\n顺序执行时间：", int(e1 - s), '秒')
    print('-' * 30)

    print('concurrent:')  # 创建多个进程，并行执行
    pool = Pool(5)  # 创建拥有5个进程数量的进程池
    # testFL:要处理的数据列表，run：处理testFL列表中数据的函数
    rl = pool.map(run, testFL)
    pool.close()  # 关闭进程池，不再接受新的进程
    pool.join()  # 主进程阻塞等待子进程的退出

    # 各进程的返回结果，会形成一个队列
    print(rl)
    e2 = time.time()
    print("并行执行时间：", int(e2 - e1), '秒')
