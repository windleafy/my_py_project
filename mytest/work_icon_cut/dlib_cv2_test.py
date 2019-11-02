#!/usr/bin/env python
"""人脸剪裁，单张测试"""
# -*- coding: utf-8 -*-
# @Time    : 2019/9/25 11:59
# @Author  : Wind
# @File    : dlib_cv2_test.py
# @Software: PyCharm
from base_kit.base_dlib_face import *
from base_kit.base_file import dir_chk_create


# dlib初始化
dlib_data_path = './base_kit/shape_predictor_68_face_landmarks.dat'
detector = dlib_init(dlib_data_path)

'''待处理图片列表代码插入点'''
for i in range(1):
    # 读取图片数据，获取人脸信息。
    img_res_path = './res/1.jpg'
    faces, img = get_faces(detector, img_res_path)
    # img.shape、faces[0].left()、faces[0].top()、faces[0].right()、faces[0].bottom()
    print(f'{img_res_path}人脸信息获取完毕')

    # 根据人脸信息，剪裁头像。
    img_res_name = img_res_path.split('/')[-1].split('.')[0]
    save_path = f'./outfile/{img_res_name}/'
    dir_chk_create(save_path)
    print('开始剪裁')
    crop_face(faces, img, save_path)
    print('剪裁完毕')


# 按指定长宽比剪裁，缩放至指定尺寸
# res_path = './res/1.jpg'  # 准备剪裁的图片
# crop_by_ratio(res_path)
