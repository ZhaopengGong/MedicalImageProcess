#
# @Author: gzp 
# @Date: 2018-08-06 10:14:17 
# @Last Modified by: gzp
# @Last Modified time: 2018-08-06 10:14:52
#
import numpy as np
import os
import xlsxwriter
# 标注文件夹的路径
label_folder_path = 'G:/Deep Learing/data/EarIOuCalculateData/标注文件'
# 结果文件夹的路径
result_parent_folder_path = 'G:/Deep Learing/data/EarIOuCalculateData/11个解剖结构的结果文件'
# excel文件地址,任意指定即可,xlsx文件不一定必须存在
IOU_result_file_path = 'G:/Deep Learing/data/EarIOuCalculateData/iou_result.xlsx'
workbook = xlsxwriter.Workbook(IOU_result_file_path)
worksheet = workbook.add_worksheet()
# 向文件中的第一行写入数据
worksheet.write(0, 0, '编号')
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

def IOU(Reframe,GTframe):
    """
    自定义函数，计算两矩形 IOU，传入为均为矩形对角线，（x,y）  坐标。
    """
    x1 = Reframe[0]
    y1 = Reframe[1]
    width1 = Reframe[2]-Reframe[0]
    height1 = Reframe[3]-Reframe[1]

    x2 = GTframe[0]
    y2 = GTframe[1]
    width2 = GTframe[2]-GTframe[0]
    height2 = GTframe[3]-GTframe[1]

    endx = max(x1+width1,x2+width2)
    startx = min(x1,x2)
    width = width1+width2-(endx-startx)

    endy = max(y1+height1,y2+height2)
    starty = min(y1,y2)
    height = height1+height2-(endy-starty)

    if width <=0 or height <= 0:
        ratio = 0 # 重叠率为 0 
    else:
        Area = width*height # 两矩形相交面积
        Area1 = width1*height1
        Area2 = width2*height2
        ratio = Area*1./(Area1+Area2-Area)
    # return IOU
    return ratio


organ_index = 0
for result_folder_name in range(1,12):
    organ_index += 1
    result_folder_path = os.path.normpath(os.path.join(result_parent_folder_path,str(result_folder_name)))
    for index in range(1, 9):
        ratio_sum = 0
        ratio_number = 0
        result_file_path = os.path.normpath(os.path.join(result_folder_path,'volumes','R10_'+str(index)+'.npz'))
        label_file_path = os.path.normpath(os.path.join(label_folder_path, str.zfill(str(index), 4)+'.npy'))
        result_file = np.load(result_file_path)
        result_file = result_file['volume']
        label_file = np.load(label_file_path)
        for pic_index in range(0, 60):
            # 取出轴位上的图像数据，并且找特定组织器官的标记像素
            result_matrix = result_file[:,:,pic_index]
            label_matrix = label_file[:,:,pic_index]
            # 求解出矩阵的shape
            height, width = result_matrix.shape
            # 求解出左侧和右侧矩阵
            result_matrix_left = result_matrix[:, 0:int(width/2)]
            result_matrix_right = result_matrix[:, int(width/2):]
            label_matrix_left = label_matrix[:, 0:int(width/2)]
            label_matrix_right = label_matrix[:, int(width/2):]
            # 找出结果文件和标注文件中目标区域的数组
            result_matrix_left_detect = np.where(result_matrix_left==1)
            result_matrix_right_detect = np.where(result_matrix_right==1)
            label_matrix_left_detect = np.where(label_matrix_left==organ_index)
            label_matrix_right_detect = np.where(label_matrix_right==organ_index)
            # 先分别判断左右两侧是不是为0
            if(result_matrix_left_detect[0].shape[0]==0):
                result_matrix_left_rect = [0,0,0,0]
            else:
                result_matrix_left_rect = [(result_matrix_left_detect[1])[np.argmin(result_matrix_left_detect[1])], (result_matrix_left_detect[0])[np.argmin(result_matrix_left_detect[0])], (result_matrix_left_detect[1])[np.argmax(result_matrix_left_detect[1])], (result_matrix_left_detect[0])[np.argmax(result_matrix_left_detect[0])]]
            if(label_matrix_left_detect[0].shape[0]==0):
                label_matrix_left_rect = [0,0,0,0]
            else:
                label_matrix_left_rect = [(label_matrix_left_detect[1])[np.argmin(label_matrix_left_detect[1])], (label_matrix_left_detect[0])[np.argmin(label_matrix_left_detect[0])], (label_matrix_left_detect[1])[np.argmax(label_matrix_left_detect[1])], (label_matrix_left_detect[0])[np.argmax(label_matrix_left_detect[0])]]
            if(result_matrix_right_detect[0].shape[0]==0):
                result_matrix_right_rect = [0,0,0,0]
            else:
                result_matrix_right_rect = [(result_matrix_right_detect[1])[np.argmin(result_matrix_right_detect[1])], (result_matrix_right_detect[0])[np.argmin(result_matrix_right_detect[0])], (result_matrix_right_detect[1])[np.argmax(result_matrix_right_detect[1])], (result_matrix_right_detect[0])[np.argmax(result_matrix_right_detect[0])]]
            if(label_matrix_right_detect[0].shape[0]==0):
                label_matrix_right_rect = [0,0,0,0]
            else:
                label_matrix_right_rect = [(label_matrix_right_detect[1])[np.argmin(label_matrix_right_detect[1])], (label_matrix_right_detect[0])[np.argmin(label_matrix_right_detect[0])], (label_matrix_right_detect[1])[np.argmax(label_matrix_right_detect[1])], (label_matrix_right_detect[0])[np.argmax(label_matrix_right_detect[0])]]
            # 计算左侧与右侧的匹配率
            left_match_ratio = IOU(result_matrix_left_rect, label_matrix_left_rect)
            right_match_ratio = IOU(result_matrix_right_rect, label_matrix_right_rect)
            if(left_match_ratio!=0):
                ratio_sum += left_match_ratio
                ratio_number += 1
                # print('leftratio-',left_match_ratio,result_matrix_left_rect,label_matrix_left_rect)
            if(right_match_ratio!=0):
                ratio_sum += right_match_ratio
                ratio_number += 1
                # print('rihtratio-',right_match_ratio,result_matrix_right_rect,label_matrix_right_rect)
        worksheet.write(index, 0, index)
        print('解剖结构',organ_index,'---病人编号',index,'---重叠数量', ratio_number,result_file_path,label_file_path)
        if(ratio_number == 0):
            average_ratio = 0
        else:
            average_ratio = ratio_sum/ratio_number
        worksheet.write(index, organ_index, average_ratio)
workbook.close()