# -*- coding: utf-8 -*-
# xlrd xlsxwriter
# @Author gzp
# @Date 2018年5月22日
# @Description 本程序是将所有的左耳和右耳的坐标合并在一个表中
import os
import xlsxwriter
import xlrd

# 已经转换好的左耳和右耳的坐标数据
split_ear_coordinate_folder_path = 'D:\\workspace\\MedicalImageWorkspace\\20180702统计坐标\\split_ear_coordinate'
# 将合并的坐标数据写入的文件夹
merge_coordinate_folder_path = 'D:\\workspace\\MedicalImageWorkspace\\20180702统计坐标\\merge'

organ_index = 1
for patient_folder_name in os.listdir(split_ear_coordinate_folder_path):
    if(organ_index <= 11):
        organ_file_name = ''
        if organ_index == 1:
            organ_file_name = 'CG.xlsx'
        elif organ_index == 2:
            organ_file_name = 'ZG.xlsx'
        elif organ_index == 3:
            organ_file_name = 'DG.xlsx'
        elif organ_index == 4:
            organ_file_name = 'EW1.xlsx'
        elif organ_index == 5:
            organ_file_name = 'EW2.xlsx'
        elif organ_index == 6:
            organ_file_name = 'NTD.xlsx'
        elif organ_index == 7:
            organ_file_name = 'QBGG.xlsx'
        elif organ_index == 8:
            organ_file_name = 'HBGG.xlsx'
        elif organ_index == 9:
            organ_file_name = 'WBGG.xlsx'
        elif organ_index == 10:
            organ_file_name = 'QT.xlsx'
        elif organ_index == 11:
            organ_file_name = 'JJMQW.xlsx'
        # 创建合并的文件
        merge_ear_file_path = os.path.join(merge_coordinate_folder_path, organ_file_name)
        workbook = xlsxwriter.Workbook(merge_ear_file_path)
        worksheet = workbook.add_worksheet()
        format = workbook.add_format({'border': 1, 'align': 'center', 'font_size': 12, 'font_color': 'red'})
        # 将文件的第一行和第二行写入数据
        col_index = 0
        for folder_name in os.listdir(split_ear_coordinate_folder_path):
            worksheet.merge_range(0, col_index, 0, col_index+9, folder_name, format)
            for sub_index in range(10):
                mystr = ''
                if sub_index == 0:
                    mystr = '左耳X'
                elif sub_index == 1:
                    mystr = '左耳Y'
                elif sub_index == 2:
                    mystr = '左耳Z'
                elif sub_index == 3:
                    mystr = '左耳HF'
                elif sub_index == 4:
                    mystr = '左耳(x,y,z,HF)'
                elif sub_index == 5:
                    mystr = '右耳X'
                elif sub_index == 6:
                    mystr = '右耳Y'
                elif sub_index == 7:
                    mystr = '右耳Z'
                elif sub_index == 8:
                    mystr = '右耳HF'
                elif sub_index == 9:
                    mystr = '右耳(x,y,z,HF)'
                worksheet.write(1, col_index+sub_index, mystr)
            col_index += 10
        col_index = 0
        print("Current is processing"+organ_file_name)
        for patient_folder_name in os.listdir(split_ear_coordinate_folder_path):
            # 拼接出文件的路径
            organ_file_path = os.path.join(split_ear_coordinate_folder_path, patient_folder_name, organ_file_name)
            if os.path.exists(organ_file_path):
                # 已经分开的xlsx文件
                xlsx_file = xlrd.open_workbook(organ_file_path)
                # 获取到第一个sheet
                sheet = xlsx_file.sheets()[0]
                # 统计第一个sheet中有多少行
                row_count = sheet.nrows
                # 当前的写入的行的索引
                current_row_index = 2
                # 遍历分辨率文件夹中的每一行
                for elements in range(row_count):
                    if elements != 0:
                        row = sheet.row_values(elements)
                        if row[0] != '':
                            worksheet.write(current_row_index, 0 + col_index, float(row[0]))
                            worksheet.write(current_row_index, 1 + col_index, float(row[1]))
                            worksheet.write(current_row_index, 2 + col_index, float(row[2]))
                            worksheet.write(current_row_index, 3 + col_index, float(row[3]))
                            worksheet.write(current_row_index, 4 + col_index, '(' + str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ')')
                        if row[4] != '':
                            worksheet.write(current_row_index, 5 + col_index, float(row[4]))
                            worksheet.write(current_row_index, 6 + col_index, float(row[5]))
                            worksheet.write(current_row_index, 7 + col_index, float(row[6]))
                            worksheet.write(current_row_index, 8 + col_index, float(row[7]))
                            worksheet.write(current_row_index, 9 + col_index, '(' + str(row[4]) + ',' + str(row[5]) + ',' + str(row[6]) + ')')
                        current_row_index += 1
                col_index += 10
            else:
                col_index += 10
        workbook.close()
    organ_index += 1

