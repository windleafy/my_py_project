#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Shark
"""
server.py
"""
# @Software: PyCharm
# @Time    : 2019 12 25 10:16

import datetime
import socket

# 环境初始化
port = 8081
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', port))
print('等待客端的消息！')

while True:
    # 接收消息，3000是缓冲区长度
    data, addr = s.recvfrom(3000)

    # 当前时间
    rec_time = datetime.datetime.now().strftime('%T')

    # 消息解码
    data = data.decode('utf-8')

    # 打印消息
    print(rec_time, 'Received: ', data, ' from ', addr)
