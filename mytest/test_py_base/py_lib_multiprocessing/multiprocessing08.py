#!/usr/bin/env python
"""multiprocessing08"""

# -*- coding: utf-8 -*-
# @Time    : 2019/10/5 16:47
# @Author  : Wind
# @Des     : 进程间通信
# @Software: PyCharm

from multiprocessing import Pool
import multiprocessing
import random
import time


# 写数据进程执行的代码:
def write(q, lock):
    lock.acquire()  # 加上锁
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
    lock.release()  # 释放锁


# 读数据进程执行的代码:
def read(q):
    while True:
        if not q.empty():
            value = q.get(False)
            print('Get %s from queue.' % value)
            time.sleep(random.random())
        else:
            break


if __name__ == '__main__':
    manager = multiprocessing.Manager()
    # 父进程创建Queue，并传给各个子进程：
    q = manager.Queue()
    lock = manager.Lock()  # 初始化一把锁
    p = Pool()
    pw = p.apply_async(write, args=(q, lock))
    pr = p.apply_async(read, args=(q,))
    p.close()
    p.join()

    print('所有数据都写入并且读完')




