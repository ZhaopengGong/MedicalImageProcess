# -*- coding: utf-8 -*-
# xlrd xlsxwriter
# @Author gzp
# @Date 2018年6月04日
# @Description 计算出左右耳体积

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
# 之前计算出的解剖结构平均值的文件夹路径
average_data_folder_path = "F:\\DeepLearing\\data\\20180701统计坐标\\average_ear_coordinate"
# 保存每个病人的校准后数据分辨率的excel表格
st_path = 'F:\\DeepLearing\\data\\64例dicom信息统计.xlsx'
# 打开分辨率文件
resolution_file = xlrd.open_workbook(st_path)
# 获取到第一个sheet
sheet = resolution_file.sheets()[0]
# 统计第一个sheet中有多少行多少列
row_count = sheet.nrows
# 创建一个目标的excel文件
volume_path = os.path.join(calculate_volume_path, 'ear_organ_volume_LR.xlsx')
workbook = xlsxwriter.Workbook(volume_path)
worksheet = workbook.add_worksheet()
format = workbook.add_format({'border': 1, 'align': 'center', 'font_size': 12, 'font_color': 'red'})
# 向文件中的第一行写入数据
worksheet.write(0, 0, 'ID')
worksheet.write(0, 1, '锤骨CG左')
worksheet.write(0, 2, '锤骨CG右')
worksheet.write(0, 3, '砧骨ZG左')
worksheet.write(0, 4, '砧骨ZG右')
worksheet.write(0, 5, '镫骨DG左')
worksheet.write(0, 6, '镫骨DG右')
worksheet.write(0, 7, '耳蜗EW1左')
worksheet.write(0, 8, '耳蜗EW1右')
worksheet.write(0, 9, '耳蜗EW2左')
worksheet.write(0, 10, '耳蜗EW2右')
worksheet.write(0, 11, '前庭QT左')
worksheet.write(0, 12, '前庭QT右')
worksheet.write(0, 13, '前半规管QBGG左')
worksheet.write(0, 14, '前半规管QBGG右')
worksheet.write(0, 15, '后半规管HBGG左')
worksheet.write(0, 16, '后半规管HBGG右')
worksheet.write(0, 17, '外半规管WBGG左')
worksheet.write(0, 18, '外半规管WBGG右')
worksheet.write(0, 19, '内听道NTD左')
worksheet.write(0, 20, '内听道NTD右')
worksheet.write(0, 21, '颈静脉球窝JJMQW左')
worksheet.write(0, 22, '颈静脉球窝JJMQW右')
# 当前的病人的索引
patient_index = 1
for patient_folder_name in os.listdir(original_file_path):
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
                        col_index = 3
                        organName = 'ZG'
                    elif organ_index == 3:
                        col_index = 5
                        organName = 'DG'
                    elif organ_index == 4:
                        col_index = 7
                        organName = 'EW1'
                    elif organ_index == 5:
                        col_index = 9
                        organName = 'EW2'
                    elif organ_index == 6:
                        col_index = 11
                        organName = 'QT'
                    elif organ_index == 7:
                        col_index = 13
                        organName = 'QBGG'
                    elif organ_index == 8:
                        col_index = 15
                        organName = 'HBGG'
                    elif organ_index == 9:
                        col_index = 17
                        organName = 'WBGG'
                    elif organ_index == 10:
                        col_index = 19
                        organName = 'NTD'
                    elif organ_index == 11:
                        col_index = 21
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
                    left_area_sum = (left_point_numbers) * pixelSpacing * pixelSpacing
                    right_area_sum = (right_point_numbers) * pixelSpacing * pixelSpacing
                    # 计算体积
                    if slice_thickness == 0.7:
                        left_volume = left_area_sum * 0.7
                        right_volume = right_area_sum * 0.7
                    elif slice_thickness < 0.7:
                        left_volume = left_area_sum * (slice_thickness + (0.7 - slice_thickness) / 2)
                        right_volume = right_area_sum * (slice_thickness + (0.7 - slice_thickness) / 2)
                    elif slice_thickness > 0.7:
                        left_volume = left_area_sum * (slice_thickness - (slice_thickness - 0.7) * 2)
                        right_volume = right_area_sum * (slice_thickness - (slice_thickness - 0.7) * 2)
                    worksheet.write(patient_index, col_index, float(left_volume))
                    worksheet.write(patient_index, col_index + 1, float(right_volume))
    patient_index += 1
workbook.close()