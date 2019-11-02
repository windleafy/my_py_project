#!/usr/bin/env python
"""multiprocessing07"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/4 19:35
# @Author  : Wind
# @Des     : windows环境下from multiprocessing import Pool 测试失败；linux环境下工作正常
# @Software: PyCharm

import os
import random
import time
from multiprocessing.dummy import Pool


def long_time_task(name):
    """
    :param name:
    """
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
