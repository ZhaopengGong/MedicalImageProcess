import os
import numpy as np
from skimage import io,data

seg_fine_result_folder = 'F:/DeepLearing/data/测试的结果/WBGG精准分割结果'
original_label_folder = 'F:/DeepLearing/data/测试的结果/WBGG标注数据'
output_folder = 'F:/DeepLearing/data/测试的结果/WBGG精准分割可视化'

for fileName in os.listdir(seg_fine_result_folder):
    seg_fine_result_filePath = os.path.normpath(os.path.join(seg_fine_result_folder, fileName))
    original_label_path = os.path.normpath(os.path.join(original_label_folder, str.zfill((fileName.split('.')[0]).split('_')[1], 4) + '.npy'))

    original_label_file = np.load(original_label_path)
    seg_result_file = np.load(seg_fine_result_filePath)
    seg_result_file = seg_result_file['volume']

    for plane in ['X', 'Y', 'Z']:
        # 1为冠状位 2为矢状位 3为轴位
        if 'X' == plane:
            view_orientation = 1
        elif 'Y' == plane:
            view_orientation = 2
        elif 'Z' == plane:
            view_orientation = 3
        output_folder_path = os.path.normpath(
            os.path.join(output_folder, plane, str.zfill((fileName.split('.')[0]).split('_')[1], 2)))
        if (~os.path.exists(output_folder_path)):
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
        for pic_index in range(pic_num):
            new_image = np.zeros((height, width, 3), dtype=np.uint8)
            is_save_pic = 0
            for row in range(height):
                for col in range(width):
                    if (view_orientation == 1):
                        original_label_value = original_label_file[pic_index, col, row]
                        seg_result_value = seg_result_file[pic_index, col, row]
                    elif (view_orientation == 2):
                        original_label_value = original_label_file[col, pic_index, row]
                        seg_result_value = seg_result_file[col, pic_index, row]
                    elif (view_orientation == 3):
                        seg_result_value = seg_result_file[row, col, pic_index]
                        original_label_value = original_label_file[row, col, pic_index]
                    if (original_label_value == 0 and seg_result_value == 0):
                        new_image[row, col, 0] = 0
                        new_image[row, col, 1] = 0
                        new_image[row, col, 2] = 0
                    elif (original_label_value > 0 and seg_result_value > 0):
                        new_image[row, col, 0] = 255
                        new_image[row, col, 1] = 255
                        new_image[row, col, 2] = 0
                        is_save_pic = 1
                    elif (original_label_value > 0 and seg_result_value == 0):
                        new_image[row, col, 0] = 0
                        new_image[row, col, 1] = 255
                        new_image[row, col, 2] = 0
                        is_save_pic = 1
                    elif (original_label_value == 0 and seg_result_value > 0):
                        new_image[row, col, 0] = 255
                        new_image[row, col, 1] = 0
                        new_image[row, col, 2] = 0
                        is_save_pic = 1
            if (is_save_pic):
                output_file_path = os.path.join(output_folder_path, str.zfill(str(pic_index + 1), 4) + '.jpg')
                io.imsave(output_file_path, new_image)
