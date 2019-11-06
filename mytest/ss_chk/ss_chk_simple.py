#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""ss_chk_simple"""
# @Time    : 2019/11/6 9:11
# @Author  : Wind
# @Des     : 检验指定ip与端口是否能连通
# @Software: PyCharm  Python3.7.2
# ss服务器IP与端口验证
from base_kit.base_ip_chk import check_ip_port
h = '204.45.182.34'
p = 8097
print(check_ip_port(h, p))
