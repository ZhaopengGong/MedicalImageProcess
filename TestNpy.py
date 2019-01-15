#!/usr/bin/env python2.7
# -*- coding:utf-8 -*- 
# import skimage.io as io
import pandas as pd
import numpy as np
import os
import xlsxwriter
import xlrd
from scipy import ndimage as ndi
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import random

# dicom_file_path = "E:/桌面文件夹/Test1/00029167/0001.dcm"
# dicom_file = pydicom.dcmread(dicom_file_path)
# dicom_file.update({'InstanceNumber': pydicom.v})
# print(type(dicom_file.InstanceNumber))
# dicom_file.InstanceNumber = int(60 - int(dicom_file.InstanceNumber))
# dicom_file.save_as(os.path.join(sub_folder_path, str.zfill(str(int(dicom_file.InstanceNumber)), 4)+".dcm"))
# os.remove(dicom_file_path)

# directory = "C:\\Users\\SIPL-gzp\\Desktop\\original_dicom\\00029167"
# for path_, _, file_ in os.walk(directory):
#     for f in sorted(file_):
#         file1 = os.path.abspath(os.path.join(path_, f))
#         image = pydicom.read_file(file1)
#         sliceID = image.data_element("InstanceNumber").value - 1
#         print(sliceID)


import os
import numpy as np
import sys
# from skimage import io,data
# a = np.random.randn(10,5)
# print(a)
# print(a[0])


# seg_result_path = 'E:/桌面文件夹/粗分割结果/R9_13.npz'
# original_label_path = 'E:/桌面文件夹/粗分割结果/0013.npy'
# output_folder_path = 'E:/桌面文件夹/粗分割结果/图片结果'
# height = 420
# width = 420
# pic_num = 60
#
# original_label_file = np.load(original_label_path)
# seg_result_file = np.load(seg_result_path)
# seg_result_file = seg_result_file['volume']
#
# f = [os.path.join(rootdir, filename)
#      for rootdir, dirnames, filenames in os.walk('F:/PPT素材/PPT汇总')
#      for filename in filenames if '.ppt' in filename]
# f.sort()
# sizeI = np.round(np.divide(np.multiply([420, 420, 60], 0.5), True))
# sizeI = np.divide(np.multiply([420, 420, 60], 0.5), True)
# sizeI = np.multiply([420, 420, 60], 0.5)
# x = np.linspace(0, 4, 5)
# y = np.linspace(0, 4, 5)
# z = np.linspace(0, 2, 3)
# a = np.arange(12).reshape(3, 4)
# MASK = np.ones((3, 4), dtype=np.uint8) > 1
# MASK[a > 3] = True
# digital, num = np.unique(a, return_counts=True)
# print(digital)
# digital = digital[digital != 3]
# print(digital)
#
# print(os.path.splitext('my.txt'))


# dicomLabelFilePath = 'E:/桌面文件夹/original_dicom/00029167/000001.dcm'
# dicomFile = pydicom.read_file(dicomLabelFilePath)
# array = dicomFile.pixel_array
# name = 'EW2'

# nii_file = 'F:/DeepLearing/data/64例裁剪后标注数据WBGG-nii/00029167/x000001.nii.gz'
# data = nibabel.load(nii_file).get_data().transpose(1, 0, 2)
# print(type(data.shape[0]))

# dicomFile = 'E:/桌面文件夹/original_dicom/00029167/000014.dcm'
# ds = pydicom.dcmread(dicomFile)
# pixelArray = ds.pixel_array

# npy_file ='F:/DeepLearing/data/测试的结果/QT原始dicom_npy/0001.npy'
# dicom_npy = np.load(npy_file)
#
# image_2d = dicom_npy[0, :, :]
# Convert to float to avoid overflow or underflow losses.

# image_2d = pixelArray.astype(float)

# Rescaling grey scale between 0-255
# image_2d_scaled = (np.maximum(image_2d, 0) / image_2d.max() if image_2d.max() else 1) * 255.0
# # Convert to uint
# image_2d_scaled = np.uint8(image_2d_scaled)
# print(image_2d_scaled.shape)
# print(image_2d_scaled[0, 0])
# plt.imshow(image_2d_scaled, cmap=plt.cm.gray)
# plt.show()
# npy_file_path = 'G:/Deep Learing/data/EarIOuCalculateData/标注文件/0001.npy'
# npy_file = np.load(npy_file_path)
# slice_arr = npy_file[:,:,23]
# print(slice_arr.shape)
# print(np.where(slice_arr==2))

# result_folder_path = 'G:/Deep Learing/data/EarIOuCalculateData/11个解剖结构的结果文件'
# path_list = os.listdir(result_folder_path)
# path_list.sort()
# for fileName in path_list:
#     print(fileName)

# npy_file_path = "C:\\Users\\Administrator\\Desktop\\0001.npy"
# label_file = np.load(npy_file_path)
# print(np.unique(label_file))

c = (1, 2)(3, 4)
print(c)