#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/27 9:02
# @Author  : Wind
# @Site    : 大图标缩放处理
# @File    : icon_big_zoom.py
# @Software: PyCharm


import cv2
import shutil
from work_icon_cut.get_pic_list import *


def clip_big_icon():
    pass
    # 坐标为[y0:y1, x0:x1]
    try:
        img = cv2.imread(pic_read)
        # img = cv2.imread(pic_read)
        # print(img.shape)
        height = img.shape[0]
        width = img.shape[1]
    except Exception as e:
        print(e)
        return print("数据读取出错！")

    get_ratio = height / width
    # print(f'get_ratio:  {get_ratio}')

    height_expected = 830
    width_expected = 650
    ratio_expected = height_expected / width_expected
    # print(f'ratio_expected:  {ratio_expected}')

    y0 = 0
    y1 = height
    x0 = 0
    x1 = width

    if get_ratio > ratio_expected:
        # 高度要减少
        width_set = width
        height_set = ratio_expected * width_set
        # get_ratio = height_set / width_set

        cut_value_height = height - height_set

        y0 = int(cut_value_height / 2)
        y1 = int(height - cut_value_height / 2)

        x0 = 0
        x1 = width_set
    else:
        if get_ratio < ratio_expected:
            # 宽度要减少
            height_set = height
            width_set = height_set / ratio_expected
            # get_ratio = height_set / width_set

            cut_value_width = width - width_set

            y0 = 0
            y1 = height_set

            x0 = int(cut_value_width / 2)
            x1 = int(width - cut_value_width / 2)

    cropped = img[y0:y1, x0:x1]
    cv2.imwrite(pic_tmp, cropped)

    img = cv2.imread(pic_tmp)
    '''
    try:
        img_resized = cv2.resize(img, (650, 830), interpolation=cv2.INTER_CUBIC)
    except Exception as e:
        print(e)
        return
    '''
    img_resized = cv2.resize(img, (650, 830), interpolation=cv2.INTER_CUBIC)
    path_save = pic_save
    cv2.imwrite(path_save, img_resized)


'''
# 生成用来显示的图像
height = y1 - y0
width = x1 - x0
img_blank = np.zeros((height, width, 3), np.uint8)  # uint8 8 位无符号整数（0 ~ 255）
blank_start = 0

for i in range(height):
    for j in range(width):
        img_blank[i][blank_start + j] = img[i][j]

img_resized = cv2.resize(img_blank, (650, 830), interpolation=cv2.INTER_CUBIC)
path_save = "./23.jpg"
cv2.imwrite(path_save, img_resized)
'''
# 坐标为[y0:y1, x0:x1]
# cropped = img[0:128, 0:512]
# cv2.imwrite("./cv_cut_21.jpg", cropped)


# out_path_3 = out_path_1 + path_icon_name

pic_read = ".\\3.jpg"
pic_save = ".\\22.jpg"
pic_tmp = ".\\tmp.jpg"

# clip_big_icon()
# path = "G:\\Data\\python\\meizitu\\pic"
path = "G:\\Data\\python\\my_download\\Male\\outfile"
pic_list = get_pic_list(path)
for i in range(0, len(pic_list)):
    # print(pic_list[i])
    print(f'\n开始处理第{i}')
    old_file = pic_list[i]
    '''此处需要根据目录，特殊定义'''
    # girl_1目录  G:\Data\python\my_download\outfile\list
    # icon_id = pic_list[i].split('\\')[6].split('-')[0]

    # boy_1目录  G:\Data\python\my_download\Male\outfile
    # icon_id = 'boy1_' + pic_list[i].split('\\')[6]

    # girl_2目录  "G:\\Data\\python\\meizitu\\pic"
    # icon_id = pic_list[i].split('\\')[5]

    # boy_2  "G:\\Data\\python\\my_download\\Male\\outfile"
    icon_id = 'boy2_' + pic_list[i].split('\\')[6]

    '''此处需要根据目录，特殊定义'''
    out_path_1 = "G:\\Data\\python\\my_download\\outfiles\\py_cut_icon\\big\\"
    out_path_2 = out_path_1 + icon_id + "\\old\\"
    out_path_3 = out_path_1 + icon_id

    if not os.path.isdir(out_path_2):
        os.makedirs(out_path_2)
        os.makedirs(out_path_1 + icon_id + "\\tmp\\")
        os.makedirs(out_path_1 + icon_id + "\\select\\")
        print(f'{icon_id}目录创建成功')
    else:
        print(f'{icon_id}目录已存在')

    new_file = out_path_2 + pic_list[i].split('\\')[-1]
    # print(old_file)
    # print(new_file)

    shutil.copyfile(old_file, new_file)

    # 剪裁方法输入参数设定
    pic_read = new_file
    pic_save = out_path_3 + "\\" + pic_list[i].split('\\')[-1]
    # print(pic_save)
    pic_tmp = out_path_1 + icon_id + "\\tmp\\" + pic_list[i].split('\\')[-1]
    # print(pic_tmp)
    clip_big_icon()
    print(f'第{i}条处理结束\n')
