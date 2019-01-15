#!/usr/bin/env python2.7
# -*- coding:utf-8 -*- 
# Author: Gong Zhaopeng
# 统计出校准后数据的坐标基本信息，包含分辨率和像素间距，层厚
# Date:   2018/7/1 11:52
import os
import pydicom
import xlsxwriter

generateDicominfoFilePath = 'F:\\DeepLearing\\data\\64例dicom信息统计.xlsx'
dicomFolderPath = 'E:/桌面文件夹/original_dicom'
# 当前的行号
current_row_index = 0
# 写入文件的路径
workbook = xlsxwriter.Workbook(generateDicominfoFilePath)
worksheet = workbook.add_worksheet()
worksheet.write(current_row_index, 0, "id")
worksheet.write(current_row_index, 1, "row")
worksheet.write(current_row_index, 2, "columns")
worksheet.write(current_row_index, 3, "pixelSpacing")
worksheet.write(current_row_index, 4, "SliceThickness")

for patient_folder_name in os.listdir(dicomFolderPath):
    subFolderPath = os.path.normpath(os.path.join(dicomFolderPath, patient_folder_name))
    dicomFilePath = os.path.normpath(os.path.join(subFolderPath, '000001.dcm'))
    # 读取dicom文件
    dicomFile = pydicom.read_file(dicomFilePath)
    current_row_index += 1
    worksheet.write(current_row_index, 0, patient_folder_name)
    worksheet.write(current_row_index, 1, dicomFile.Rows)
    worksheet.write(current_row_index, 2, dicomFile.Columns)
    worksheet.write(current_row_index, 3, dicomFile.PixelSpacing[0])
    worksheet.write(current_row_index, 4, dicomFile.SliceThickness)
workbook.close()
