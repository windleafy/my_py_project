#!/usr/bin/env python
"""secret_key"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 14:59
# @Author  : Wind
# @Des     : 
# @Software: PyCharm
import base64
import os


def generate_secret_key():
    """
    生成密钥
    """
    return base64.b64encode(os.urandom(66))
