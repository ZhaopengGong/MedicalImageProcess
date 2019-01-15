'''
@Author: 弓照鹏
@LastEditors: 弓照鹏
@Date: 2018-11-30 16:41:30
@LastEditTime: 2018-11-30 18:17:49
@organization: BJUT
'''
# -*- coding:utf-8 -*- 

import numpy as np
import os
import cv2

original_npy_folder = "D:\\workspace\\MedicalImageWorkspace\\FCN-BoundingBox\\original_npy"
image_folder = "D:\\workspace\\MedicalImageWorkspace\\FCN-BoundingBox\\image"

npy_list = os.listdir(original_npy_folder)
for npy_filename in npy_list:
    image_sub_folder = os.path.join(image_folder, npy_filename.split(".")[0])
    npy_file_path = os.path.join(original_npy_folder, npy_filename)
    if not os.path.exists(image_sub_folder):
        os.mkdir(image_sub_folder)
    npy_file = np.load(npy_file_path)
    for slice_index in range(60):
        image_2d = npy_file[:,:,slice_index]
        image_path = os.path.join(image_sub_folder, npy_filename.split(".")[0]+"_"+str.zfill(str(slice_index), 4)+".jpg")
        image_2d_scaled = (np.maximum(image_2d, 0) / image_2d.max() if image_2d.max() else 1) * 255.0
        cv2.imwrite(image_path, image_2d_scaled)
    print(npy_filename)
