#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""run_batch"""
# @Time    : 2019/10/25 17:51
# @Author  : Wind
# @Des     : 
# @Software: PyCharm
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from myapp_fac import create_app
from config import release, debug

release_app = create_app(release)
debug_app = create_app(debug)

app = DispatcherMiddleware(release_app, {'/test': debug_app})

run_simple('0.0.0.0', 5000, app, use_reloader=True, use_debugger=True)
