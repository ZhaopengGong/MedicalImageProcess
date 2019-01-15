# -*- coding:utf-8 -*- 

import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns
import xlsxwriter

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


def printMinMaxValue():
    excel_path = "D:\\workspace\\MedicalImageWorkspace\\20181202统计坐标\\CoordinateIntegration\\earIntegration.xlsx"
    min_max_excel_path = "D:\\workspace\\MedicalImageWorkspace\\20181202统计坐标\\CoordinateIntegration\\min_max.xlsx"
    data = pd.read_excel(excel_path, 'Sheet1')
    workbook = xlsxwriter.Workbook(min_max_excel_path)
    worksheet = workbook.add_worksheet() 
    worksheet.write(0, 1, 'min_L_X')
    worksheet.write(0, 2, 'max_L_X')
    worksheet.write(0, 3, 'min_L_Y')
    worksheet.write(0, 4, 'max_L_Y')
    worksheet.write(0, 5, 'min_L_Z')
    worksheet.write(0, 6, 'max_L_Z')
    worksheet.write(0, 7, 'min_R_X')
    worksheet.write(0, 8, 'max_R_X')
    worksheet.write(0, 9, 'min_R_Y')
    worksheet.write(0, 10, 'max_R_Y')
    worksheet.write(0, 11, 'min_R_Z')
    worksheet.write(0, 12, 'max_R_Z')
    for organ_index in range(1, 12):
        L_X = data[getOrganName(organ_index)+'_L_X']
        L_Y = data[getOrganName(organ_index)+'_L_Y']
        L_Z = data[getOrganName(organ_index)+'_L_Z']
        R_X = data[getOrganName(organ_index)+'_R_X']
        R_Y = data[getOrganName(organ_index)+'_R_Y']
        R_Z = data[getOrganName(organ_index)+'_R_Z']
        worksheet.write(organ_index, 0, getOrganName(organ_index))
        worksheet.write(organ_index, 1, int(min(L_X)))
        worksheet.write(organ_index, 2, int(max(L_X)))
        worksheet.write(organ_index, 3, int(min(L_Y)))
        worksheet.write(organ_index, 4, int(max(L_Y)))
        worksheet.write(organ_index, 5, int(min(L_Z)))
        worksheet.write(organ_index, 6, int(max(L_Z)))
        worksheet.write(organ_index, 7, int(min(R_X)))
        worksheet.write(organ_index, 8, int(max(R_X)))
        worksheet.write(organ_index, 9, int(min(R_Y)))
        worksheet.write(organ_index, 10, int(max(R_Y)))
        worksheet.write(organ_index, 11, int(min(R_Z)))
        worksheet.write(organ_index, 12, int(max(R_Z)))
    workbook.close()


if __name__ == "__main__":
    printMinMaxValue()
