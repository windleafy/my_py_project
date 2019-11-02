#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 9:37
# @Author  : Wind
# @Site    : v_0.1
# @File    : icon_small_dlib_cut.py
# @Software: PyCharm


import dlib
import numpy as np
import cv2
from work_icon_cut.get_pic_list import *
import shutil


def init():
    # dlib检测器初始化
    print('dlib初始化开始')
    init_detector = dlib.get_frontal_face_detector()
    path = "F:/python_test/test/face/predictor/shape_predictor_68_face_landmarks.dat"
    dlib.shape_predictor(path)
    print('dlib初始化结束')
    return init_detector


def clip_icon():
    img = cv2.imread(img_res)
    # print("img/shape", img.shape)  # 高、宽、通道数

    # dlib检测
    try:
        dets = detector(img, 1)
        # print("人脸数", len(dets))
    except Exception as e:
        print(e)
        return print('处理detector(img, 1)失败')

    if len(dets) == 0:
        return print('未识别出人脸')

    height = 0
    width = 0

    # 计算要生成的图像大小
    for k, d in enumerate(dets):
        height = d.bottom() - d.top() + 200
        width = d.right() - d.left() + 200

        if height > width:
            width = height
        else:
            height = width

    # 绘制用来显示人脸的图像大小
    print("img_blank的大小：")
    print("高度：", height, "宽度：", width)

    # 生成用来显示的图像
    img_blank = np.zeros((height, width, 3), np.uint8)  # uint8 8 位无符号整数（0 ~ 255）
    # 记录每次开始写入人脸像素的宽度位置
    blank_start = 0
    # 将人脸填充到img_blank
    for k, d in enumerate(dets):
        # 填充
        for i in range(height):
            for j in range(width):
                # 调整填充坐标位置
                try:
                    img_blank[i][blank_start + j] = img[d.top() - 100 + i][d.left() - 100 + j]
                except Exception as e:
                    print(e)
                    return print('调整填充坐标位置，处理失败')

        # 更新读取图像起始位置
        blank_start += width

    # 图片缩放
    img_resized = cv2.resize(img_blank, (300, 300), interpolation=cv2.INTER_CUBIC)

    # 文件输出
    cv2.imwrite(path_save, img_resized)
    cv2.waitKey(0)


def crop_face():
    # detector = init()
    img_res_name = img_res.split('\\')[-1].split('.')[0]
    try:
        img = cv2.imread(img_res)
        img_height = img.shape[0]
        img_width = img.shape[1]
        print(f'图片尺寸:  {img.shape}')

        dets = detector(img, 1)
        print("人脸数", len(dets))
        if len(dets) == 0:
            return print('未发现人脸')
    except Exception as e:
        print(e)
        return print('数据读取出错')
    # print(dets)

    for k, v in enumerate(dets):
        # @margin脸轮廓外部区域，最小值为0，表示刚好取脸部大小
        margin = 150
        if (v.left() - margin) >= 0:
            x0 = v.left() - margin
        else:
            x0 = 0

        if (v.top() - margin) >= 0:
            y0 = v.top() - margin
        else:
            y0 = 0

        if (v.bottom() + margin) <= img_height:
            y1 = v.bottom() + margin
        else:
            y1 = img.shape[0]

        if (v.right() + margin) <= img_width:
            x1 = v.right() + margin
        else:
            x1 = img.shape[1]

        height = y1 - y0
        width = x1 - x0

        # 处理为正方形
        if height > width:
            y1 = y1 - (height - width)
            height = width
        else:
            x1 = x1 - (width - height)
            width = height

        # print(f'cropped_height:  {height}')
        # print(f"cropped_width: {width}")

        # 图片剪裁
        img_cropped = img[y0:y1, x0:x1]
        # 图片缩放
        img_resized = cv2.resize(img_cropped, (width_set, height_set), interpolation=cv2.INTER_CUBIC)

        # 图片保存
        pic = path_save + img_res_name + '_' + f"{k}.jpg"
        print(pic)
        cv2.imwrite(pic, img_resized)
        # print("\n")


# dlib初始化
detector = init()
'''
img_res = "G:\\Data\\python\\my_download\\outfile\\list\\10836-道重沙由美\\" \
          "道重さゆみ Sayumi Michishige [Hello! Project Digital Books] Vol.117\\30.jpg"
          
img_res = "G:\\Data\\python\\my_download\\outfile\\list\\86.jpg"
path_save = "G:\\Data\\python\\my_download\\outfile\\py_cut_icon\\small\\10836\\30.jpg"
clip_icon()
'''

# path = "G:\\Data\\python\\meizitu\\pic"
path = "G:\\Data\\python\\my_download\\Male\\outfile"
pic_list = get_pic_list(path)
# for pic_index in range(0, 10):

for pic_index in range(0, len(pic_list)):

    print(f'第{pic_index}条处理开始')

    '''此处需要根据目录，特殊定义'''
    # girl_1目录  G:\Data\python\my_download\outfile\list
    # path_icon_name = pic_list[pic_index].split('\\')[6].split('-')[0]

    # boy_1目录  G:\Data\python\my_download\Male\outfile
    # path_icon_name = 'boy1_' + pic_list[pic_index].split('\\')[6]

    # girl_2目录  "G:\\Data\\python\\meizitu\\pic"
    # path_icon_name = pic_list[pic_index].split('\\')[5]

    # boy_2目录  "G:\\Data\\python\\my_download\\Male\\outfile"
    path_icon_name = 'boy2_' + pic_list[pic_index].split('\\')[6]

    '''此处需要根据目录，特殊定义'''

    # print(pic_index)
    out_path_1 = "G:\\Data\\python\\my_download\\outfiles\\py_cut_icon\\small\\"
    out_path_2 = out_path_1 + path_icon_name + "\\old\\"
    out_path_3 = out_path_1 + path_icon_name + '\\'

    if not os.path.isdir(out_path_2):
        os.makedirs(out_path_2)
        print(f'{path_icon_name}目录创建成功')
        # os.makedirs(out_path_1 + path_icon_name + "\\tmp\\")
    else:
        print(f'{path_icon_name}目录已存在')

    old_file = pic_list[pic_index]
    new_file = out_path_2 + old_file.split("\\")[-1]
    # print(f"old_file:{old_file}")
    # print(f"new_file:{new_file}")
    shutil.copyfile(old_file, new_file)

    # 图片资源 print(pic_list[pic_index])
    img_res = new_file
    print(img_res)

    '''此处需要根据目录，特殊定义'''
    # path_save = out_path_3 + pic_list[pic_index].split('\\')[-1]
    path_save = out_path_3
    # print(path_save)
    width_set = 300
    height_set = 300
    crop_face()
    print(f'第{pic_index}条处理结束\n')
