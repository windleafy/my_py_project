#!/usr/bin/env python
"""multiprocessing06"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/4 16:41
# @Author  : Wind
# @Des     : Queue+守护进程+for循环的添加子进程耗时测试
# @Software: PyCharm

import time
from queue import Queue
from multiprocessing.dummy import Pool


def test(p):
    """
    :param p:
    :return:
    """
    time.sleep(0.0001)

    if p == 10:
        return True
    else:
        return False


if __name__ == "__main__":

    # 数据初始化
    # start_time = time.time()
    pool = Pool(10)
    q = Queue()

    start_time = time.time()
    for i in range(200000):
        '''将子进程对象存入队列中。'''
        q.put(pool.apply_async(test, args=(i,)))  # 维持执行的进程总数为10，当一个进程执行完后添加新进程.

    end_time = time.time()
    print(f'used time: {end_time-start_time}')

    '''
    父进程设置为守护状态，获取返回值并校验。
    '''
    while 1:
        if q.get().get():
            pool.terminate()  # 结束进程池中的所有子进程。
            break

    pool.close()
    pool.join()


