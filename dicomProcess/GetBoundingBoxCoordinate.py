'''
@Author: 弓照鹏
@LastEditors: 弓照鹏
@Date: 2019-01-16 11:40:39
@LastEditTime: 2019-01-17 15:54:00
@organization: BJUT
获取boundingbox的坐标
'''
import os
import numpy as np
import pydicom

# npy_file_path = "G:\\耳部CT数据集\\label_npy_64\\00071536.npy"
# npy_file = np.load(npy_file_path)
# for slice_number in range(60):
#     label_matrix = npy_file[:,:,slice_number]
#     # 求解出矩阵的shape
#     height, width = label_matrix.shape
#     label_matrix_left = label_matrix[:, 0:int(width/2)]
#     label_matrix_left_detect = np.where(label_matrix_left==1)
#     if(label_matrix_left_detect[0].shape[0]!=0):
#         label_matrix_left_rect = [(label_matrix_left_detect[1])[np.argmin(label_matrix_left_detect[1])], (label_matrix_left_detect[0])[np.argmin(label_matrix_left_detect[0])], (label_matrix_left_detect[1])[np.argmax(label_matrix_left_detect[1])], (label_matrix_left_detect[0])[np.argmax(label_matrix_left_detect[0])]]
#         print(label_matrix_left_rect,  slice_number)


dicom_folder_path = "G:\\耳部CT数据集\\LabelDicom_CG\\00144086"
for dicom_filename in os.listdir(dicom_folder_path):
    dicom_file_path = os.path.join(dicom_folder_path, dicom_filename)
    dicomFile = pydicom.read_file(dicom_file_path)
    dicom_npy = np.array(dicomFile.pixel_array)
    height, width = dicom_npy.shape
    label_matrix_left = dicom_npy[:, 0:int(width/2)]
    label_matrix_left_detect = np.where(label_matrix_left==1)
    pixel_spacing = dicomFile.PixelSpacing[0]
    if(label_matrix_left_detect[0].shape[0]!=0):
        pixel_label_matrix_left_rect = [(label_matrix_left_detect[1])[np.argmin(label_matrix_left_detect[1])], (label_matrix_left_detect[0])[np.argmin(label_matrix_left_detect[0])], (label_matrix_left_detect[1])[np.argmax(label_matrix_left_detect[1])], (label_matrix_left_detect[0])[np.argmax(label_matrix_left_detect[0])]]
        # 特别注意一下python中的元素是怎么相乘的
        label_matrix_left_rect = [i * pixel_spacing for i in pixel_label_matrix_left_rect]
        print(label_matrix_left_rect, dicom_filename)