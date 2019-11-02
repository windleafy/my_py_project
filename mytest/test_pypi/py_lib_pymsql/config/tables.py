#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""tables"""
# @Time    : 2019/10/30 14:10
# @Author  : Wind
# @Des     : 定义表
# @Software: PyCharm  Python3.7.2

students = ('CREATE TABLE  `students`(\n'
            '  `id` INT NOT NULL AUTO_INCREMENT,\n'
            '  `name` VARCHAR(255),\n'
            '  `age` VARCHAR(2),\n'
            '  PRIMARY KEY (`id`)\n'
            ');\n')

this_is_new_table = ('CREATE TABLE  `this_is_new_table`(\n'
                     '  `id` INT NOT NULL AUTO_INCREMENT,\n'
                     '  `name` VARCHAR(255),\n'
                     '  `age` VARCHAR(3),\n'
                     '  `height` VARCHAR(3),\n'
                     '  `weight` VARCHAR(3),\n'
                     '  `gender` VARCHAR(1),\n'
                     '  PRIMARY KEY (`id`)\n'
                     ');\n')
