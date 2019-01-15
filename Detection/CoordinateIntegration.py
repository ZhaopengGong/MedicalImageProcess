'''
@Author: 弓照鹏
@LastEditors: 弓照鹏
@Date: 2018-12-01 15:23:59
@LastEditTime: 2018-12-02 09:25:50
@organization: BJUT
'''
# -*- coding: utf-8 -*-
# xlrd xlsxwriter
# @Author gzp
# @Date 2018年5月22日
# @Description 本程序是将所有的左耳和右耳的坐标合并在一个表中
import os
import xlsxwriter
import xlrd


def getOrganName(i):
    if i==1:
        return "CG"
    elif i==2:
        return "ZG"
    elif i==3:
        return "DG"
    elif i==4:
        return "EW1"
    elif i==5:
        return "EW2"
    elif i==6:
        return "WBGG"
    elif i==7:
        return "HBGG"
    elif i==8:
        return "QBGG"
    elif i==9:
        return "JJMQW"
    elif i==10:
        return "QT"
    elif i==11:
        return "NTD"

# 已经按照解剖结构统计好的左侧和右侧xmls表格
merge_coordinate_folder_path = 'D:\\workspace\\MedicalImageWorkspace\\20181202统计坐标\\merge_ear_coordinate'
# 将合并的坐标数据写入的文件夹
integration_coordinate_folder_path = 'D:\\workspace\MedicalImageWorkspace\\20181202统计坐标\\CoordinateIntegration'

# 创建整合后的文件
integration_coordinate_file_path = os.path.join(integration_coordinate_folder_path,"earIntegration.xlsx")
workbook = xlsxwriter.Workbook(integration_coordinate_file_path)
worksheet = workbook.add_worksheet()
# 向文件的第一行写入数据
col_index = 0
for index in range(1,12):
    for sub_index in range(6):
        if sub_index == 0:
            mystr = getOrganName(index)+"_L_X"
        elif sub_index == 1:
            mystr = getOrganName(index)+"_L_Y"
        elif sub_index == 2:
            mystr = getOrganName(index)+"_L_Z"
        elif sub_index == 3:
            mystr = getOrganName(index)+"_R_X"
        elif sub_index == 4:
            mystr = getOrganName(index)+"_R_Y"
        elif sub_index == 5:
            mystr = getOrganName(index)+"_R_Z"
        worksheet.write(0, col_index+sub_index, mystr)
    col_index += 6
organ_index = 0
for iterator_organ_index in range(1, 12):
    # 已经分割好的组织器官的坐标数据
    organ_file_path = os.path.join(merge_coordinate_folder_path, getOrganName(iterator_organ_index)+".xlsx")
    # 已经分开的xlsx文件
    xlsx_file = xlrd.open_workbook(organ_file_path)
    # 获取到第一个sheet
    sheet = xlsx_file.sheets()[0]
    # 统计第一个sheet中有多少行
    row_count = sheet.nrows
    # 当前的写入的行的索引
    current_left_row_index = 1
    current_right_row_index = 1
    # 遍历分辨率文件夹中的每一行
    for elements in range(2, row_count):
        for patient_index in range(64):
            row = sheet.row_values(elements)
            if row[0+patient_index*10] != '':
                worksheet.write(current_left_row_index, 0 + organ_index, float(row[0+patient_index*10]))
                worksheet.write(current_left_row_index, 1 + organ_index, float(row[1+patient_index*10]))
                worksheet.write(current_left_row_index, 2 + organ_index, float(row[2+patient_index*10]))
                current_left_row_index += 1
            if row[5+patient_index*10] != '':
                worksheet.write(current_right_row_index, 3 + organ_index, float(row[5+patient_index*10]))
                worksheet.write(current_right_row_index, 4 + organ_index, float(row[6+patient_index*10]))
                worksheet.write(current_right_row_index, 5 + organ_index, float(row[7+patient_index*10]))
                current_right_row_index +=1
    organ_index += 6
workbook.close()

