'''
@Author: 弓照鹏
@LastEditors: 弓照鹏
@Date: 2019-01-16 16:22:38
@LastEditTime: 2019-01-24 17:18:22
@organization: BJUT
生成npy文件
'''

import os
import numpy as np
import pydicom

original_dicom_folder = "G:\\耳部CT数据集\\OriginalDicomCropSymmetry"
label_dicom_folder = "G:\\耳部CT数据集\\标注数据组合后dicom裁剪_64"
two_degree_label_dicom_folder = "G:\耳部CT数据集\LabelDicomCropSymmetry_UnCombine_Split"
output_label_two_degree_folder = "G:\耳部CT数据集\LabelDicomCropSymmetry_UnCombine_Split_npy"
output_original_npy_folder = "G:\\耳部CT数据集\\OriginalDicomCropSymmetryNpy_64"
output_label_npy_folder = "G:\\耳部CT数据集\\label_npy_64"

# 生成原始的dicom图像对应的npy文件，需要注意的是这里的原始dicom图像是裁剪之后的，文件的命名的格式是patient_id.npy
def generateImageNpy():
    for patient_folder_name in os.listdir(original_dicom_folder):
        print(patient_folder_name)
        sub_folder_path = os.path.join(original_dicom_folder, patient_folder_name)
        data = np.zeros((420, 420, 60), dtype = np.float32)
        for dicom_file_name in sorted(os.listdir(sub_folder_path)):
            dicom_file_path = os.path.join(sub_folder_path, dicom_file_name)
            dicom_file = pydicom.read_file(dicom_file_path)
            data[:, :, dicom_file.data_element("InstanceNumber").value-1] = dicom_file.pixel_array
        npy_file_path = os.path.join(output_original_npy_folder, patient_folder_name+".npy")
        np.save(npy_file_path, data)

# 生成标记图像对应的npy文件，需要注意的是这里的原始dicom图像是裁剪之后的，文件的命名的格式是patient_id.npy
def generateLabelNpy():
    for patient_folder_name in os.listdir(label_dicom_folder):
        print(patient_folder_name)
        sub_folder_path = os.path.join(label_dicom_folder, patient_folder_name)
        data = np.zeros((420, 420, 60), dtype = np.float32)
        for dicom_file_name in sorted(os.listdir(sub_folder_path)):
            dicom_file_path = os.path.join(sub_folder_path, dicom_file_name)
            dicom_file = pydicom.read_file(dicom_file_path)
            data[:, :, dicom_file.data_element("InstanceNumber").value-1] = dicom_file.pixel_array
        npy_file_path = os.path.join(output_label_npy_folder, patient_folder_name+".npy")
        np.save(npy_file_path, data)

# 生成标注数据对应的npy文件，标注数据有两层第一层为解剖结构的列表，每个关键解剖结构下面有许多标注数据文件
def generateTwoDegreeLabelNpy():
    for organName in os.listdir(two_degree_label_dicom_folder):
        patient_folder_path = os.path.join(two_degree_label_dicom_folder, organName)
        for patient_folder_name in os.listdir(patient_folder_path):
            print(patient_folder_name)
            sub_folder_path = os.path.join(patient_folder_path, patient_folder_name)
            data = np.zeros((420, 420, 60), dtype = np.float32)
            for dicom_file_name in sorted(os.listdir(sub_folder_path)):
                dicom_file_path = os.path.join(sub_folder_path, dicom_file_name)
                dicom_file = pydicom.read_file(dicom_file_path)
                data[:, :, dicom_file.data_element("InstanceNumber").value-1] = dicom_file.pixel_array
            npy_folder_path = os.path.join(output_label_two_degree_folder, organName)
            if not os.path.exists(npy_folder_path):
                os.mkdir(npy_folder_path)
            npy_file_path = os.path.join(npy_folder_path, patient_folder_name+".npy")
            np.save(npy_file_path, data)

if __name__ == "__main__":
    generateImageNpy()