#!/usr/bin/env python2.7
# -*- coding:utf-8 -*- 
# Author: Gong Zhaopeng
# Date:   2018/7/25 14:36
# 将标注数据的dicom序列传入直接识别出每张slice的x的最小值和最大值，y的最小值和最大值
import pydicom
import os
import numpy as np

LabelFolderPath = 'F:\\DeepLearing\\data\\鼓室标注区域测试'

def getPredictBoundingBox(LabelFolderPath):
    for pic_index in range(21, 33):
        dicomFilePath = os.path.normpath(os.path.join(LabelFolderPath, str.zfill(str(pic_index), 6)+'.dcm'))
        dicomFile = pydicom.read_file(dicomFilePath)
        dicomPixelArray = dicomFile.pixel_array
        height, width = dicomPixelArray.shape
        left_matrix = dicomPixelArray[:, 0:int(width/2)]
        right_matrix = dicomPixelArray[:, int(width/2):]
        if pic_index == 21:
            # print(left_matrix.shape, right_matrix.shape)
            if(left_matrix.nonzero()[0].shape[0] == 0):
                left_y_min = -1
                left_y_max = -1
                left_x_min = -1
                left_x_max = -1
            else:
                left_y_min = (left_matrix.nonzero()[0])[np.argmin(left_matrix.nonzero()[0])]
                left_y_max = (left_matrix.nonzero()[0])[np.argmax(left_matrix.nonzero()[0])]
                left_x_min = (left_matrix.nonzero()[1])[np.argmin(left_matrix.nonzero()[1])]
                left_x_max = (left_matrix.nonzero()[1])[np.argmax(left_matrix.nonzero()[1])]
            print(left_matrix.nonzero()[0])
            print(left_y_min, left_y_max, left_x_min, left_x_max)


if __name__ == '__main__':
    getPredictBoundingBox(LabelFolderPath)