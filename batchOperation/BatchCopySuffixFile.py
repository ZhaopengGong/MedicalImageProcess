#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
# 复制指定后缀名的文件
# Author: Gong Zhaopeng
# Date:   2018/7/1 14:16
import os
import shutil

originalFolderPath = 'E:\\桌面文件夹\\64例标注数据裁剪后nii'
targetFolderPath = 'F:\\DeepLearing\\data\\64例裁剪后标注数据QT-nii'

for folderName in os.listdir(originalFolderPath):
    subFolderPath = os.path.normpath(os.path.join(originalFolderPath, folderName))
    for organName in os.listdir(subFolderPath):
        organFolderPath = os.path.normpath(os.path.join(subFolderPath, organName))
        for fileName in os.listdir(organFolderPath):
            if '.nii.gz' in fileName and organName == 'QT':
                originalFilePath = os.path.normpath(os.path.join(organFolderPath, fileName))
                targetFilePath = os.path.normpath(os.path.join(targetFolderPath, folderName, fileName))
                shutil.copy(originalFilePath, targetFilePath)