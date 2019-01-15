# -*- coding: utf-8 -*-
# 将标注数据的dicom文件重命名将instancenumber修改

import os
import pydicom
import numpy as np

dicom_root_folder_path = "E:/桌面文件夹/Test1"
for patient_folder in os.listdir(dicom_root_folder_path):
    print("正在rename" + patient_folder)
    sub_folder_path = os.path.join(dicom_root_folder_path, patient_folder)
    for dicom_file_name in os.listdir(sub_folder_path):
        dicom_file_path = os.path.join(sub_folder_path, dicom_file_name)
        dicom_file = pydicom.dcmread(dicom_file_path)
        dicom_file.InstanceNumber = str(int(60 - int(dicom_file.InstanceNumber)))
        dicom_file.save_as(os.path.join(sub_folder_path, str.zfill(str(int(dicom_file.InstanceNumber)), 4)+".dcm"))
        os.remove(dicom_file_path)