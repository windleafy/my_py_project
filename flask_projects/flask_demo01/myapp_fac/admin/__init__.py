#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""__init__.py"""
# @Time    : 2019/10/25 10:57
# @Author  : Wind
# @Des     : 创建admin蓝图对象
# @Software: PyCharm
from flask import Blueprint

admin_bp_fac = Blueprint('admin', __name__, url_prefix='/admin_fac')

from myapp_fac.admin import views
