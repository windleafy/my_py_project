#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""run"""
# @Time    : 2019/10/25 11:03
# @Author  : Wind
# @Des     : 启动app
# @Software: PyCharm
from myapp_fac import create_app
from config import debug, release

# app.run(host='0.0.0.0')

app1 = create_app(release)
app1.run(host='0.0.0.0')
