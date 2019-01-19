#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
# 从已经处理好的nii文件中批量提取特定组织器官的文件
# Author: Gong Zhaopeng
# Date:   2018/7/3 21:36
import os
import shutil


organName = 'CG'
# 包含10个关键解剖结构的文件夹
originalFolderPath = 'G:\\耳部CT数据集\\LabelDicomCropSymmetry_UnCombine'
# 抽取后写入的文件夹
targetFolderPath = 'G:\\耳部CT数据集\\LabelDicom_CG'

for patientFolderName in os.listdir(originalFolderPath):
    subFolderPath = os.path.normpath(os.path.join(originalFolderPath, patientFolderName))
    # 特别注意名字不要重名以免名字拼接造成不必要的麻烦
    targetPatientFolderPath = os.path.normpath(os.path.join(targetFolderPath, patientFolderName))
    
    organFolderPath = os.path.normpath(os.path.join(subFolderPath, organName))
    shutil.copytree(organFolderPath, targetPatientFolderPath)
    # for organFileName in os.listdir(organFolderPath):
    #     organFilePath = os.path.normpath(os.path.join(organFolderPath, organFileName))
    #     targetNiiFilePath = os.path.normpath(os.path.join(targetNiiFolderPath, organFileName))
    #     shutil.copy(organFilePath, targetNiiFilePath)