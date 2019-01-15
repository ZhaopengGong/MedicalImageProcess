'''
@Author: 弓照鹏
@LastEditors: 弓照鹏
@Date: 2018-12-01 10:06:20
@LastEditTime: 2018-12-01 20:41:55
@organization: BJUT
'''
# -*- coding:utf-8 -*- 

import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns



# 获取去重之后的矩阵
def getMatrix(candidate_matrix, i):
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
    del_col_index_data = [index for index, coordinate in enumerate(row_list) if coordinate<lower or coordinate>upper]
    # 要被删除的索引集合
    del_index_list = []
    # 只要是x或者是y方向检测到异常值就将其删除掉
    if len(del_row_index_data)==len(del_col_index_data):
        del_index_list = del_row_index_data
    elif len(del_row_index_data)>len(del_col_index_data):
        del_index_list = del_row_index_data
    elif len(del_row_index_data)<len(del_col_index_data):
         del_index_list = del_col_index_data
    # 删除的时候一定要注意是从后面往前面删除的
    for index in sorted(del_index_list, reverse=True):
        del row_list[index]
        del col_list[index]
    return [row_list, col_list]

npy_file_path = "D:\\workspace\\MedicalImageWorkspace\\FCN-BoundingBox\\predict_label\\0004.npy"
min_max_excel_path = "D:\\workspace\\MedicalImageWorkspace\\20180702统计坐标\\CoordinateIntegration\\min_max.xlsx"
npy_file = np.load(npy_file_path)
npy_file_slice = npy_file[:,:,26]

height, width= npy_file_slice.shape
predict_left_matrix = npy_file_slice[:, 0:int(width/2)]
predict_right_matrix = npy_file_slice[:, int(width/2):]
# predict_left_matrix_filter = np.where(predict_right_matrix==4)
predict_left_matrix_filter = getMatrix(predict_left_matrix, 11)
filter_row = predict_left_matrix_filter[0]
filter_col = predict_left_matrix_filter[1]
filter_data_list = []
for i in range(len(filter_row)):
    filter_data_list.append([filter_row[i],filter_col[i]])
pre_data_list = []
pre_matrix = np.where(predict_left_matrix==11)
pre_row = pre_matrix[0]
pre_col = pre_matrix[1]
for i in range(len(pre_row)):
    pre_data_list.append([pre_row[i],pre_col[i]])
# row_data = pd.DataFrame(row)
# col_data = pd.DataFrame(col)
# plt.subplot(1,2,1)
# sns.boxplot(data=predict_left_matrix_filter, palette="Set1")
# plt.subplot(1,2,2)
# sns.boxplot(data=predict_left_matrix_filter, palette="Set1")
# plt.show()
print(pre_data_list)
print(filter_data_list)
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
data = pd.DataFrame(filter_data_list, columns=['y坐标','x坐标'])
ax =sns.boxplot(data=data, palette="Set1")
ax.set_title('右侧耳蜗内腔分割坐标统计盒图(single slice)')
plt.show()
