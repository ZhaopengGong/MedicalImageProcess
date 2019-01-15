'''
@Author: 弓照鹏
@LastEditors: 弓照鹏
@Date: 2018-12-29 14:32:31
@LastEditTime: 2018-12-29 15:11:20
@organization: BJUT
主要将标注数据叠加在原始的图像上用不同的颜色显示出来
'''

import os
import numpy as np
from skimage import io,data


original_label_folder = 'D:/workspace/MedicalImageWorkspace/FCN-BoundingBox/groundtruth'
output_folder = 'D:/workspace/MedicalImageWorkspace/FCN-BoundingBox/label_colorful'
original_dicom_npy_folder = 'D:/workspace/MedicalImageWorkspace/FCN-BoundingBox/original_npy'


def getColorByIndex(i):
    if i==1:
        return (255, 191, 0)
    elif i==2:
        return (0, 100, 0)
    elif i==3:
        return (92, 92, 205)
    elif i==4:
        return (147, 20, 255)
    elif i==5:
        return (0, 0, 139)
    elif i==6:
        return (0, 255, 255)
    elif i==7:
        return (0, 165, 255)
    elif i==8:
        return (0, 69, 255)
    elif i==9:
        return (64, 64, 255)
    elif i==10:
        return (186, 231, 186)
    elif i==11:
        return (180, 238, 180)

for fileName in os.listdir(original_label_folder):
    if fileName != '0003.npy':
        continue
    original_label_path = os.path.normpath(os.path.join(original_label_folder, fileName))
    original_dicom_npy_path = os.path.normpath(os.path.join(original_dicom_npy_folder,fileName))

    original_label_file = np.load(original_label_path)
    original_dicom_npy_file = np.load(original_dicom_npy_path)
    # seg_result_file = seg_result_file['volume']

    for plane in ['Z']:
        # 1为冠状位 2为矢状位 3为轴位
        if 'X' == plane:
            view_orientation = 1
        elif 'Y' == plane:
            view_orientation = 2
        elif 'Z' == plane:
            view_orientation = 3
        output_folder_path = os.path.normpath(
            os.path.join(output_folder, plane, str.zfill((fileName.split('.')[0]), 2)))
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)
            # 冠状位或者是矢状位
        if (view_orientation == 1 or view_orientation == 2):
            height = 60
            width = 420
            pic_num = 420
            # 轴位
        elif (view_orientation == 3):
            height = 420
            width = 420
            pic_num = 60
        is_start = 0
        for pic_index in range(pic_num):
            if(view_orientation == 1):
                image_2d = original_dicom_npy_file[pic_index, :, :]
            elif(view_orientation == 2):
                image_2d = original_dicom_npy_file[:, pic_index, :]
            elif(view_orientation == 3):
                image_2d = original_dicom_npy_file[:, :, pic_index]
            if(image_2d.max()):
                image_2d_scaled = ((np.maximum(image_2d, 0) + 0.1)/ image_2d.max()) * 255.0
            else:
                image_2d_scaled = image_2d
            # image_2d_scaled = np.uint8(image_2d_scaled)
            new_image = np.zeros((height, width, 3), dtype=np.uint8)
            is_save_pic = 0
            is_save_original = 0
            for row in range(height):
                for col in range(width):
                    if (view_orientation == 1):
                        original_label_value = original_label_file[pic_index, col, row]
                        original_dicom_value = image_2d_scaled[col, row]
                    elif (view_orientation == 2):
                        original_label_value = original_label_file[col, pic_index, row]
                        original_dicom_value = image_2d_scaled[col, row]
                    elif (view_orientation == 3):
                        original_label_value = original_label_file[row, col, pic_index]
                        original_dicom_value = image_2d_scaled[row, col]
                    
                    if original_label_value == 1:
                        new_image[row, col] = getColorByIndex(1)
                    elif original_label_value == 2:
                        new_image[row, col] = getColorByIndex(2)
                    elif original_label_value == 3:
                        new_image[row, col] = getColorByIndex(3)
                    elif original_label_value == 4:
                        new_image[row, col] = getColorByIndex(4)
                    elif original_label_value == 5:
                        new_image[row, col] = getColorByIndex(5)
                    elif original_label_value == 6:
                        new_image[row, col] = getColorByIndex(6)
                    elif original_label_value == 7:
                        new_image[row, col] = getColorByIndex(7)
                    elif original_label_value == 8:
                        new_image[row, col] = getColorByIndex(8)
                    elif original_label_value == 9:
                        new_image[row, col] = getColorByIndex(9)
                    elif original_label_value == 10:
                        new_image[row, col] = getColorByIndex(10)
                    elif original_label_value == 11:
                        new_image[row, col] = getColorByIndex(11)
                    else:
                        new_image[row, col, 0] = original_dicom_value
                        new_image[row, col, 1] = original_dicom_value
                        new_image[row, col, 2] = original_dicom_value           
            output_file_path = os.path.join(output_folder_path, str.zfill(str(pic_index + 1), 4) + '.jpg')
            io.imsave(output_file_path, new_image)
