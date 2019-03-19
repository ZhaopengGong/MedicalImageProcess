#!/usr/bin/env python
# coding=UTF-8
'''
@Author: 弓照鹏
@LastEditors: 弓照鹏
@organization: BJUT
@Date: 2019-03-11 14:40:45
@LastEditTime: 2019-03-15 10:44:33
将原来比较大的数据立方体生成96*96*60大小的立方体
'''

import numpy as np
import os, sys

image_data_folder = 'H:\\耳部CT数据集\\OriginalDicomCropSymmetryNpy_64'
label_data_folder = 'H:\\耳部CT数据集\\LabelDicomCropSymmetry_UnCombine_Split_npy'
cube_label_npy_folder = 'H:\\耳部CT数据集\\cube_label_npy'
cube_image_npy_folder = 'H:\\耳部CT数据集\\cube_image_npy'

target_width = 96
target_height = 96
height = 420
width = 420

#当前所有的耳部关键解剖结构的名称 
# organNameList = ['ZG', 'DG', 'EW1', 'EW2', 'WBGG', 'HBGG', 'QBGG', 'JJMQW', 'QT', 'NTD']
organNameList = ['JJMQW', 'QT', 'NTD']
# 关键解剖结构的索引
organ_index = 0
# 遍历每个关键解剖结构的名称并且生成对应的解剖结构的小的立方体
for organName in organNameList:
    organ_index += 1
    # 显示处理程序的进度条
    sys.stdout.write('\r>> Converting image %d/%d' % (organ_index, len(organNameList)))
    sys.stdout.flush()
    # 上面的全局变量指定的是一个的父类的文件夹，下面为每个解剖结构创建文件夹
    organ_label_data_folder = os.path.join(label_data_folder, organName)
    organ_cube_label_npy_folder = os.path.join(cube_label_npy_folder, organName)
    organ_cube_image_npy_folder = os.path.join(cube_image_npy_folder, organName)
    # 这里是判断我们指定的组织器官的文件夹是不是存在，如果不存在就创建一个
    if not os.path.exists(organ_cube_label_npy_folder):
        os.mkdir(organ_cube_label_npy_folder)
    if not os.path.exists(organ_cube_image_npy_folder):
        os.mkdir(organ_cube_image_npy_folder)
    # 病人的id，这里我们要将前8例数据作为验证和测试集，注意这里的验证集并没有参与训练，只是在训练过程中不断的验证
    patient_index = 0
    for label_fileName in sorted(os.listdir(organ_label_data_folder)):
        patient_index += 1
        if(patient_index>8):
            organ_cube_label_npy_type_folder = os.path.join(organ_cube_label_npy_folder, 'train')
            organ_cube_image_npy_type_folder = os.path.join(organ_cube_image_npy_folder, 'train')
        else:
            organ_cube_label_npy_type_folder = os.path.join(organ_cube_label_npy_folder, 'valid')
            organ_cube_image_npy_type_folder = os.path.join(organ_cube_image_npy_folder, 'valid')
        # 判断训练或者是验证的文件夹是不是存在
        if not os.path.exists(organ_cube_label_npy_type_folder):
            os.mkdir(organ_cube_label_npy_type_folder)
        if not os.path.exists(organ_cube_image_npy_type_folder):
            os.mkdir(organ_cube_image_npy_type_folder)
        print(label_fileName)
        # 数据和label的路径
        label_file_path = os.path.join(organ_label_data_folder, label_fileName)
        image_file_path = os.path.join(image_data_folder, label_fileName)
        # 加载数据和label文件
        image_file = np.load(image_file_path)
        label_file = np.load(label_file_path)
        
        left_y_min_list = [] 
        left_y_max_list = []
        left_x_min_list = []
        left_x_max_list = []
        right_y_min_list = [] 
        right_y_max_list = []
        right_x_min_list = []
        right_x_max_list = []
        for slice_index in range(label_file.shape[2]):
            label_file_slice = label_file[:,:, slice_index]
            
            # 划分为左侧的矩阵和右侧的矩阵
            left_matrix = label_file_slice[:, 0:int(width/2)]
            right_matrix = label_file_slice[:, int(width/2):]
            if(left_matrix.nonzero()[0].shape[0] != 0):
                left_y_min = (left_matrix.nonzero()[0])[np.argmin(left_matrix.nonzero()[0])]
                left_y_max = (left_matrix.nonzero()[0])[np.argmax(left_matrix.nonzero()[0])]
                left_x_min = (left_matrix.nonzero()[1])[np.argmin(left_matrix.nonzero()[1])]
                left_x_max = (left_matrix.nonzero()[1])[np.argmax(left_matrix.nonzero()[1])]
                left_y_min_list.append(left_y_min)
                left_y_max_list.append(left_y_max)
                left_x_min_list.append(left_x_min)
                left_x_max_list.append(left_x_max)
            if(right_matrix.nonzero()[0].shape[0] != 0):
                # 处理右侧的
                right_y_min = (right_matrix.nonzero()[0])[np.argmin(right_matrix.nonzero()[0])]
                right_y_max = (right_matrix.nonzero()[0])[np.argmax(right_matrix.nonzero()[0])]
                right_x_min = (right_matrix.nonzero()[1])[np.argmin(right_matrix.nonzero()[1])]
                right_x_max = (right_matrix.nonzero()[1])[np.argmax(right_matrix.nonzero()[1])]
                right_y_min_list.append(right_y_min)
                right_y_max_list.append(right_y_max)
                right_x_min_list.append(right_x_min)
                right_x_max_list.append(right_x_max)
        # 判断左侧是不是有立方体
        is_left_cube_exist = 0
        if(len(left_x_min_list)!=0 and len(left_y_min_list) and len(left_x_max_list) and left_y_max_list):
            is_left_cube_exist = 1
            # 循环完成之后取左边界和上边界的最小值，右边界和下边界的最大值
            left_x_min_value = min(left_x_min_list)
            left_y_min_value = min(left_y_min_list)
            left_x_max_value = max(left_x_max_list)
            left_y_max_value = max(left_y_max_list)
            # 左侧的值水平方向做减法
            x_original = left_x_max_value - left_x_min_value
            x_offset = int((target_width-x_original)/2)
            if(left_x_min_value>x_offset):
                left_x_min_value = left_x_min_value-x_offset
            else:
                left_x_min_value = 0
            left_x_max_value += x_offset
            # 判断修改后的值是否等于96了
            x_modify = left_x_max_value - left_x_min_value
            if(x_modify!=target_width):
                left_x_max_value += target_width - x_modify
            # 左侧的值垂直方向做减法
            y_original = left_y_max_value - left_y_min_value
            y_offset = int((target_height-y_original)/2)
            left_y_min_value = left_y_min_value-y_offset
            left_y_max_value += y_offset
            # 判断修改后的值是否等于96了
            y_modify = left_y_max_value - left_y_min_value
            if(y_modify!=target_height):
                left_y_max_value += target_height - y_modify
        # 判断右侧是不是有立方体
        is_right_cube_exist = 0
        if(len(right_x_min_list)!=0 and len(right_y_min_list) and len(right_x_max_list) and right_y_max_list):
            is_right_cube_exist = 1
            # 循环完成之后取左边界和上边界的最小值，右边界和下边界的最大值
            right_x_min_value = min(right_x_min_list)
            right_y_min_value = min(right_y_min_list)
            right_x_max_value = max(right_x_max_list)
            right_y_max_value = max(right_y_max_list)
            # 右侧的值水平方向做减法
            x_original = right_x_max_value - right_x_min_value
            x_offset = int((target_width-x_original)/2)
            if(right_x_min_value>x_offset):
                right_x_min_value = right_x_min_value-x_offset
            else:
                right_x_min_value = 0
            right_x_max_value += x_offset
            # 判断修改后的值是否等于96了
            x_modify = right_x_max_value - right_x_min_value
            if(x_modify!=target_width):
                right_x_max_value += target_width - x_modify
            # 右侧的值垂直方向做减法
            y_original = right_y_max_value - right_y_min_value
            y_offset = int((target_height-y_original)/2)
            right_y_min_value = right_y_min_value-y_offset
            right_y_max_value += y_offset
            # 判断修改后的值是否等于96了
            y_modify = right_y_max_value - right_y_min_value
            if(y_modify!=target_height):
                right_y_max_value += target_height - y_modify
            # 特别注意要转换为整数
            right_x_min_value += int(width/2)
            right_x_max_value += int(width/2)
            # 新建两个空的数组大小分别是96*96*60，用来保存左侧和右侧的立方体
        cube_left_label = np.zeros((target_height, target_width, 60))
        cube_right_label = np.zeros((target_height, target_width, 60))
        cube_left_image = np.zeros((target_height, target_width, 60))
        cube_right_image = np.zeros((target_height, target_width, 60))
        for slice_index in range(label_file.shape[2]):
            label_file_slice = label_file[:, :, slice_index]
            image_file_slice = image_file[:, :, slice_index]
            if(is_left_cube_exist == 1):
                cube_left_label[:, :, slice_index] = label_file_slice[left_y_min_value:left_y_max_value, left_x_min_value:left_x_max_value]
                cube_left_image[:, :, slice_index] = image_file_slice[left_y_min_value:left_y_max_value, left_x_min_value:left_x_max_value]
            if(is_right_cube_exist == 1):
                cube_right_label[:, :, slice_index] = label_file_slice[right_y_min_value:right_y_max_value, right_x_min_value:right_x_max_value]
                cube_right_image[:, :, slice_index] = image_file_slice[right_y_min_value:right_y_max_value, right_x_min_value:right_x_max_value]

        cube_label_left_save_path = os.path.join(organ_cube_label_npy_type_folder, label_fileName.split('.')[0]+'L.npy')
        cube_label_right_save_path = os.path.join(organ_cube_label_npy_type_folder, label_fileName.split('.')[0]+'R.npy')
        cube_image_left_save_path = os.path.join(organ_cube_image_npy_type_folder, label_fileName.split('.')[0]+'L.npy')
        cube_image_right_save_path = os.path.join(organ_cube_image_npy_type_folder, label_fileName.split('.')[0]+'R.npy')
        if(is_left_cube_exist == 1):
            np.save(cube_label_left_save_path, cube_left_label)
            np.save(cube_image_left_save_path, cube_left_image)
        if(is_right_cube_exist == 1):
            np.save(cube_label_right_save_path, cube_right_label)
            np.save(cube_image_right_save_path, cube_right_image)