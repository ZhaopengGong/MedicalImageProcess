# -*- coding: utf-8 -*-
# xlrd xlsxwriter
# @Author gzp
# @Date 2018年5月24日
# @Description 计算坐标的均值
import os
import xlsxwriter
import xlrd

# 已经转换好的左耳和右耳的坐标数据
split_ear_coordinate_folder_path = 'F:\\DeepLearing\\data\\20180701统计坐标\\split_ear_coordinate'
# 将合并的坐标数据写入的文件夹
average_coordinate_folder_path = 'F:\\DeepLearing\\data\\20180701统计坐标\\average_ear_coordinate'

ear_organ_average_file_name = ''
organ_hf_file_name = ''
ear_organ_average_file_name = 'EW2_Average.xlsx'
organ_hf_file_name = 'EW2.xlsx'
# 创建合并的文件
ear_organ_average_file_path = os.path.join(average_coordinate_folder_path, ear_organ_average_file_name)
workbook = xlsxwriter.Workbook(ear_organ_average_file_path)
worksheet = workbook.add_worksheet()
# 将文件的第一行和第二行写入数据
worksheet.write(0, 0, 'ID')
worksheet.write(0, 1, '左x平均值')
worksheet.write(0, 2, '左y平均值')
worksheet.write(0, 3, '左z平均值')
worksheet.write(0, 4, '总个数(左)')
worksheet.write(0, 5, '右x平均值')
worksheet.write(0, 6, '右y平均值')
worksheet.write(0, 7, '右z平均值')
worksheet.write(0, 8, '总个数(右)')
print("Current is processing" + ear_organ_average_file_name)
patient_index = 0
for patient_folder_name in os.listdir(split_ear_coordinate_folder_path):

    patient_index += 1
    # 定义统计坐标的各个变量的值
    left_ear_num = 0
    left_ear_x_averge = 0
    left_ear_y_averge = 0
    left_ear_z_averge = 0
    right_ear_num = 0
    right_ear_x_averge = 0
    right_ear_y_averge = 0
    right_ear_z_averge = 0

    # 拼接出文件的路径
    organ_file_path = os.path.join(split_ear_coordinate_folder_path, patient_folder_name, organ_hf_file_name)
    if os.path.exists(organ_file_path):
        # 已经分开的xlsx文件
        xlsx_file = xlrd.open_workbook(organ_file_path)
        # 获取到第一个sheet
        sheet = xlsx_file.sheets()[0]
        # 统计第一个sheet中有多少行
        row_count = sheet.nrows
        # 遍历分辨率文件夹中的每一行
        for elements in range(row_count):
            if elements != 0:
                row = sheet.row_values(elements)
                if row[0] != '':
                    left_ear_x_averge += float(row[0])
                    left_ear_y_averge += float(row[1])
                    left_ear_z_averge += float(row[2])
                    left_ear_num += 1
                if row[4] != '':
                    right_ear_x_averge += float(row[4])
                    right_ear_y_averge += float(row[5])
                    right_ear_z_averge += float(row[6])
                    right_ear_num += 1
    if left_ear_num != 0:
        left_ear_x_averge = left_ear_x_averge / left_ear_num
        left_ear_y_averge = left_ear_y_averge / left_ear_num
        left_ear_z_averge = left_ear_z_averge / left_ear_num

    if right_ear_num != 0:
        right_ear_x_averge = right_ear_x_averge / right_ear_num
        right_ear_y_averge = right_ear_y_averge / right_ear_num
        right_ear_z_averge = right_ear_z_averge / right_ear_num

    worksheet.write(patient_index, 0, patient_folder_name)
    worksheet.write(patient_index, 1, left_ear_x_averge)
    worksheet.write(patient_index, 2, left_ear_y_averge)
    worksheet.write(patient_index, 3, left_ear_z_averge)
    worksheet.write(patient_index, 4, left_ear_num)
    worksheet.write(patient_index, 5, right_ear_x_averge)
    worksheet.write(patient_index, 6, right_ear_y_averge)
    worksheet.write(patient_index, 7, right_ear_z_averge)
    worksheet.write(patient_index, 8, right_ear_num)
workbook.close()

