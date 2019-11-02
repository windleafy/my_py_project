#!/usr/bin/env python
"""根据ID批量重命名图标"""
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 9:35
# @Author  : Wind
# @Des     : 
# @File    : slct_dir_chk.py
# @Software: PyCharm

import os
import time

from base_kit.base_file import *
import shutil
# 待移动目录 G:\Data\python\my_download\outfiles\py_cut_icon
small_path = 'G:\\Data\\python\\my_download\\outfiles\\py_cut_icon\\small191022\\'
big_path = 'G:\\Data\\python\\my_download\\outfiles\\py_cut_icon\\big191022\\'


# 创建slct icon数量统计文件
def init_chk():
    path = big_path
    name = 'big.csv'
    chk(path, name)

    path = small_path
    name = 'small.csv'
    chk(path, name)


def chk(path, name):
    dir_icon = os.listdir(path)
    icon_item_list = ['id,num']
    for i in range(0, len(dir_icon)):
        tmp = path + dir_icon[i] + '\\'
        # 取出icon_id
        icon_item = dir_icon[i] + ','
        for j in os.listdir(tmp):
            if j == 'select':
                # G:\Data\python\my_download\outfiles\py_cut_icon\small\10836\select
                # 取出slct数量
                slct_num = len(os.listdir(tmp + j))
                for k in os.listdir(tmp + j):
                    if k == 'Thumbs.db':
                        slct_num -= 1
                icon_item += str(slct_num)
        icon_item_list.append(icon_item)

    save_path = './outfile/'

    str_list2csv(icon_item_list, save_path, name)


# 生成大小图标数量对照表result.csv
def b_s_result():
    # @ file_path_small, 输入值
    # @ file_path_big， 输入值
    file_path_small = './outfile/small.csv'
    # small = read_txt(file_path_small)
    header, small = csv2list(file_path_small)
    # print(small)

    file_path_big = './outfile/big.csv'
    # big = read_txt(file_path_big)
    header, big = csv2list(file_path_big)
    # print(big)

    # print(small)
    # print(big)

    result = []

    for i in small:
        s_id = i[0]
        s_num = i[1]
        for j in big:
            # print(j)
            b_id = j[0]
            b_num = j[1]
            if b_id == s_id:
                if int(s_num) >= int(b_num):
                    num = int(b_num)
                else:
                    num = int(s_num)

                # print(f'small:{s_id}-{s_num}---big:{b_id}-{b_num}-----num:{num}')
                result_item = [s_id, s_num, b_id, b_num, num]
                result.append(result_item)

    # print(result)

    class MyData:
        pass

    my_data = MyData
    my_data.header = ['s_id', 's_num', 'b_id', 'b_num', 'num']
    my_data.save_name = './outfile/result.csv'
    my_data.rows = result

    list2csv(my_data)


# 初始化robot_id的创建环境。根据大小图标对应关系，复制图标并以最终ID命名
def robot_id_create():
    # start_id = 10086
    start_id = 13104
    out_path = './outfile/new_icon/'
    b_s_relation_file = './outfile/result.csv'
    # 取出大小图标对应关系表b_s_relation
    header, b_s_relation = csv2list(b_s_relation_file)
    # print(b_s_relation)

    # 创建小图标保存目录
    mk_dir_small = out_path + "icon_small/"
    dir_chk_create(mk_dir_small)

    # 创建大图标保存目录
    mk_dir_big = out_path + "icon_big/"
    dir_chk_create(mk_dir_big)

    # 处理小图标
    old_small_path = small_path
    old_path = old_small_path
    mk_dir = mk_dir_small
    save_data = file_copy(b_s_relation, old_path, start_id, mk_dir)  # 此处是生成器，并未执行

    save_path = './outfile/'
    save_name = 'slct_files.csv'
    str_list2csv(save_data, save_path, save_name)  # save_data生成器在此执行
    print('小图标复制工作处理完毕！\n')

    # 处理大图标
    old_big_path = big_path
    old_path = old_big_path
    mk_dir = mk_dir_big
    save_data = file_copy(b_s_relation, old_path, start_id, mk_dir)  # 此处是生成器，并未执行

    for _ in save_data:  # save_data生成器在此执行
        pass
    print('大图标复制工作处理完毕！\n')


def file_copy(b_s_relation, old_path, start_id, mk_dir):
    # @ 四个输入值，robot_id()内部调用时获取
    # @ b_s_relation，从result.csv表中取值
    for i in range(0, len(b_s_relation)):
        num = int(b_s_relation[i][4])
        old_name_path = old_path + b_s_relation[i][0] + '\\select\\'
        slct_file = os.listdir(old_name_path)
        if 'Thumbs.db' in slct_file:
            slct_file.remove('Thumbs.db')

        for j in range(0, num):
            new_name = mk_dir + str(start_id) + '.jpg'
            old_name = old_name_path + slct_file[j]

            # 复制文件
            shutil.copyfile(old_name, new_name)
            start_id += 1
            # print(old_name, new_name)

            # 取出old_name做性别识别
            save_data = old_name_path + ',' + str(start_id)
            yield save_data  # 此处返回                         是列表中的一个元素，可用生成器的写法。不再用list[] list.append  return的三段写法


start_time = time.time()
# start_id 在robot_id_create中设置

# 创建大小图标选中数量统计文件
'''
@ big.txt 输出文件
@ small.txt 输出文件
'''
init_chk()
''''''

# 生成大小图标数量对照表
'''
@ result.csv 输出文件
'''
b_s_result()
''''''

# 生成机器人ID对应的目录，按机器人ID命名大小图标
'''
# @ ./outfile/new_icon/icon_small/10086.jpg
# @ ./outfile/new_icon/icon_big/10086.jpg
'''
robot_id_create()
''''''

end_time = time.time()

print(f'used time :{int(end_time - start_time)} seconds.')
