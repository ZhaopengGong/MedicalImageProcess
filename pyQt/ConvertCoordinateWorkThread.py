# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QThread,pyqtSignal
import time
import os
import glob
import codecs
import pandas as pd
import skimage.io as io
import numpy as np


# 定义校准数据的工作线程
class ConvertCoordinateWorkThread(QtCore.QThread):
    convertProcessSignal = pyqtSignal(str)
    finishSignal = pyqtSignal()

    def __init__(self, label_root_dir, coordinate_root_dir):
        super(ConvertCoordinateWorkThread, self).__init__()
        self.label_root_dir = label_root_dir
        self.coordinate_root_dir = coordinate_root_dir

    def run(self):
        # 总共的病人文件夹数
        total_patient_num = len(os.listdir(self.label_root_dir))
        current_patient_num = 0
        for patient_folder in os.listdir(self.label_root_dir):
            current_patient_num += 1
            self.convertProcessSignal.emit('正在校准-'+patient_folder + "-" + str(current_patient_num) + "/" + str(total_patient_num))
            # 二级文件夹
            sub_folder_dir = os.path.join(self.label_root_dir, patient_folder)
            # 标记面积的文件夹
            axial_Area_files_path = os.path.join(sub_folder_dir, 'Axial_Area')
            # 标记的bmp文件
            axial_bmp_files_path = os.path.join(sub_folder_dir, 'Axial_bmp')
            for area_file_name in os.listdir(axial_Area_files_path):
                # 将标注文件的名称按照_进行分割，示例CG_Axial.txt
                area_file_split = area_file_name.split('_')
                # 截取关键解剖结构的名称例如CG
                area_file_type = area_file_split[0]
                # 拼接具体的标注区域文件的路径
                area_file_path = os.path.join(axial_Area_files_path, area_file_name)
                # 打开文件
                area_file = codecs.open(area_file_path, 'r', 'utf-16')
                line_number = 0
                slice_space_mm = 0
                # 坐标文件的路径，还是根据前面已经有的信息拼接起来
                grayValue_file_path = os.path.join(sub_folder_dir, 'Axial_HF', area_file_type + '_grayvalues.txt')
                grayValue_folder_path = os.path.join(self.coordinate_root_dir, patient_folder)
                if os.path.exists(grayValue_folder_path) == 0:
                    os.mkdir(grayValue_folder_path)
                grayValue_file_path_final = os.path.join(self.coordinate_root_dir, patient_folder, area_file_type + '_HF.csv')
                fileSize = os.path.getsize(grayValue_file_path)
                if(fileSize != 0):
                    dot_num = 0
                    # 读取标注文件
                    grayValue_file = pd.read_csv(grayValue_file_path, header=None, names=None)
                    # 遍历坐标文件的
                    line_number_grayValue = 0
                    for line in area_file:
                        line_number += 1
                        if line_number > 1:
                            # 其实这里的分割符是两个\t标识
                            line_split = line.split('		')
                            slice_number = line_split[0]
                            axial_area_value = line_split[1]
                            # 获取层间距以算出层编号
                            if line_number == 3:
                                slice_space_mm = float(slice_number)
                            if (slice_space_mm == 0):
                                slice_number = 1
                            else:
                                slice_number = round(float(slice_number) / slice_space_mm) + 1
                            # 找到标注面积不为0的点，
                            if float(axial_area_value) > 0:
                                # 此处注意四舍五如，小数点后保留两位小数，将数字转换为字符串
                                slice_number_format = str(format(round(float(line_split[0]), 2), '3.2f'))
                                split_str = slice_number_format.split('.')
                                # 分别提取出前缀和后缀
                                split_prefix = split_str[0]
                                # 去除掉空格
                                split_prefix = split_prefix.strip()
                                split_suffix = split_str[1]
                                # 对前缀补0
                                format_str = split_prefix.zfill(3)
                                # 目标文件名称的拼接
                                strcat_str = format_str + '.' + split_suffix[0:1]
                                # 导出的标注图片文件，需要注意的是这里是拿着bmp文件的名字进行匹配，一定意义上是在搜索
                                bmp_file_array = glob.glob(os.path.join(axial_bmp_files_path, area_file_type, '*_Axial+' + strcat_str + '*' + '.bmp'))
                                bmp_file_array = bmp_file_array[0]
                                test_point = 0
                                bmp_file = io.imread(bmp_file_array)
                                image_shape = bmp_file.shape
                                dot_count = 0
                                for height in range(image_shape[0]-150):
                                    # 对图像区域进行搜索，由于有大黑边的存在所以必须要跳过大黑边以提高程序的性能
                                    if ((bmp_file[height, :, 0]).tolist().count(0) < int(0.9*image_shape[1])):
                                        for width in range(80, image_shape[1]-80):
                                            # 计算图像第三个通道的r,g,b值的方差,x
                                            std = np.std([bmp_file[height, width, 0], bmp_file[height, width, 1], bmp_file[height, width, 2]])
                                            if ( std > 10):
                                                grayValue_file.iat[line_number_grayValue, 0] = width
                                                grayValue_file.iat[line_number_grayValue, 1] = height
                                                grayValue_file.iat[line_number_grayValue, 2] = 60 - slice_number + 1
                                                dot_count = dot_count + 1
                                                # 统计已经修改了多少行了
                                                line_number_grayValue += 1
                                dot_num += dot_count
                        if grayValue_file.shape[0] != dot_num:
                            print("异常数据" + patient_folder + "下面的" + area_file_type + "应有" + str(grayValue_file.shape[0]) + "个点实际有" + str(dot_num))
                    area_file.close()
                    # 将数据重新写入一个新的文件
                    grayValue_file.to_csv(grayValue_file_path_final, index=False, mode='w', header=False)
        # 向主线程发送消息，括号里面可以加入文字[' ', '测试数据 ']
        self.finishSignal.emit()