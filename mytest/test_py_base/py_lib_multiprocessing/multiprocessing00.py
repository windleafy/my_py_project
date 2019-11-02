#!/usr/bin/env python
"""multiprocessing00"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/3 16:04
# @Author  : Wind
# @Des     : 进程的开启与阻塞
# @Software: PyCharm

import multiprocessing


def do(n):
    """
   :param n: 第n个进程
   :return:
   """
    # 获取当前线程的名字
    name = multiprocessing.current_process().name
    print(name, 'starting')
    print("worker ", n)
    return


if __name__ == '__main__':
    numList = []
    for i in range(5):
        p = multiprocessing.Process(target=do, args=(i,))
        numList.append(p)
        p.start()
        p.join()
        print("Process end.", '\n')




