#!/usr/bin/env python2.7
# -*- coding:utf-8 -*- 
# Author: Gong Zhaopeng
# Date:   2018/7/26 11:53
# 将数据进行翻转，旋转1份数据产生13份数据

import os
import numpy as np


def flip(inputs, labels, axis):
    return np.flip(inputs, axis), np.flip(labels, axis)


def rotate(inputs, labels, num_of_rots, axes):
    return np.rot90(inputs, num_of_rots, axes), np.rot90(labels, num_of_rots, axes)


original_dicom_folder_path = 'F:\\DeepLearing\\data\\原始数据npy'
label_dicom_folder_path = 'F:\\DeepLearing\\data\\标注数据npy'
totalDataNumber = len(os.listdir(original_dicom_folder_path))
for filename in sorted(os.listdir(original_dicom_folder_path)):
    # 原始dicom的npy文件的路径
    original_dicom_npy_file_path = os.path.normpath(os.path.join(original_dicom_folder_path, filename))
    # 标记dicom的npy文件的路径
    label_dicom_npy_file_path = os.path.normpath(os.path.join(label_dicom_folder_path, filename))
    original_dicom_npy_file = np.load(original_dicom_npy_file_path)
    label_dicom_npy_file = np.load(label_dicom_npy_file_path)
    for index in range(1, 13):
        if(index == 1):
            target_original_npy_file, target_label_npy_file = flip(original_dicom_npy_file, label_dicom_npy_file, axis=0)
        elif(index == 2):
            target_original_npy_file, target_label_npy_file = flip(original_dicom_npy_file, label_dicom_npy_file, axis=1)
        elif(index == 3):
            target_original_npy_file, target_label_npy_file = flip(original_dicom_npy_file, label_dicom_npy_file, axis=2)
        elif(index == 4):
            target_original_npy_file, target_label_npy_file = rotate(original_dicom_npy_file, label_dicom_npy_file, 1, axes=(0, 1))
        elif(index == 5):
            target_original_npy_file, target_label_npy_file = rotate(original_dicom_npy_file, label_dicom_npy_file, 2, axes=(0, 1))
        elif(index == 6):
            target_original_npy_file, target_label_npy_file = rotate(original_dicom_npy_file, label_dicom_npy_file, 3, axes=(0, 1))
        elif(index == 7):
            target_original_npy_file, target_label_npy_file = rotate(original_dicom_npy_file, label_dicom_npy_file, 1, axes=(0, 2))
        elif(index == 8):
            target_original_npy_file, target_label_npy_file = rotate(original_dicom_npy_file, label_dicom_npy_file, 2, axes=(0, 2))
        elif(index == 9):
            target_original_npy_file, target_label_npy_file = rotate(original_dicom_npy_file, label_dicom_npy_file, 3, axes=(0, 2))
        elif(index == 10):
            target_original_npy_file, target_label_npy_file = rotate(original_dicom_npy_file, label_dicom_npy_file, 1, axes=(1, 2))
        elif(index == 11):
            target_original_npy_file, target_label_npy_file = rotate(original_dicom_npy_file, label_dicom_npy_file, 2, axes=(1, 2))
        elif(index == 12):
            target_original_npy_file, target_label_npy_file = rotate(original_dicom_npy_file, label_dicom_npy_file, 3, axes=(1, 2))
        # 新保存的数据的编号
        saveNumber = str.zfill(str(index+totalDataNumber+12*(int(filename.split('.')[0])-1)), 4)
        print('正在处理', filename.split('.')[0], saveNumber)
        target_original_npy_file_path = os.path.normpath(os.path.join(original_dicom_folder_path, saveNumber+'.npy'))
        target_label_npy_file_path = os.path.normpath(os.path.join(label_dicom_folder_path, saveNumber+'.npy'))
        if target_label_npy_file.shape[0] == 420 and target_label_npy_file.shape[1] == 420:
            np.save(target_original_npy_file_path, target_original_npy_file)
            np.save(target_label_npy_file_path, target_label_npy_file)