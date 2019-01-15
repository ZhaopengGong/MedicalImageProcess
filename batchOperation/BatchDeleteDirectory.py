#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
# 批量删除文件夹
# Author: Gong Zhaopeng
# Date:   2018/7/1 10:13
import shutil
import os

folderPath = 'E:/桌面文件夹/NIFTI_EW'

# for patientFolder in os.listdir(folderPath):
#     sub_folderPath = os.path.normpath(os.path.join(folderPath, patientFolder))
#     print("正在删除"+patientFolder)
#     for st0_Folder in os.listdir(sub_folderPath):
#         deleteFolderPath = os.path.normpath(os.path.join(sub_folderPath, 'ST0', "SE0"))
#         shutil.rmtree(deleteFolderPath)

for patientFolder in os.listdir(folderPath):
    sub_folderPath = os.path.normpath(os.path.join(folderPath, patientFolder))
    for fileName in os.listdir(sub_folderPath):
        if '.mat' in fileName:
            print('正在删除'+ patientFolder+"--"+fileName)
            filePath = os.path.normpath(os.path.join(sub_folderPath, fileName))
            os.remove(filePath)