#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
# 加载nifiti文件
# Author: Gong Zhaopeng
# Date:   2018/7/3 11:02

import nibabel

niiFile = 'C:\\Users\\SIPL-gzp\\Desktop\\label0010.nii'
count = 0
nifitiFile = nibabel.load(niiFile).get_data()
for slice_number in range(nifitiFile.shape[2]):
    matrix = nifitiFile[:, :, slice_number]
    if(len(matrix.nonzero()[0])>0):
        count += 1
print(count)
