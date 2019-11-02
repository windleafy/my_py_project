#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""__init__.py"""
# @Time    : 2019/10/25 10:57
# @Author  : Wind
# @Des     : 创建app
# @Software: PyCharm
from flask import Flask
#
from werkzeug.utils import import_string
from myapp_fac.admin import admin_bp_fac


blueprints = [
    'myapp_fac.main:main_bp_fac',
    'myapp_fac.admin:admin_bp_fac',
]


def create_app(config):
    # Instance blueprint
    app = Flask(__name__)
    # Load config
    app.config.from_object(config)

    # Load extensions
    # mail.init_app(app)
    # db.init_app(app)

    # Load blueprints
    for bp_name in blueprints:
        bp = import_string(bp_name)
        app.register_blueprint(bp)
    return app

    # app.register_blueprint(admin_bp_fac)



