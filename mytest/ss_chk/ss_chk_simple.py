#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""ss_chk_simple"""
# @Time    : 2019/11/6 9:11
# @Author  : Wind
# @Des     : 检验指定ip与端口是否能连通
# @Software: PyCharm  Python3.7.2
import socket

socket.setdefaulttimeout(3)


def check_ip_port(host, port):
    if ':' in host:
        inet = socket.AF_INET6
    else:
        inet = socket.AF_INET
    sock = socket.socket(inet)
    status = sock.connect_ex((host, port))
    sock.close()
    return status == 0


h = '204.45.182.34'
p = 8097

print(check_ip_port(h, p))
