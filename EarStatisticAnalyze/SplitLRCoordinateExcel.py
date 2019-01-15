# -*- coding: utf-8 -*-
# xlrd xlsxwriter
# @Author gzp
# @Date 2018年5月22日
# @Description 本程序是将已经转换完的坐标左耳和右耳的坐标分开

import csv
import xlrd
import xlsxwriter
import os
# 保存的csv文件的文件夹
csv_folder_path = 'F:\\DeepLearing\\data\\all_data'
# 需要保存xlsx的文件夹
split_ear_path = 'F:\\DeepLearing\\data\\split_ear_coordinate'
# 保存每个病人的校准后数据分辨率的excel表格
resolution_path = 'F:\\DeepLearing\\data\\66例分辨率.xlsx'

# 打开分辨率文件
resolution_file = xlrd.open_workbook(resolution_path)
# 获取到第一个sheet
sheet = resolution_file.sheets()[0]
# 统计第一个sheet中有多少行多少列
row_count = sheet.nrows
col_count = sheet.ncols

for patient_folder_name in os.listdir(csv_folder_path):
    # 在输出文件夹中创建一个相同的文件夹
    patient_folder_out_path = os.path.join(split_ear_path, patient_folder_name)
    os.mkdir(patient_folder_out_path)
    # 遍历分辨率文件夹中的每一行
    for elements in range(row_count):
        # 查询文件夹中的目录所对应分辨率文件中的行
        if patient_folder_name in sheet.row_values(elements):
            middle_col = int(sheet.row_values(elements)[3])/2
            # 进入到每个病人的文件夹下面，文件下面有不同的解剖结构的坐标数据是csv
            sub_folder_dir = os.path.join(csv_folder_path, patient_folder_name)
            # 遍历每一个标注文件
            for csv_file_name in os.listdir(sub_folder_dir):
                print("正在处理"+patient_folder_name+"-"+csv_file_name)
                # 每个关键解剖结构的文件名字
                csv_file_path = os.path.join(sub_folder_dir, csv_file_name)
                # 当前左右耳写入行的索引,第一行已经跳过
                current_left_ear_row_index = 1
                current_right_ear_row_index = 1
                # 打开csv文件
                csv_file = open(csv_file_path, 'r')
                # 要写入的文件的路径
                split_ear_file_path = os.path.join(split_ear_path, patient_folder_name, csv_file_name.split('.')[0]+'.xlsx')
                reader = csv.reader(csv_file)
                # 写入文件的路径
                workbook = xlsxwriter.Workbook(split_ear_file_path)
                worksheet = workbook.add_worksheet()
                worksheet.write(0, 0, "left_x")
                worksheet.write(0, 1, "left_y")
                worksheet.write(0, 2, "left_z")
                worksheet.write(0, 3, "left_HF")
                worksheet.write(0, 4, "right_x")
                worksheet.write(0, 5, "right_y")
                worksheet.write(0, 6, "right_z")
                worksheet.write(0, 7, "right_HF")

                for line in reader:
                    if(float(line[0]) < middle_col):
                        worksheet.write(current_left_ear_row_index, 0, float(line[0]))
                        worksheet.write(current_left_ear_row_index, 1, float(line[1]))
                        worksheet.write(current_left_ear_row_index, 2, float(line[2]))
                        worksheet.write(current_left_ear_row_index, 3, float(line[3]))
                    else:
                        worksheet.write(current_right_ear_row_index, 4, float(line[0]))
                        worksheet.write(current_right_ear_row_index, 5, float(line[1]))
                        worksheet.write(current_right_ear_row_index, 6, float(line[2]))
                        worksheet.write(current_right_ear_row_index, 7, float(line[3]))

                csv_file.close()
                workbook.close()
            break