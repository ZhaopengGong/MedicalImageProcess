#!/usr/bin/env python2.7
# -*- coding:utf-8 -*- 
# Author: Gong Zhaopeng
# Date:   2018/7/26 14:55
# 可视化dicom原始图像，需要注意的是这里的图像已经转化为了浮点数类型的了

import os
import numpy as np
import matplotlib.pyplot as plt


dicomNpyFile = 'C:\\Users\\Administrator\\Desktop\\image\\0001.npy'
dicom_npy = np.load(dicomNpyFile)

image_2d = dicom_npy[:, :, 21]

image_2d_scaled = (np.maximum(image_2d, 0) / image_2d.max() if image_2d.max() else 1) * 255.0
# # Convert to uint
# image_2d_scaled = np.uint8(image_2d_scaled)
# print(image_2d_scaled.shape)
# print(image_2d_scaled[0, 0])
plt.imshow(image_2d, cmap=plt.cm.gray)
plt.show()