#!/usr/bin/env python
"""multiprocessing.03"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/4 15:10
# @Author  : Wind
# @Des     : apply_async()、get()方法的实例
# @Software: PyCharm
import time
from multiprocessing.dummy import Pool


def run(fn):
    """
    :param fn:测试队列中的元素
    :return:
    """
    # fn: 函数参数是数据列表的一个元素
    time.sleep(1)
    return fn * fn


if __name__ == "__main__":

    # 数据初始化
    testFL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 初始化待处理参数列表
    e1 = time.time()  # 初始化开始时间
    rl = []  # 初始化结果列表

    pool = Pool(5)  # 创建拥有5个进程数量的进程池
    for i in range(len(testFL)):
        '''
        for循环执行流程：
        （1）添加子进程到pool，并将这个对象（子进程）添加到result这个列表中。
            （此时子进程并没有运行）
        （2）执行子进程（同时执行5个）
        '''
        r = pool.apply_async(run, args=(testFL[i],))  # 返回的是子进程对象，需用.get()获取返回值
        rl.append(r)
    print('Waiting for all sub_processes done...')
    pool.close()  # 关闭进程池，不再接受新的进程
    pool.join()  # 主进程阻塞等待子进程的退出

    '''
    遍历结果列表，取出子进程对象，访问get()方法，获取返回值。
    get()方法只能等子进程运行完毕后才能调用成功，
    否则会一直阻塞等待。如果写在for循环内容，相当于变成了同步，执行效率将会非常低。
    '''
    for i in rl:
        print(i.get(), '  ', end='')
    e2 = time.time()
    print("\n并行执行时间：", int(e2 - e1), '秒')
