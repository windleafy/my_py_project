#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 14:22
# @Author  : Wind
# @Site    : 
# @File    : get_pic_list.py
# @Software: PyCharm

import os


def get_pic_list(path):
    # path = "G:\\Data\\python\\my_download\\outfile\\list"
    # path = "G:\\Data\\python\\my_download\\Male\\outfile"
    # 遍历目录下所有文件
    g = os.walk(path)
    for path, dir_list, file_list in g:
        for file_name in file_list:
            yield (path + "\\" + file_name)

    '''
    for i in range(1000):
        print(pic_list[i])
        print(pic_list[i].split('/')[6])
    '''


# print(get_pic_list())
def dir_rename():
    path1 = "G:\\Data\\python\\meizitu\\pic\\"
    # print(os.listdir(path))
    j = 1
    for i in os.listdir(path1):
        old_dir_name = path1+i
        new_dir_name = path1 + f"girl2_{j}"
        print(new_dir_name)
        j += 1
        os.rename(old_dir_name, new_dir_name)
        

'''
path2 = "G:\\Data\\python\\meizitu\\pic\\"
pic_list = get_pic_list(path2)
print(pic_list[0])
print(pic_list[1])
print(pic_list[2])

print(pic_list[0].split('\\')[5])
print(pic_list[1].split('\\')[5])
print(pic_list[2].split('\\')[5])

print(pic_list[0].split('\\')[-1].split('.')[0])
print(pic_list[1].split('\\')[-1].split('.')[0])
print(pic_list[2].split('\\')[-1].split('.')[0])
'''

