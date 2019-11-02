#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""add_log"""

# @Time    : 2019/10/23 9:53
# @Author  : Wind
# @Des     :
# @Software: PyCharm
from flask import Flask
import logging.handlers
from logging.handlers import TimedRotatingFileHandler, RotatingFileHandler

app = Flask(__name__)


def ini_log():
    # 初始化handler
    handler = TimedRotatingFileHandler('log/flask.log',
                                       when='D', encoding='utf-8')
    fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
    formatter = logging.Formatter(fmt,
                                  datefmt='%Y-%m-%d,%H:%M:%S')
    handler.setFormatter(formatter)

    # logger实例绑定handler
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)

    return app.logger


app.logger = ini_log()


@app.route('/')
def root():
    app.logger.info('info log')
    app.logger.warning('warning log')
    return 'welcome'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
