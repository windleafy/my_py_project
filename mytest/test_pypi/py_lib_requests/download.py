#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/2 15:09
# @Author  : Wind
# @Des     : 下载大文件测试
# @File    : download.py
# @Software: PyCharm
from base_kit.base_requests import *


url = 'http://ftp-idc.pconline.com.cn/ceff57a41e12f1cd0a46706630efa2c5/pub/download' \
      '/201010/HD.Club-4K-Chimei-inn-20mbps.rar'
save_name = './outfile/my_download.rar'

status = 'net_error1'
while status == 'net_error1' or status == 'net_error2':
    status = download(url, save_name)

