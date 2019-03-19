#!/usr/bin/env python
# coding=UTF-8
'''
@Author: 弓照鹏
@LastEditors: 弓照鹏
@organization: BJUT
@Date: 2019-03-12 11:55:49
@LastEditTime: 2019-03-12 15:23:44
基于连通域获取标注区域的boundingbox的测试文件
'''

from skimage import measure, color
import pydicom
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

filepath =  'H:\\耳部CT数据集\\WED64例标注数据导出后\\00158998\\000037.dcm'
dicom_file= pydicom.read_file(filepath)
dicom_array = dicom_file.pixel_array
labels=measure.label(dicom_array,background=0)
image_label_overlay =color.label2rgb(labels, image=dicom_array) #不同标记用不同颜色显示

fig,(ax0,ax1)= plt.subplots(1,2, figsize=(8, 6))
ax0.imshow(dicom_array,plt.cm.gray)
ax1.imshow(image_label_overlay)
for region in measure.regionprops(labels):
    print(region.area)
    #绘制外包矩形
    minr, minc, maxr, maxc = region.bbox
    rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                              fill=False, edgecolor='red', linewidth=2)
    ax1.add_patch(rect)
fig.tight_layout()
plt.show()