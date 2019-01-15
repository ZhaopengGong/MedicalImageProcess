#!/usr/bin/env python2.7
# -*- coding:utf-8 -*- 
# Author: Gong Zhaopeng
# Date:   2018/8/25 10:17
# 读取nii文件并且可视化

import nibabel as nb
import matplotlib.pyplot as plt
import numpy as np
nii_file_path  = "F:/DeepLearing/source_code/miccai17-mmwhs-hybrid/ct_train_1001_image.nii"
nii_label_path = "F:/DeepLearing/source_code/miccai17-mmwhs-hybrid/ct_train_1001_label.nii"

nii_file = nb.load(nii_file_path).get_data()
image_2d = nii_file[:,:,150]
image_2d = np.transpose(image_2d,(1,0))
plt.imshow(image_2d, cmap=plt.cm.gray)
plt.show()
# print(nii_file.shape)