#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
# 保存分割结果
# Author: Gong Zhaopeng
# Date:   2018/7/8 14:28
import os
import numpy as np
from skimage import io,data

label_file_path = 'F:/DeepLearing/data/测试的结果/QT标注数据/0001.npy'
output_path = 'F:/DeepLearing/data/测试的结果/QT标注数据可视化'


if (os.path.exists(output_path) == 0):
    os.makedirs(output_path)

data = np.load(label_file_path)
for index in range(data.shape[2]):
    new_image = np.zeros((420, 420, 3), dtype=np.uint8)
    output_file_path = os.path.normpath(os.path.join(output_path, str.zfill(str(index+1), 4)+'.jpg'))
    for row in range(420):
        for col in range(420):
            if(data[row, col, index] >0):
                new_image[row, col, 0] = 255
                new_image[row, col, 1] = 255
                new_image[row, col, 2] = 255
            else:
                new_image[row, col, 0] = 0
                new_image[row, col, 1] = 0
                new_image[row, col, 2] = 0
    io.imsave(output_file_path, new_image)

