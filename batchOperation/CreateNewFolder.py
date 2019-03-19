# -*- coding: utf-8 -*-
# 在另外一个文件夹下面创建与当前文件夹相同的目录结构(只创建一级目录结构)
import os
import glob

original_folder_path = "H:\\耳部CT数据集\\WED81例标注数据MIMIC"
target_folder_path = "H:\\耳部CT数据集\\WED81例标注数据导出后"

for patient_folder in os.listdir(original_folder_path):
    created_folder_path = os.path.join(target_folder_path, patient_folder.split('.')[0])
    os.makedirs(created_folder_path)