#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""tmp"""
# @Time    : 2019/10/30 11:05
# @Author  : Wind
# @Des     : 
# @Software: PyCharm  Python3.7.2

target_table = '''CREATE TABLE  `students`(
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255),
  `age` VARCHAR(2),
  PRIMARY KEY (`id`)
);
'''
print(target_table)
print(target_table.split('`')[1])

