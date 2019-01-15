# -*- coding: utf-8 -*-
# 将dicom文件按照InstanceNumber命名

import os
import glob
import pydicom
# 是否是标记的dicom文件
isLabelDicom  = 1
# 文件夹层级
folder_degree = 0
# dicom 文件夹路径
dicom_root_folder_path = "F:\\DeepLearing\\data\\鼓室标注区域测试"


def renameDicom(parentFolderPath):
    for dicom_file_name in os.listdir(parentFolderPath):
        dicom_file_path = os.path.join(parentFolderPath, dicom_file_name)
        dicom_file = pydicom.dcmread(dicom_file_path)
        if (isLabelDicom):
            dicom_file.InstanceNumber = str(int(60 - int(dicom_file.InstanceNumber)))
            dicom_file.save_as(os.path.join(parentFolderPath, str.zfill(str(int(dicom_file.InstanceNumber)), 6) + ".dcm"))
            os.remove(dicom_file_path)
        else:
            os.rename(dicom_file_path,
                      os.path.join(parentFolderPath, str.zfill(str(dicom_file.InstanceNumber), 6) + ".dcm"))


total_folder_number = len(os.listdir(dicom_root_folder_path))
patient_folder_index = 0
for patient_folder in os.listdir(dicom_root_folder_path):
    patient_folder_index += 1
    print("正在rename"+patient_folder+" "+str(patient_folder_index)+"/"+str(total_folder_number))
    if(folder_degree == 1):
        renameDicom(os.path.join(dicom_root_folder_path, patient_folder))
    elif(folder_degree == 0):
        renameDicom(dicom_root_folder_path)
        break;
    else:
        subFolderPath = os.path.join(dicom_root_folder_path, patient_folder)
        for organName in os.listdir(subFolderPath):
            renameDicom(os.path.join(subFolderPath, organName))
