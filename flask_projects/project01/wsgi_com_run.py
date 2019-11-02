#!/usr/bin/env python
"""wsgi通用run程序入口"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 16:48
# @Author  : Wind
# @Des     : 
# @Software: PyCharm


from app import app
from flask_script import Manager, Shell
manager = Manager(app)


def make_shell_context():
    return dict(app=app)


manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def deploy():
    pass


if __name__ == "__main__":
    manager.run()
