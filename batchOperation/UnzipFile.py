# -*- coding: utf-8 -*-
# zipfile36
# @Author gzp
# @Date 2018年6月05日
# @Description 解压缩文件

import zipfile36
import os

# folder_path = "C:\\Users\\SIPL-gzp\\Desktop\\三例EW2-右侧不全-MIMICS"
# for patient_folder in os.listdir(folder_path):
#     print("正在处理"+patient_folder)
#     sub_folder_path = os.path.join(folder_path, patient_folder)
#     for zip_file_name in os.listdir(sub_folder_path):
#         # 关键解剖结构的文件夹
#         organ_folder_path = os.path.join(sub_folder_path, zip_file_name.split(".")[0])
#         if not os.path.exists(organ_folder_path):
#             os.makedirs(organ_folder_path)
#         if len(os.listdir(organ_folder_path)) == 0:
#             zip_file_path = os.path.join(sub_folder_path, zip_file_name)
#             # 特别注意的就是路径中不允许出现//
#             zip_file_path = zip_file_path.replace("\\", "/")
#             # 判断是不是压缩文件
#             if(zipfile36.is_zipfile(zip_file_path)):
#                 # 将文件路径下面的所有文件全部列出来
#                 zipfile = zipfile36.ZipFile(zip_file_path)
#                 # 遍历包含的文件全部解压
#                 for file in zipfile.namelist():
#                     zipfile.extract(file,  organ_folder_path.replace("\\", "/"))
#                 # 接触解压缩占用
#                 zipfile.close()
#             # 将压缩文件删除掉
#             os.remove(zip_file_path)

folder_path = "H:\\耳部CT数据集\\WED74例标注数据导出后"
for patient_folder in os.listdir(folder_path):
    print("正在处理"+patient_folder)
    sub_folder_path = os.path.join(folder_path, patient_folder)
    for zip_file_name in os.listdir(sub_folder_path):
        zip_file_path = os.path.join(sub_folder_path, zip_file_name)
        # 特别注意的就是路径中不允许出现//
        zip_file_path = zip_file_path.replace("\\", "/")
        # 判断是不是压缩文件
        if(zipfile36.is_zipfile(zip_file_path)):
            # 将文件路径下面的所有文件全部列出来
            zipfile = zipfile36.ZipFile(zip_file_path)
            # 遍历包含的文件全部解压
            for file in zipfile.namelist():
                zipfile.extract(file,  sub_folder_path.replace("\\", "/"))
            # 接触解压缩占用
            zipfile.close()
        # 将压缩文件删除掉
        os.remove(zip_file_path)