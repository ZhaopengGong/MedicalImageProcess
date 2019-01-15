# -*- coding: utf-8 -*-
# xlrd xlsxwriter
# @Author gzp
# @Date 2018年5月22日
# @Description 计算出体积

import csv
import xlrd
import xlsxwriter
import os
import codecs
import pandas as pd

# 标注后的原始文件夹的路径
original_file_path = 'F:\\DeepLearing\\data\\友谊64例标注数据DICOM'
# 计算出的体积文件夹的路径
calculate_volume_path = 'F:\\DeepLearing\\data\\20180701统计坐标\\ear_organ_volume'
# 保存每个病人的校准后数据分辨率的excel表格
st_path = 'F:\\DeepLearing\\data\\64例dicom信息统计.xlsx'
# 之前计算出的解剖结构平均值的文件夹路径
average_data_folder_path = "F:\\DeepLearing\\data\\20180701统计坐标\\average_ear_coordinate"
# 打开分辨率文件
dicom_info_file = xlrd.open_workbook(st_path)
# 获取到第一个sheet
sheet = dicom_info_file.sheets()[0]
# 统计第一个sheet中有多少行多少列
row_count = sheet.nrows
# 创建一个目标的excel文件
volume_path = os.path.join(calculate_volume_path, 'ear_organ_volume.xlsx')
workbook = xlsxwriter.Workbook(volume_path)
worksheet = workbook.add_worksheet()
format = workbook.add_format({'border': 1, 'align': 'center', 'font_size': 12, 'font_color': 'red'})
# 向文件中的第一行写入数据
worksheet.write(0, 0, 'ID')
worksheet.write(0, 1, '锤骨CG')
worksheet.write(0, 2, '砧骨ZG')
worksheet.write(0, 3, '镫骨DG')
worksheet.write(0, 4, '耳蜗EW1')
worksheet.write(0, 5, '耳蜗EW2')
worksheet.write(0, 6, '前庭QT')
worksheet.write(0, 7, '前半规管QBGG')
worksheet.write(0, 8, '后半规管HBGG')
worksheet.write(0, 9, '外半规管WBGG')
worksheet.write(0, 10, '内听道NTD')
worksheet.write(0, 11, '颈静脉球窝JJMQW')
# 当前的病人的索引
patient_index = 1
for patient_folder_name in os.listdir(original_file_path):
    sub_folder_dir = os.path.join(original_file_path, patient_folder_name, 'Axial_Area')
    # 遍历层厚文件夹中的每一行
    for elements in range(row_count):
        # 将id值写入到第一列中
        worksheet.write(patient_index, 0, patient_folder_name)
        # 查询文件夹中的目录所对应分辨率文件中的行
        if patient_folder_name in sheet.row_values(elements):
            slice_thickness = float(sheet.row_values(elements)[4])
            pixelSpacing = float(sheet.row_values(elements)[3])
            for organ_index in range(12):
                if(organ_index > 0):
                    if organ_index == 1:
                        col_index = 1
                        organName = 'CG'
                    elif organ_index == 2:
                        col_index = 2
                        organName = 'ZG'
                    elif organ_index == 3:
                        col_index = 3
                        organName = 'DG'
                    elif organ_index == 4:
                        col_index = 4
                        organName = 'EW1'
                    elif organ_index == 5:
                        col_index = 5
                        organName = 'EW2'
                    elif organ_index == 6:
                        col_index = 6
                        organName = 'QT'
                    elif organ_index == 7:
                        col_index = 7
                        organName = 'QBGG'
                    elif organ_index == 8:
                        col_index = 8
                        organName = 'HBGG'
                    elif organ_index == 9:
                        col_index = 9
                        organName = 'WBGG'
                    elif organ_index == 10:
                        col_index = 10
                        organName = 'NTD'
                    elif organ_index == 11:
                        col_index = 11
                        organName = 'JJMQW'
                    average_file_path = os.path.join(average_data_folder_path,
                                                    organName + '_' + 'Average.xlsx')
                    average_file = xlrd.open_workbook(average_file_path)
                    # 获取到第一个sheet
                    average_sheet = average_file.sheets()[0]
                    # 统计第一个sheet中有多少行多少列
                    average_row_count = average_sheet.nrows
                    # 遍历计算出的平均值文件夹
                    for average_row in range(average_row_count):
                        if patient_folder_name in average_sheet.row_values(average_row):
                            left_point_numbers = float(average_sheet.row_values(average_row)[4])
                            right_point_numbers = float(average_sheet.row_values(average_row)[8])
                            break
                    volume_value = 0
                    area_sum = (left_point_numbers+right_point_numbers)*pixelSpacing*pixelSpacing
                    # 计算体积
                    if slice_thickness == 0.7:
                        volume_value = area_sum * 0.7
                    elif slice_thickness < 0.7:
                        volume_value = area_sum * (slice_thickness + (0.7 - slice_thickness) / 2)
                    elif slice_thickness > 0.7:
                        volume_value = area_sum * (slice_thickness - (slice_thickness - 0.7) * 2)
                    worksheet.write(patient_index, col_index, float(volume_value))
    patient_index += 1
workbook.close()