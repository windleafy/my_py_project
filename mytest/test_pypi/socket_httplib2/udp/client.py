#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Shark
"""
client.py
"""
# @Software: PyCharm
# @Time    : 2019 12 25 10:16

import socket

# 环境初始化
port = 8081
host = '192.168.1.109'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # 输入待发送的消息
    msg = input('说点什么吧：',)
    msg = msg.encode('utf-8')

    # 发送消息
    s.sendto(msg, (host, port))
    print('消息已发送！')
