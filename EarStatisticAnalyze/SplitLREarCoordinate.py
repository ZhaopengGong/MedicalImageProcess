#!/usr/bin/env python2.7
# -*- coding:utf-8 -*- 
# Author: Gong Zhaopeng
# Date:   2018/7/1 15:28

import os
import pydicom
import xlsxwriter

dicomFolderPath = 'E:\\桌面文件夹\\original_dicom'
maskFolderPath = 'F:\\DeepLearing\\data\\友谊64例标注数据DICOM'
split_ear_path = 'F:\\DeepLearing\\data\\20180701统计坐标\\split_ear_coordinate'

for patientFolderName in os.listdir(maskFolderPath):
    subFolderPath = os.path.normpath(os.path.join(maskFolderPath, patientFolderName))
    for organFolderName in os.listdir(subFolderPath):
        print("正在处理-", patientFolderName, '-', organFolderName)
        subOrganFolderPath = os.path.normpath(os.path.join(subFolderPath, organFolderName))
        # 要写入的文件的路径
        split_ear_file_path = os.path.join(split_ear_path, patientFolderName, organFolderName + '.xlsx')
        # 写入文件的路径
        workbook = xlsxwriter.Workbook(split_ear_file_path)
        worksheet = workbook.add_worksheet()
        # 左侧，右侧的行号
        left_row_number = 0
        right_row_number = 0
        worksheet.write(0, 0, "left_x")
        worksheet.write(0, 1, "left_y")
        worksheet.write(0, 2, "left_z")
        worksheet.write(0, 3, "left_HF")
        worksheet.write(0, 4, "right_x")
        worksheet.write(0, 5, "right_y")
        worksheet.write(0, 6, "right_z")
        worksheet.write(0, 7, "right_HF")
        for organFileName in os.listdir(subOrganFolderPath):
            # 遍历每个解剖结构下面的每个标注数据文件
            originalDicomPath = os.path.normpath(os.path.join(dicomFolderPath, patientFolderName, organFileName))
            maskFilePath = os.path.normpath(os.path.join(subFolderPath, organFolderName, organFileName))
            maskDicomFile = pydicom.read_file(maskFilePath)
            # 读取矩阵的数组
            maskDicomArray = maskDicomFile.pixel_array
            # 如果mask中的不全为0则读取相应的原始的dicom文件提取出胡氏值
            if(len(maskDicomArray.nonzero()[0])>0):
                originalDicomFile = pydicom.dcmread(originalDicomPath)
                # 读取原始的dicom数据的数组
                orignalDicomFileArray = originalDicomFile.pixel_array
                for height in range(maskDicomArray.shape[0]):
                    # 为了跳过大黑边
                    if(len(maskDicomArray[height,:].nonzero()[0])>0):
                        for width in range(maskDicomArray.shape[1]):
                            if(maskDicomArray[height, width] > 0):
                                # 判断是属于坐标还是右边
                                if(width < maskDicomArray.shape[1]/2):
                                    left_row_number += 1
                                    worksheet.write(left_row_number, 0, float(width))
                                    worksheet.write(left_row_number, 1, float(height))
                                    worksheet.write(left_row_number, 2, int(maskDicomFile.InstanceNumber))
                                    worksheet.write(left_row_number, 3, float(orignalDicomFileArray[height, width])-1024)
                                else:
                                    right_row_number += 1
                                    worksheet.write(right_row_number, 4, float(width))
                                    worksheet.write(right_row_number, 5, float(height))
                                    worksheet.write(right_row_number, 6, int(maskDicomFile.InstanceNumber))
                                    worksheet.write(right_row_number, 7, float(orignalDicomFileArray[height, width])-1024)
        workbook.close()