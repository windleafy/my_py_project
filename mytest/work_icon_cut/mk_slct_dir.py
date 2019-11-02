#!/usr/bin/env python
"""mk_slct_dir"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11 20:27
# @Author  : Wind
# @Des     : 创建select
# @Software: PyCharm

import os
import shutil

# path1 = "G:\\Data\\python\\my_download\\outfiles\\py_cut_icon\\small\\"
# path2 = "G:\\Data\\python\\my_download\\outfiles\\py_cut_icon\\big\\"
# path3 = "G:\\Data\\python\\my_download\\outfiles\\py_cut_icon\\big\\"
path1 = "G:\\Data\\python\\my_download\\outfiles\\py_cut_icon\\big191011\\"

small_big = os.listdir(path1)
# print(small_big)

'''向select目录移动文件_版本1'''
for i in small_big:
    if i.split('_')[0] == 'girl2':
        # print(path1+i)
        tmp = os.listdir(path1 + i)

        for j in tmp:
            if j.split('.')[-1] == 'jpg':
                old_name = path1 + i + '\\' + j
                new_name = path1 + i + '\\' + 'select' + '\\' + j
                print(old_name)
                print(new_name)
                shutil.copyfile(old_name, new_name)

'''
"""创建select目录模块"""
for i in range(0, len(small_big)):
    print(small_big[i])
    # print(small[1])
    select = path1 + small_big[i] + '\\' + 'select'
    # print(select)

    if os.path.isdir(select):
        print('目录已存在\n')
    else:
        os.mkdir(select)
        print('目录创建成功\n')
'''

'''
"""向select目录移动文件_版本2"""
id_dir = os.listdir(path1)
# print(id_dir[0])

for i in range(3, len(id_dir)):
    print(f'第{i}条处理开始')
    id_item = os.listdir(path1 + id_dir[i])
    print(id_dir[i])
    # print(id_item)

    for item in id_item:
        if (item.split('.')[-1] =='jpg'):
            old_name = path1 + id_dir[i] + '\\' + item
            new_name = path1 + id_dir[i] + '\\' + 'select\\' + item
            # print(old_name, '---', new_name)
            shutil.copyfile(old_name, new_name)
    print(f'第{i}条处理完毕\n')
'''