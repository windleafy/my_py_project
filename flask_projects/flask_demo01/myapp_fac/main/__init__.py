#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""__init__.py"""
# @Time    : 2019/10/25 10:57
# @Author  : Wind
# @Des     : 创建admin蓝图对象
# @Software: PyCharm
from flask import Blueprint

main_bp_fac = Blueprint('main', __name__, url_prefix='/')

from myapp_fac.main import views
