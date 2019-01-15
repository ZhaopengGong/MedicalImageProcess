#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
# 批量的剪切文件,主要的目的是从子目录提升到父目录中
# Author: Gong Zhaopeng
# Date:   2018/7/1 10:32

import os
import shutil

folderPath = 'F:/DeepLearing/data/66例校准后的CT原始数据'

for patientFolder in os.listdir(folderPath):
    subFolderPath = os.path.normpath(os.path.join(folderPath, patientFolder, 'ST0', 'SE1'))
    targetFolderPath = os.path.normpath(os.path.join(folderPath, patientFolder))
    delete_folder_path = os.path.normpath(os.path.join(folderPath, patientFolder, 'ST0'))
    # 要删除的目录文件路径，原来包含了文件，当文件被剪切掉时将其删除掉
    for patientFile in os.listdir(subFolderPath):
        originalFilePath = os.path.normpath(os.path.join(subFolderPath, patientFile))
        targetFilePath = os.path.normpath(os.path.join(targetFolderPath, patientFile))
        shutil.move(originalFilePath, targetFilePath)
    # 每次命名完成一次即将父目录删除掉
    shutil.rmtree(delete_folder_path)


