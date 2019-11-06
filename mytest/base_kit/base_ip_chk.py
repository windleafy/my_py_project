#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""ip_chk"""
# @Time    : 2019/11/6 9:11
# @Author  : Wind
# @Des     : 检验指定ip与端口是否能连通
# @Software: PyCharm  Python3.7.2
import socket


def check_ip_port(host, port):
    socket.setdefaulttimeout(3)
    if ':' in host:
        inet = socket.AF_INET6
    else:
        inet = socket.AF_INET
    sock = socket.socket(inet)
    status = sock.connect_ex((host, port))
    sock.close()
    return status == 0
