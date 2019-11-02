#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""log"""
# @Time    : 2019/10/23 10:19
# @Author  : Wind
# @Des     : 
# @Software: PyCharm

import logging.handlers

'''日志文件输出_示例1'''
LOG_FILE = 'outfile/log/tst.log'

handler1 = logging.handlers.RotatingFileHandler(
    LOG_FILE, maxBytes=1024 * 1024, backupCount=5)  # 实例化handler
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
formatter = logging.Formatter(fmt)  # 实例化formatter
handler1.setFormatter(formatter)  # 为handler添加formatter

logger1 = logging.getLogger('tst')  # 获取名为tst的logger
logger1.addHandler(handler1)  # 为logger添加handler
logger1.setLevel(logging.DEBUG)  # 设置日志级别

logger1.info('first info message')

'''日志文件输出_示例2'''
handler2 = logging.FileHandler('outfile/log/tst2.log',
                               encoding='utf-8')  # 实例化日志handler，目录需要先建好
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'  # 定义日志格式
formatter = logging.Formatter(fmt, datefmt='%Y-%m-%d,%H:%M:%S')  # 实例化formatter
handler2.setFormatter(formatter)  # 为handler添加formatter

logger2 = logging.getLogger('tst2')  # 实例化logger，命名为tst2
logger2.addHandler(handler2)  # 给logger添加handler
logger2.setLevel(logging.DEBUG)  # 设置日志级别

logger2.info('提示')
logger2.warning('警告')

'''控制台输出'''
logger3 = logging.getLogger('tst3')
logger3.setLevel(logging.DEBUG)  # 设置日志级别
logger3.warning('this is warning')
