#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
# 标注数据可视化
# Author: Gong Zhaopeng
# Date:   2018/7/15 11:37

import os
import numpy as np
from skimage import io,data
import nibabel

label_file_path = 'E:/data/TrainData/CT-Labels/00029167/00029167.nii.gz'
output_path = 'E:/data/标注数据可视化'


if (os.path.exists(output_path) == 0):
    os.makedirs(output_path)

data = nibabel.load(label_file_path).get_data().transpose(1, 0, 2)

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

