#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""ip_chk"""
# @Time    : 2019/11/6 9:11
# @Author  : Wind
# @Des     : 检验指定ip与端口是否能连通
# @Software: PyCharm  Python3.7.2
import socket


# 检验指定ip与端口是否能连通，host兼容IP与url
def check_ip_port(host, port):
    ip = socket.getaddrinfo(host, None)[0][4][0]
    socket.setdefaulttimeout(3)
    if ':' in ip:
        inet = socket.AF_INET6
    else:
        inet = socket.AF_INET
    sock = socket.socket(inet)
    status = sock.connect_ex((host, port))
    sock.close()
    return status == 0


if __name__ == "__main__":
    print(check_ip_port('www.baidu.com', 80))
    # 测试本地记得开http server
    print(check_ip_port('127.0.0.1', 80))