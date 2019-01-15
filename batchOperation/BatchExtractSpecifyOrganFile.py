#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
# 从已经处理好的nii文件中批量提取特定组织器官的文件
# Author: Gong Zhaopeng
# Date:   2018/7/3 21:36
import os
import shutil


organName = 'WBGG'
# 原始的nii文件夹路径
originalNiiFolderPath = 'E:\\桌面文件夹\\64例标注数据裁剪后nii'
# 目标的要写入的文件夹的路径
targetNiiFolderPath = 'E:\\桌面文件夹\\64例WBGG-nii'

for patientFolderName in os.listdir(originalNiiFolderPath):
    subFolderPath = os.path.normpath(os.path.join(originalNiiFolderPath, patientFolderName))
    targetFolderPath = os.path.normpath(os.path.join(targetNiiFolderPath, patientFolderName, organName))
    # if(~os.path.exists(targetNiiFolderPath)):
    #     os.makedirs(targetNiiFolderPath)
    organFolderPath = os.path.normpath(os.path.join(subFolderPath, organName))
    shutil.copytree(organFolderPath, targetFolderPath)
    # for organFileName in os.listdir(organFolderPath):
    #     organFilePath = os.path.normpath(os.path.join(organFolderPath, organFileName))
    #     targetNiiFilePath = os.path.normpath(os.path.join(targetNiiFolderPath, organFileName))
    #     shutil.copy(organFilePath, targetNiiFilePath)