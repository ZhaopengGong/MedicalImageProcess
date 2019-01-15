'''
@Author: 弓照鹏
@LastEditors: 弓照鹏
@Date: 2018-11-30 15:33:00
@LastEditTime: 2018-12-02 17:41:53
@organization: BJUT
'''
# -*- coding:utf-8 -*- 

import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

# path = 'D:\\workspace\\MedicalImageWorkspace\\FCN-BoundingBox\\validate\\0001.npy'
# imageFolder = 'D:\\workspace\\MedicalImageWorkspace\\FCN-BoundingBox\\image'
# npy_file = np.load(path)

# slice_file  = npy_file[:,:,23]
# np_array = np.array(slice_file).reshape(420, 420)

# height, width= slice_file.shape
# left_matrix = slice_file[:, 0:int(width/2)]
# right_matrix = slice_file[:, int(width/2):]
# print((np.where(left_matrix==4)[0])[np.argmin(np.where(left_matrix==4)[0])])


# img = cv2.imdecode(slice_file, 0)
# cv2.namedWindow("test", flags=cv2.WINDOW_AUTOSIZE)
# cv2.imshow("img_path", img)
# cv2.waitKey(0)

# 将dicom图像直接转换为数组并且保存在本地

# for i in range(60):
#     image_2d = npy_file[:,:,i]
#     image_path = os.path.join(imageFolder, "0001_"+str.zfill(str(i), 4)+".jpg")
#     image_2d_scaled = (np.maximum(image_2d, 0) / image_2d.max() if image_2d.max() else 1) * 255.0
#     cv2.imwrite(image_path, image_2d_scaled)

# 测试保存之后的图像是几个通道的

sum_CG = 0
"sum_CG"