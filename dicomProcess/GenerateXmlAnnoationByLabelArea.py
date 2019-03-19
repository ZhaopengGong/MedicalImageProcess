#!/usr/bin/env python
# coding=UTF-8
'''
@Author: 弓照鹏
@LastEditors: 弓照鹏
@organization: BJUT
@Date: 2019-03-12 15:21:31
@LastEditTime: 2019-03-19 09:54:17
通过连通域来生成对应的标注xml文件
'''

from lxml.etree import Element, SubElement, tostring
import pprint
from xml.dom.minidom import parseString
import os
import pydicom 
import numpy as np
import cv2

from skimage import measure, color
import pydicom
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# 标注数据文件夹路径
label_folder_path = 'H:\\耳部CT数据集\\WED138例标注数据裁剪后'
# 原始数据文件夹路径
original_folder_path = 'H:\\耳部CT数据集\\外耳道138例原始数据裁剪后'
# 输出的文件夹的路径
target_folder_path = 'H:\\耳部CT数据集\\WEDAnnotationXml'
# 保存包含外耳道的dcm对应的jpg图像
image_folder_path = 'H:\\WED-DCM2JPG'

total_count = len(os.listdir(label_folder_path))
i = 0
for folderName in os.listdir(label_folder_path):
        i += 1
        print(folderName, str(i)+'/'+str(total_count))
        labelFolderPath = os.path.join(label_folder_path, folderName)
        imageFolderPath = os.path.join(original_folder_path, folderName)
        for fileName in os.listdir(labelFolderPath):
                labelFilePath = os.path.join(labelFolderPath, fileName)
                imageFilePath = os.path.join(original_folder_path, folderName,fileName)
                dicom_file = pydicom.read_file(labelFilePath)
                dicom_array = dicom_file.pixel_array
                labels=measure.label(dicom_array,background=0)
                if(len(np.unique(labels))>1):
                        image_dicom_file = pydicom.read_file(imageFilePath)
                        image_dicom_array = image_dicom_file.pixel_array
                        node_root = Element('annotation')
                        node_folder = SubElement(node_root, 'folder')
                        node_folder.text = folderName

                        node_filename = SubElement(node_root, 'filename')
                        node_filename.text = folderName+"_"+fileName.split(".")[0]+".jpg"

                        node_size = SubElement(node_root, 'size')
                        node_width = SubElement(node_size, 'width')
                        node_width.text = '420'

                        node_height = SubElement(node_size, 'height')
                        node_height.text = '420'

                        node_depth = SubElement(node_size, 'depth')
                        node_depth.text = '1'
                        image_path = os.path.join(image_folder_path, folderName+"_"+fileName.split(".")[0]+".jpg")
                        image_2d_scaled = (np.maximum(image_dicom_array, 0) / image_dicom_array.max() if image_dicom_array.max() else 1) * 255.0
                        cv2.imwrite(image_path, image_2d_scaled)
                        for region in measure.regionprops(labels):
                                minr, minc, maxr, maxc = region.bbox
                                node_object = SubElement(node_root, 'object')
                                node_name = SubElement(node_object, 'name')
                                node_name.text = 'WED'
                                node_difficult = SubElement(node_object, 'difficult')
                                node_difficult.text = '0'
                                node_bndbox = SubElement(node_object, 'bndbox')
                                # 写入xml文件需要将数字转换为字符串
                                node_xmin = SubElement(node_bndbox, 'xmin')
                                node_xmin.text = str(minc)
                                node_ymin = SubElement(node_bndbox, 'ymin')
                                node_ymin.text = str(minr)
                                node_xmax = SubElement(node_bndbox, 'xmax')
                                node_xmax.text = str(maxc)
                                node_ymax = SubElement(node_bndbox, 'ymax')
                                node_ymax.text = str(maxr)
                                xml = tostring(node_root, pretty_print=True)  #格式化显示，该换行的换行
                                output_file_path = os.path.join(target_folder_path, folderName+"_"+fileName.split(".")[0]+".xml")
                                output_file =  open(output_file_path, 'w')
                                output_file.write(str(xml, encoding = "utf-8"))
                                output_file.close()
                