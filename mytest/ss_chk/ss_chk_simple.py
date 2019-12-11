#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""ss_chk_simple"""
# @Time    : 2019/11/6 9:11
# @Author  : Wind
# @Des     : 检验指定ip与端口是否能连通
# @Software: PyCharm  Python3.7.2
# ss服务器IP与端口验证
from base_kit.base_ip_chk import check_ip_port


# 取ss-free服务器列表
def get_server_url():
    with open('url_list.txt', encoding='utf8') as f:
        s_content = f.read()
    content_list = s_content.split('\n')
    for i in content_list:
        yield i.split()[1:5]


# 检测出可以ping通的ip
def ping_ip():
    urls = list(get_server_url())
    print(urls)
    num = len(urls)
    count = 1
    for item in urls:
        print(f'No.{count}, left:{num-count}')
        count += 1
        host = item[0]
        port = int(item[1])
        # 读取待检测IP列表，进行批量检测
        status = check_ip_port(host, port)
        print(status)
        if status:
            print(host, port)
            yield item
        print('\n')


if __name__ == "__main__":
    tmp = list(ping_ip())
