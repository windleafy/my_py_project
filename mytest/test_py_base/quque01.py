#!/usr/bin/env python
"""quque01"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/4 17:47
# @Author  : Wind
# @Des     : 
# @Software: PyCharm

# 先进先出(FIFO)
from queue import Queue

q = Queue()

for i in range(3):
    q.put(i)

while not q.empty():
    print(q.get())
