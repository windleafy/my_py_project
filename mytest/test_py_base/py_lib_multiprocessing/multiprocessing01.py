#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/3 11:14
# @Author  : Wind
# @Des     : 多进程未使用进程池，未加阻塞。
# @Site    : 
# @File    : multiprocessing01.py
# @Software: PyCharm
import multiprocessing
import time
import random
import os


def do(n):
    """
    :param n: 第n个进程
    :return:
    """
    # 获取当前线程的名字
    name = multiprocessing.current_process().name
    pid = os.getpid()
    print(name, 'starting', 'pid', pid)
    print("worker ", n[1], '\n')
    time.sleep(float(random.randint(1, 500)) / 100)
    print(f"Process {name} end.")
    end_time = time.time()
    print(f'used time :{end_time - n[0]}\n')
    return


if __name__ == '__main__':
    numList = []
    start_time = time.time()
    for i in range(5):
        my_list = [start_time, i]
        p = multiprocessing.Process(target=do, args=(my_list,))
        numList.append(p)
        p.start()
    print('我比上面的内容先执行哟！！！')
