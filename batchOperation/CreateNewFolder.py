# -*- coding: utf-8 -*-
# 在另外一个文件夹下面创建与当前文件夹相同的目录结构(只创建一级目录结构)
import os
import glob

original_folder_path = "F:\\DeepLearing\\data\\友谊64例标注数据MIMIC"
target_folder_path = "F:\\DeepLearing\\data\\64例裁剪后标注数据QT-nii"

for patient_folder in os.listdir(original_folder_path):
    created_folder_path = os.path.join(target_folder_path, patient_folder)
    os.makedirs(created_folder_path)