'''
@Author: 弓照鹏
@LastEditors: 弓照鹏
@Date: 2019-01-18 18:33:45
@LastEditTime: 2019-01-21 16:47:34
@organization: BJUT
生成标注数据的xml文件，将boundingbox的坐标写入到xml文件中
'''
from lxml.etree import Element, SubElement, tostring
import pprint
from xml.dom.minidom import parseString
import os
import pydicom 
import numpy as np

folder_path = "G:\\耳部CT数据集\\LabelDicomCropSymmetry_Combine_modifity"
output_folder_path = "G:\\耳部CT数据集\AnnotationXml"

def writeXmlObjectNode(matrix, organName):
        node_object = SubElement(node_root, 'object')
        node_name = SubElement(node_object, 'name')
        node_name.text = organName
        node_difficult = SubElement(node_object, 'difficult')
        node_difficult.text = '0'
        node_bndbox = SubElement(node_object, 'bndbox')
        # 写入xml文件需要将数字转换为字符串
        node_xmin = SubElement(node_bndbox, 'xmin')
        node_xmin.text = str(matrix[0])
        node_ymin = SubElement(node_bndbox, 'ymin')
        node_ymin.text = str(matrix[1])
        node_xmax = SubElement(node_bndbox, 'xmax')
        node_xmax.text = str(matrix[2])
        node_ymax = SubElement(node_bndbox, 'ymax')
        node_ymax.text = str(matrix[3])
        
# 该目录下面的每一个文件夹
for folderName in os.listdir(folder_path):
        print(folderName)
        single_folder_path = os.path.join(folder_path, folderName)
        # 遍历每一张dicom图像
        for filename in os.listdir(single_folder_path):
                dicom_file_path = os.path.join(single_folder_path, filename)
                dicomFile = pydicom.read_file(dicom_file_path)
                dicom_npy = np.array(dicomFile.pixel_array)
                height, width = dicom_npy.shape
                label_matrix_left = dicom_npy[:, 0:int(width/2)]
                label_matrix_right = dicom_npy[:, int(width/2):]
                # 左侧或者是右侧包含目标解剖结构才生成xml文件
                if len(np.unique(label_matrix_left))!=1 or len(np.unique(label_matrix_right))!=1:    
                        node_root = Element('annotation')
                        node_folder = SubElement(node_root, 'folder')
                        node_folder.text = folderName

                        node_filename = SubElement(node_root, 'filename')
                        node_filename.text = filename

                        node_size = SubElement(node_root, 'size')
                        node_width = SubElement(node_size, 'width')
                        node_width.text = '420'

                        node_height = SubElement(node_size, 'height')
                        node_height.text = '420'

                        node_depth = SubElement(node_size, 'depth')
                        node_depth.text = '1'

                        # 检测左侧包含了哪些目标解剖结构
                        if len(np.unique(label_matrix_left))!=1:
                                label_matrix_left_CG = np.where(label_matrix_left==1)
                                label_matrix_left_ZG = np.where(label_matrix_left==2)
                                label_matrix_left_EW1 = np.where(label_matrix_left==4)
                                label_matrix_left_JJMQW = np.where(label_matrix_left==9)
                                label_matrix_left_QT = np.where(label_matrix_left==10)
                                label_matrix_left_NTD = np.where(label_matrix_left==11)
                                if label_matrix_left_CG[0].shape[0] != 0:
                                        result_matrix_left_CG = [(label_matrix_left_CG[1])[np.argmin(label_matrix_left_CG[1])], (label_matrix_left_CG[0])[np.argmin(label_matrix_left_CG[0])],
                                                                (label_matrix_left_CG[1])[np.argmax(label_matrix_left_CG[1])], (label_matrix_left_CG[0])[np.argmax(label_matrix_left_CG[0])]]
                                        writeXmlObjectNode(result_matrix_left_CG, 'CG')
                                if label_matrix_left_ZG[0].shape[0] != 0:
                                        result_matrix_left_ZG = [(label_matrix_left_ZG[1])[np.argmin(label_matrix_left_ZG[1])], (label_matrix_left_ZG[0])[np.argmin(label_matrix_left_ZG[0])],
                                                                (label_matrix_left_ZG[1])[np.argmax(label_matrix_left_ZG[1])], (label_matrix_left_ZG[0])[np.argmax(label_matrix_left_ZG[0])]]
                                        writeXmlObjectNode(result_matrix_left_ZG, 'ZG')
                                if label_matrix_left_EW1[0].shape[0] != 0:
                                        result_matrix_left_EW1 = [(label_matrix_left_EW1[1])[np.argmin(label_matrix_left_EW1[1])], (label_matrix_left_EW1[0])[np.argmin(label_matrix_left_EW1[0])],
                                                                (label_matrix_left_EW1[1])[np.argmax(label_matrix_left_EW1[1])], (label_matrix_left_EW1[0])[np.argmax(label_matrix_left_EW1[0])]]
                                        writeXmlObjectNode(result_matrix_left_EW1, 'EW1')
                                if label_matrix_left_JJMQW[0].shape[0] != 0:
                                        result_matrix_left_JJMQW = [(label_matrix_left_JJMQW[1])[np.argmin(label_matrix_left_JJMQW[1])], (label_matrix_left_JJMQW[0])[np.argmin(label_matrix_left_JJMQW[0])],
                                                                (label_matrix_left_JJMQW[1])[np.argmax(label_matrix_left_JJMQW[1])], (label_matrix_left_JJMQW[0])[np.argmax(label_matrix_left_JJMQW[0])]]
                                        writeXmlObjectNode(result_matrix_left_JJMQW, 'JJMQW')
                                if label_matrix_left_QT[0].shape[0] != 0:
                                        result_matrix_left_QT = [(label_matrix_left_QT[1])[np.argmin(label_matrix_left_QT[1])], (label_matrix_left_QT[0])[np.argmin(label_matrix_left_QT[0])],
                                                                (label_matrix_left_QT[1])[np.argmax(label_matrix_left_QT[1])], (label_matrix_left_QT[0])[np.argmax(label_matrix_left_QT[0])]]
                                        writeXmlObjectNode(result_matrix_left_QT, 'QT')
                                if label_matrix_left_NTD[0].shape[0] != 0:
                                        result_matrix_left_NTD = [(label_matrix_left_NTD[1])[np.argmin(label_matrix_left_NTD[1])], (label_matrix_left_NTD[0])[np.argmin(label_matrix_left_NTD[0])],
                                                                (label_matrix_left_NTD[1])[np.argmax(label_matrix_left_NTD[1])], (label_matrix_left_NTD[0])[np.argmax(label_matrix_left_NTD[0])]]
                                        writeXmlObjectNode(result_matrix_left_NTD, 'NTD')
                        # 检测右侧包含了哪些目标解剖结构
                        if len(np.unique(label_matrix_right))!=1:
                                label_matrix_right_CG = np.where(label_matrix_right==1)
                                label_matrix_right_ZG = np.where(label_matrix_right==2)
                                label_matrix_right_EW1 = np.where(label_matrix_right==4)
                                label_matrix_right_JJMQW = np.where(label_matrix_right==9)
                                label_matrix_right_QT = np.where(label_matrix_right==10)
                                label_matrix_right_NTD = np.where(label_matrix_right==11)
                                if label_matrix_right_CG[0].shape[0] != 0:
                                        result_matrix_right_CG = [(label_matrix_right_CG[1])[np.argmin(label_matrix_right_CG[1])], (label_matrix_right_CG[0])[np.argmin(label_matrix_right_CG[0])],
                                                                (label_matrix_right_CG[1])[np.argmax(label_matrix_right_CG[1])], (label_matrix_right_CG[0])[np.argmax(label_matrix_right_CG[0])]]
                                        writeXmlObjectNode(result_matrix_right_CG, 'CG')
                                if label_matrix_right_ZG[0].shape[0] != 0:
                                        result_matrix_right_ZG = [(label_matrix_right_ZG[1])[np.argmin(label_matrix_right_ZG[1])], (label_matrix_right_ZG[0])[np.argmin(label_matrix_right_ZG[0])],
                                                                (label_matrix_right_ZG[1])[np.argmax(label_matrix_right_ZG[1])], (label_matrix_right_ZG[0])[np.argmax(label_matrix_right_ZG[0])]]
                                        writeXmlObjectNode(result_matrix_right_ZG, 'ZG')
                                if label_matrix_right_EW1[0].shape[0] != 0:
                                        result_matrix_right_EW1 = [(label_matrix_right_EW1[1])[np.argmin(label_matrix_right_EW1[1])], (label_matrix_right_EW1[0])[np.argmin(label_matrix_right_EW1[0])],
                                                                (label_matrix_right_EW1[1])[np.argmax(label_matrix_right_EW1[1])], (label_matrix_right_EW1[0])[np.argmax(label_matrix_right_EW1[0])]]
                                        writeXmlObjectNode(result_matrix_right_EW1, 'EW1')
                                if label_matrix_right_JJMQW[0].shape[0] != 0:
                                        result_matrix_right_JJMQW = [(label_matrix_right_JJMQW[1])[np.argmin(label_matrix_right_JJMQW[1])], (label_matrix_right_JJMQW[0])[np.argmin(label_matrix_right_JJMQW[0])],
                                                                (label_matrix_right_JJMQW[1])[np.argmax(label_matrix_right_JJMQW[1])], (label_matrix_right_JJMQW[0])[np.argmax(label_matrix_right_JJMQW[0])]]
                                        writeXmlObjectNode(result_matrix_right_JJMQW, 'JJMQW')
                                if label_matrix_right_QT[0].shape[0] != 0:
                                        result_matrix_right_QT = [(label_matrix_right_QT[1])[np.argmin(label_matrix_right_QT[1])], (label_matrix_right_QT[0])[np.argmin(label_matrix_right_QT[0])],
                                                                (label_matrix_right_QT[1])[np.argmax(label_matrix_right_QT[1])], (label_matrix_right_QT[0])[np.argmax(label_matrix_right_QT[0])]]
                                        writeXmlObjectNode(result_matrix_right_QT, 'QT')
                                if label_matrix_right_NTD[0].shape[0] != 0:
                                        result_matrix_right_NTD = [(label_matrix_right_NTD[1])[np.argmin(label_matrix_right_NTD[1])], (label_matrix_right_NTD[0])[np.argmin(label_matrix_right_NTD[0])],
                                                                (label_matrix_right_NTD[1])[np.argmax(label_matrix_right_NTD[1])], (label_matrix_right_NTD[0])[np.argmax(label_matrix_right_NTD[0])]]
                                        writeXmlObjectNode(result_matrix_right_NTD, 'NTD')
                        xml = tostring(node_root, pretty_print=True)  #格式化显示，该换行的换行
                        output_file_path = os.path.join(output_folder_path, folderName+"_"+filename.split(".")[0]+".xml")
                        output_file =  open(output_file_path, 'w')
                        output_file.write(str(xml, encoding = "utf-8"))
                        output_file.close()
        
                