'''
@Author: 弓照鹏
@LastEditors: 弓照鹏
@Date: 2018-12-10 18:40:22
@LastEditTime: 2019-01-04 10:37:35
@organization: BJUT
'''

import os
import imageio

# visual_result_folder_path = 'D:\\workspace\\MedicalImageWorkspace\\FCN-BoundingBox\\visual_result'
# save_gif_path = 'D:\\workspace\\MedicalImageWorkspace\\FCN-BoundingBox\\visual_result\\gif'
# folder_list = os.listdir(visual_result_folder_path)
# for folder_name in folder_list:
#     sub_folder_path = os.path.join(visual_result_folder_path, folder_name)
#     imagelist = os.listdir(sub_folder_path)
#     frames = []
#     for image_file in imagelist:
#         image_file_path = os.path.join(sub_folder_path, image_file)
#         frames.append(imageio.imread(image_file_path))
#     save_path = os.path.join(save_gif_path, folder_name+".gif")
#     imageio.mimsave(save_path, frames, 'GIF', duration = 0.3)

image_folder_path = 'D:/workspace/MedicalImageWorkspace/FCN-BoundingBox/visual_result/gif_source'
output_folder_path = 'D:/workspace/MedicalImageWorkspace/FCN-BoundingBox/visual_result/gif_generate'
imagelist = os.listdir(image_folder_path)
frames = []
for image_file in imagelist:
        image_file_path = os.path.join(image_folder_path, image_file)
        frames.append(imageio.imread(image_file_path))
save_path = os.path.join(output_folder_path, "kaiti.gif")
imageio.mimsave(save_path, frames, 'GIF', duration = 0.3)