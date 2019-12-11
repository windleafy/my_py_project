#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""ss_chk_simple"""
# @Time    : 2019/11/6 9:11
# @Author  : Wind
# @Des     : 检验指定ip与端口是否能连通
# @Software: PyCharm  Python3.7.2
# ss服务器IP与端口验证
from base_kit.base_ip_chk import check_ip_port
from ss_chk.ss_chk_run import get_server_url


def ping_ip(urls):
    for item in urls:
        host = item[0]
        port = int(item[1])
        # 读取待检测IP列表，进行批量检测
        status = check_ip_port(host, port)
        print(status)
        if status:
            print(host, port)
            yield item


if __name__ == "__main__":
    url_list = list(get_server_url())
    for ss in list(ping_ip(url_list)):
        print(ss)


