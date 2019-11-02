#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""lang_module"""
# @Time    : 2019/10/22 11:24
# @Author  : Wind
# @Des     : 蓝图应用在多语言项目的实例
# @Software: PyCharm
from flask import Blueprint, g, url_for

lang_bp = Blueprint('lang', __name__, url_prefix='/<lang_code>')


@lang_bp.route('/')
def index():
    return f'<h1>Index of language {g.lang_code}</h1>'


@lang_bp.route('/path')
def path():
    return f'<h1>Language base URL is {url_for(".index")}</h1>'

# 视图函数被调用之前，URL路径被预处理时执行，获取url参数
@lang_bp.url_value_preprocessor
def get_lang_code_from_url(endpoint, view_args):
    g.lang_code = view_args.pop('lang_code')

# 对当前蓝图内的所有视图有效，设置url规则上参数的默认值，
# 只需将参数名及其默认值保存在函数的第二个参数values里即可。
@lang_bp.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', g.lang_code)

