#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
# 对文件进行批量的重命名
# Author: Gong Zhaopeng
# Date:   2018/6/24 15:57

import os

# ctDir = 'E:/data/CT-Labels-CZD-Nii'
#
# for folderName in os.listdir(ctDir):
#     patientFolderPath = os.path.join(ctDir, folderName)
#     for ctFileName in os.listdir(os.path.normpath(patientFolderPath)):
#         # 原文件的名称注意这里包含了路径
#         originalFileName = os.path.join(patientFolderPath, ctFileName)
#         # 当前文件的名称，这里也包含了路径
#         newFileName = os.path.join(patientFolderPath, folderName+'.nii.gz')
#         os.rename(os.path.normpath(originalFileName), os.path.normpath(newFileName))

folderPath = 'F:/DeepLearing/data/友谊66例标注数据'
for folderName in os.listdir(folderPath):
    originalFolderPath = os.path.normpath(os.path.join(folderPath, folderName))
    targetFolderPath = os.path.normpath(os.path.join(folderPath, folderName.split('-')[0]))
    os.rename(originalFolderPath, targetFolderPath)