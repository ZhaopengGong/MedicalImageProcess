'''
@Author: 弓照鹏
@LastEditors: 弓照鹏
@Date: 2018-11-30 16:38:42
@LastEditTime: 2018-12-10 18:33:56
@organization: BJUT
'''


# -*- coding:utf-8 -*- 

import numpy as np
import cv2
import os
import pandas as pd
import xlrd
import xlsxwriter
import matplotlib.pyplot as plt

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

def getColorByIndex(i):
    if i==1:
        return (255, 191, 0)
    elif i==2:
        return (0, 100, 0)
    elif i==3:
        return (92, 92, 205)
    elif i==4:
        return (147, 20, 255)
    elif i==5:
        return (0, 0, 139)
    elif i==6:
        return (0, 255, 255)
    elif i==7:
        return (0, 165, 255)
    elif i==8:
        return (0, 69, 255)
    elif i==9:
        return (64, 64, 255)
    elif i==10:
        return (186, 231, 186)
    elif i==11:
        return (180, 238, 180)

# 获取去重之后的矩阵
def getMatrix(candidate_matrix, i, sheet, row_count,isleft):
    result_matrix = np.where(candidate_matrix==i)
    four = pd.Series(result_matrix[0]).describe()
    # 先检测行有没有
    Q1 = four['25%']
    Q3 = four['75%']
    IQR = Q3 - Q1
    # 计算出上限和下限
    upper = Q3 + 1.5 * IQR
    lower = Q1 - 1.5 * IQR
    row_list = [coordinate for coordinate in result_matrix[0]]
    del_row_index_data = [index for index, coordinate in enumerate(row_list) if coordinate<lower or coordinate>upper ]
    four = pd.Series(result_matrix[1]).describe()
    # 先检测行有没有
    Q1 = four['25%']
    Q3 = four['75%']
    IQR = Q3 - Q1
    # 计算出上限和下限
    upper = Q3 + 1.5 * IQR
    lower = Q1 - 1.5 * IQR
    col_list = [coordinate for coordinate in result_matrix[1]]
    del_col_index_data = [index for index, coordinate in enumerate(col_list) if coordinate<lower or coordinate>upper]
    # 要被删除的索引集合
    del_index_list = list(set(del_row_index_data).union(set(del_col_index_data)))
    # 删除的时候一定要注意是从后面往前面删除的
    for index in sorted(del_index_list, reverse=True):
        del row_list[index]
        del col_list[index]
    # 继续检测是不是满足x和y的范围
    for elements in range(row_count):
        if getOrganName(i) in sheet.row_values(elements):
            min_x = 0
            max_x = 0
            min_y = 0
            max_y = 0
            if isleft==1:
                min_x = int(sheet.row_values(elements)[1])
                max_x = int(sheet.row_values(elements)[2])
                min_y = int(sheet.row_values(elements)[3])
                max_y = int(sheet.row_values(elements)[4])
            else:
                # 因为是右侧多加了宽度的一半
                min_x = int(sheet.row_values(elements)[7])-210
                max_x = int(sheet.row_values(elements)[8])-210
                min_y = int(sheet.row_values(elements)[9])
                max_y = int(sheet.row_values(elements)[10])
            del_row_index_data = [index for index, coordinate in enumerate(row_list) if coordinate<min_y or coordinate>max_y ]
            del_col_index_data = [index for index, coordinate in enumerate(col_list) if coordinate<min_x or coordinate>max_x ]
            del_index = list(set(del_row_index_data).union(set(del_col_index_data)))
            # 删除的时候一定要注意是从后面往前面删除的
            for index in sorted(del_index, reverse=True):
                del row_list[index]
                del col_list[index]
            break
    return [row_list, col_list]

def IOU(Reframe,GTframe):
    cx1 = Reframe[0]
    cy1 = Reframe[1]
    cx2 = Reframe[2]
    cy2 = Reframe[3]
    width1 = Reframe[2]-Reframe[0]
    height1 = Reframe[3]-Reframe[1]

    gx1 = GTframe[0]
    gy1= GTframe[1]
    gx2 = GTframe[2]
    gy2= GTframe[3]
    width2 = GTframe[2]-GTframe[0]
    height2 = GTframe[3]-GTframe[1]

    carea = (cx2 - cx1) * (cy2 - cy1) #C的面积
    garea = (gx2 - gx1) * (gy2 - gy1) #G的面积

    x1 = max(cx1, gx1)
    y1 = max(cy1, gy1)
    x2 = min(cx2, gx2)
    y2 = min(cy2, gy2)

    width = max(0, x2 - x1)
    height = max(0, y2 - y1)
    area = width * height #C∩G的面积
 
    if width <=0 or height <= 0:
        iou = 0 # 重叠率为 0 
    else:
        iou = area*1. / (carea + garea - area)
    return iou
  
        
def saveVisualResult():
    # dicom图像转换为jpg图像后的路径
    image_jpg_folder_path = "D:\\workspace\\MedicalImageWorkspace\\FCN-BoundingBox\\image"
    # 可视化结果保存路径
    visual_result_path = "D:\\workspace\\MedicalImageWorkspace\\FCN-BoundingBox\\visual_result"
    # 真值的路径的
    ground_truth_path = "D:\\workspace\\MedicalImageWorkspace\\FCN-BoundingBox\\groundtruth"
    # 预测值的路径
    predict_label = "D:\\workspace\\MedicalImageWorkspace\\FCN-BoundingBox\\predict_label"
    # 已经保存了每个解剖结构最大值和最小值的文件
    min_max_excel_path = "D:\\workspace\\MedicalImageWorkspace\\20181202统计坐标\\CoordinateIntegration\\min_max.xlsx"
    # 计算出的IOU的值
    iou_excel_path = "D:\\workspace\\MedicalImageWorkspace\\20181202统计坐标\\CoordinateIntegration\\iou.xlsx"
    workbook = xlsxwriter.Workbook(iou_excel_path)
    worksheet = workbook.add_worksheet()
    # 向第一行写入数据
    for organIndex in range(1, 12):
        worksheet.write(0, organIndex, getOrganName(organIndex))
    # 打开文件
    min_max_file = xlrd.open_workbook(min_max_excel_path)
    # 获取到第一个sheet
    sheet = min_max_file.sheets()[0]
    # 统计第一个sheet中有多少行多少列
    row_count = sheet.nrows
    image_folder_list = os.listdir(image_jpg_folder_path)
    for folder_index, image_folder_name in enumerate(image_folder_list):
        sub_image_folder_path = os.path.join(image_jpg_folder_path, image_folder_name)
        image_list = os.listdir(sub_image_folder_path)
        predict_label_file_path = os.path.join(predict_label, image_folder_name+".npy")
        ground_truth_file_path = os.path.join(ground_truth_path, image_folder_name+".npy")
        predict_label_file = np.load(predict_label_file_path)
        ground_truth_file = np.load(ground_truth_file_path)
        sum_CG_IOU = 0
        sum_ZG_IOU = 0
        sum_DG_IOU = 0
        sum_EW1_IOU = 0
        sum_EW2_IOU = 0
        sum_WBGG_IOU = 0
        sum_HBGG_IOU = 0
        sum_QBGG_IOU = 0
        sum_QT_IOU = 0
        sum_JJMQW_IOU = 0
        sum_NTD_IOU = 0
        sum_CG_IOU_count = 0
        sum_ZG_IOU_count = 0
        sum_DG_IOU_count = 0
        sum_EW1_IOU_count = 0
        sum_EW2_IOU_count = 0
        sum_WBGG_IOU_count = 0
        sum_HBGG_IOU_count = 0
        sum_QBGG_IOU_count = 0
        sum_QT_IOU_count = 0
        sum_JJMQW_IOU_count = 0
        sum_NTD_IOU_count = 0
        for image_file_name in image_list:
            image_file_path = os.path.join(sub_image_folder_path,image_file_name)
            slice_index = int((image_file_name.split("_")[1]).split(".")[0])
            
            predict_label_file_slice = predict_label_file[:,:,slice_index]
            ground_truth_file_slice = ground_truth_file[:,:,slice_index]
            # 要创建出8个数组分别保存真值两侧区域，
            # 真值数组
            height, width= ground_truth_file_slice.shape
            
            gt_left_matrix = ground_truth_file_slice[:, 0:int(width/2)]
            gt_right_matrix = ground_truth_file_slice[:, int(width/2):]

            predict_left_matrix = predict_label_file_slice[:, 0:int(width/2)]
            predict_right_matrix = predict_label_file_slice[:, int(width/2):]
            # 写入每一行的第一列
            worksheet.write(folder_index+1, 0, image_folder_name)
            col_index = 1
            image = cv2.imdecode(np.fromfile(image_file_path, dtype=np.uint8), 1)
            image_gt = cv2.imdecode(np.fromfile(image_file_path, dtype=np.uint8), 1)
            for i in range(1, 12):
                # image = cv2.imdecode(np.fromfile(image_file_path, dtype=np.uint8), 1)
                gt_left_matrix_filter = np.where(gt_left_matrix==i)
                if(len(gt_left_matrix_filter[0]) != 0):
                    gt_left_y_min = (gt_left_matrix_filter[0])[np.argmin(gt_left_matrix_filter[0])]
                    gt_left_y_max = (gt_left_matrix_filter[0])[np.argmax(gt_left_matrix_filter[0])]
                    gt_left_x_min = (gt_left_matrix_filter[1])[np.argmin(gt_left_matrix_filter[1])]
                    gt_left_x_max = (gt_left_matrix_filter[1])[np.argmax(gt_left_matrix_filter[1])]
                    cv2.rectangle(image_gt,(gt_left_x_min,gt_left_y_min),(gt_left_x_max, gt_left_y_max),getColorByIndex(i), 1)
                    # 构建左侧的真值检测矩形框
                    gt_left_rect = [gt_left_x_min, gt_left_y_min, gt_left_x_max, gt_left_y_max]
                else:
                    gt_left_rect = [0, 0, 0, 0]
                gt_right_matrix_filter = np.where(gt_right_matrix==i)
                if(len(gt_right_matrix_filter[0]) != 0):
                    gt_right_y_min = (gt_right_matrix_filter[0])[np.argmin(gt_right_matrix_filter[0])]
                    gt_right_y_max = (gt_right_matrix_filter[0])[np.argmax(gt_right_matrix_filter[0])]
                    gt_right_x_min = int(width/2)+(gt_right_matrix_filter[1])[np.argmin(gt_right_matrix_filter[1])]
                    gt_right_x_max = int(width/2)+(gt_right_matrix_filter[1])[np.argmax(gt_right_matrix_filter[1])]
                    cv2.rectangle(image_gt,(gt_right_x_min,gt_right_y_min),(gt_right_x_max, gt_right_y_max),getColorByIndex(i), 1)
                    # 构建右侧的真值检测矩形框
                    gt_right_rect = [gt_right_x_min, gt_right_y_min, gt_right_x_max, gt_right_y_max]
                else:
                    gt_right_rect = [0, 0, 0, 0]
                predict_left_matrix_filter = getMatrix(predict_left_matrix, i, sheet, row_count, 1)
                if(len(predict_left_matrix_filter[0]) != 0):
                    predict_left_y_min = (predict_left_matrix_filter[0])[np.argmin(predict_left_matrix_filter[0])]
                    predict_left_y_max = (predict_left_matrix_filter[0])[np.argmax(predict_left_matrix_filter[0])]
                    predict_left_x_min = (predict_left_matrix_filter[1])[np.argmin(predict_left_matrix_filter[1])]
                    predict_left_x_max = (predict_left_matrix_filter[1])[np.argmax(predict_left_matrix_filter[1])]
                    cv2.rectangle(image,(predict_left_x_min,predict_left_y_min),(predict_left_x_max, predict_left_y_max),getColorByIndex(i), 1)
                    # 构建左侧的预测值检测矩形框
                    predict_left_rect = [predict_left_x_min, predict_left_y_min, predict_left_x_max, predict_left_y_max]
                else:
                    predict_left_rect = [0, 0, 0, 0]
                predict_right_matrix_filter = getMatrix(predict_right_matrix, i, sheet, row_count, 0)
                if(len(predict_right_matrix_filter[0]) != 0):
                    predict_right_y_min = (predict_right_matrix_filter[0])[np.argmin(predict_right_matrix_filter[0])]
                    predict_right_y_max = (predict_right_matrix_filter[0])[np.argmax(predict_right_matrix_filter[0])]
                    predict_right_x_min = int(width/2)+(predict_right_matrix_filter[1])[np.argmin(predict_right_matrix_filter[1])]
                    predict_right_x_max = int(width/2)+(predict_right_matrix_filter[1])[np.argmax(predict_right_matrix_filter[1])]
                    cv2.rectangle(image,(predict_right_x_min,predict_right_y_min),(predict_right_x_max, predict_right_y_max),getColorByIndex(i), 1)
                    # 构建右侧的预测值检测矩形框
                    predict_right_rect = [predict_right_x_min, predict_right_y_min, predict_right_x_max, predict_right_y_max]
                else:
                    predict_right_rect = [0, 0, 0, 0]
                if predict_left_rect!=[0,0,0,0] and gt_left_rect!=[0,0,0,0]:
                    left_iou = IOU(predict_left_rect, gt_left_rect)
                    if i ==1:
                        sum_CG_IOU += left_iou
                        sum_CG_IOU_count += 1
                    elif i==2:
                        sum_ZG_IOU += left_iou
                        sum_ZG_IOU_count += 1
                    elif i==3:
                        sum_DG_IOU += left_iou
                        sum_DG_IOU_count += 1
                    elif i==4:
                        sum_EW1_IOU += left_iou
                        sum_EW1_IOU_count += 1
                    elif i==5:
                        sum_EW2_IOU += left_iou
                        sum_EW2_IOU_count += 1
                    elif i==6:
                        sum_WBGG_IOU += left_iou
                        sum_WBGG_IOU_count += 1
                    elif i==7:
                        sum_HBGG_IOU += left_iou
                        sum_HBGG_IOU_count += 1
                    elif i==8:
                        sum_QBGG_IOU += left_iou
                        sum_QBGG_IOU_count += 1
                    elif i==9:
                        sum_JJMQW_IOU += left_iou
                        sum_JJMQW_IOU_count += 1
                    elif i==10:
                        sum_QT_IOU += left_iou
                        sum_QT_IOU_count += 1
                    elif i==11:
                        sum_NTD_IOU += left_iou
                        sum_NTD_IOU_count += 1
                if predict_right_rect!=[0,0,0,0] and gt_right_rect!=[0,0,0,0]:
                    right_iou =  IOU(predict_right_rect, gt_right_rect)
                    if i ==1:
                        sum_CG_IOU += right_iou
                        sum_CG_IOU_count += 1
                    elif i==2:
                        sum_ZG_IOU += right_iou
                        sum_ZG_IOU_count += 1
                    elif i==3:
                        sum_DG_IOU += right_iou
                        sum_DG_IOU_count += 1
                    elif i==4:
                        sum_EW1_IOU += right_iou
                        sum_EW1_IOU_count += 1
                    elif i==5:
                        sum_EW2_IOU += right_iou
                        sum_EW2_IOU_count += 1
                    elif i==6:
                        sum_WBGG_IOU += right_iou
                        sum_WBGG_IOU_count += 1
                    elif i==7:
                        sum_HBGG_IOU += right_iou
                        sum_HBGG_IOU_count += 1
                    elif i==8:
                        sum_QBGG_IOU += right_iou
                        sum_QBGG_IOU_count += 1
                    elif i==9:
                        sum_JJMQW_IOU += right_iou
                        sum_JJMQW_IOU_count += 1
                    elif i==10:
                        sum_QT_IOU += right_iou
                        sum_QT_IOU_count += 1
                    elif i==11:
                        sum_NTD_IOU += right_iou
                        sum_NTD_IOU_count += 1
                
            save_folder_parent_path = os.path.join(visual_result_path, image_folder_name)
            if not os.path.exists(save_folder_parent_path):
                os.mkdir(save_folder_parent_path)
            save_file_path = os.path.join(save_folder_parent_path, image_file_name.split('.')[0]+".png")
            # save_gt_file_path = os.path.join(save_folder_parent_path, image_file_name.split('.')[0]+"_gt.jpg")
            # cv2.imwrite(save_file_path, image)
            # cv2.imwrite(save_gt_file_path, image_gt)
            plt.figure()
            plt.subplot(1, 2, 1)
            plt.title('predict')
            plt.imshow(image)
            plt.axis('off')
            plt.subplot(1, 2, 2)
            # 设置子图的标题，注意设置title的位置
            plt.title('groundtruth')
            plt.imshow(image_gt)
            # 隐藏坐标轴
            plt.axis('off')
            # 设置图像的清晰度，设置去掉白边，显示的紧凑一点，将图像保存
            plt.savefig(save_file_path, dpi=300, bbox_inches='tight')
            # 将绘图面板关闭掉
            plt.close()
        worksheet.write(folder_index+1, 1, float(sum_CG_IOU/sum_CG_IOU_count))
        worksheet.write(folder_index+1, 2, float(sum_ZG_IOU/sum_ZG_IOU_count))
        worksheet.write(folder_index+1, 3, float(sum_DG_IOU/sum_DG_IOU_count))
        worksheet.write(folder_index+1, 4, float(sum_EW1_IOU/sum_EW1_IOU_count))
        worksheet.write(folder_index+1, 5, float(sum_EW2_IOU/sum_EW2_IOU_count))
        worksheet.write(folder_index+1, 6, float(sum_WBGG_IOU/sum_WBGG_IOU_count))
        worksheet.write(folder_index+1, 7, float(sum_HBGG_IOU/sum_HBGG_IOU_count))
        worksheet.write(folder_index+1, 8, float(sum_QBGG_IOU/sum_QBGG_IOU_count))
        worksheet.write(folder_index+1, 9, float(sum_JJMQW_IOU/sum_JJMQW_IOU_count))
        worksheet.write(folder_index+1, 10, float(sum_QT_IOU/sum_QT_IOU_count))
        worksheet.write(folder_index+1, 11, float(sum_NTD_IOU/sum_NTD_IOU_count))
    workbook.close()


if __name__ == "__main__":
    saveVisualResult()