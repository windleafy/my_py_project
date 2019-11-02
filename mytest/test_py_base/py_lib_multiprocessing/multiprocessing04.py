#!/usr/bin/env python
"""multiprocessing04"""
# -*- coding: utf-8 -*-
# @Time    : 2019/10/3 13:10
# @Author  : Wind
# @Des     : 多进程检查，指定目录下所有txt文件，提取每个文件的行数与字数并保存。
# @Software: PyCharm
import os
from multiprocessing.dummy import Pool
import time


# 文件保存输出
def out(list1, write_file_path):
    """
    :param list1:需要输出的内容列表
    :param write_file_path: 输出的文件路径
    """
    # 将统计结果写入结果文件中
    file_lines = 0
    char_num = 0
    with open(write_file_path, 'a', encoding='utf-8') as fp:
        for i in list1:
            fp.write(i[2] + " 行数：" + str(i[0]) + " 字符数：" + str(i[1]) + "\n")
            file_lines += i[0]
            char_num += i[1]


# 获取指定目录下的所有txt文件的带目录文件名。
def get_file(chk_path):
    """
    :chk_path:待检测的目录
    :return:
    """
    # 获取目录下的文件list
    file_list = []
    for root, dirs, files in list(os.walk(chk_path)):
        for i in files:
            if i.endswith('.txt'):
                file_list.append(root + "\\" + i)
    return file_list


# 获取指定文件的行数，字符数，文件路径
def open_file(file_path):
    """
    :param file_path:需要处理的文件，所在路径
    :return:文件行数，文件字符数，文件路径
    """
    # 统计每个文件中行数和字符数，并返回
    with open(file_path) as fp:
        content = fp.readlines()
        lines = len(content)
        alpha_num = 0
        for i in content:
            alpha_num += len(i.strip('\n'))
    return lines, alpha_num, file_path


if __name__ == "__main__":

    # 数据初始化
    startTime = time.time()
    path = r'G:\PycharmProjects\mytest\res\files'
    files_init = get_file(path)
    print('数据初始化完毕！')

    # 多进程并发处理
    print('并发处理开始！')
    pool = Pool(5)  # 创建拥有5个进程数量的进程池
    r = pool.map(open_file, files_init)  # 各个进程的处理结果，会形成一个队列
    pool.close()  # 关闭进程池，不再接受新的进程
    pool.join()  # 主进程阻塞等待子进程的退出
    print('并发处理结束！')

    # 结果数据输出
    writeFilePath = r"G:\PycharmProjects\mytest\outfile\res.txt"
    out(r, writeFilePath)
    print('数据保存结束！')
    endTime = time.time()
    print("used time is ", endTime - startTime)


