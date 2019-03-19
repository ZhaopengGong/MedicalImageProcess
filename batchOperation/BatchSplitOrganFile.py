'''
@Author: 弓照鹏
@LastEditors: 弓照鹏
@Date: 2019-01-21 21:22:34
@LastEditTime: 2019-01-21 21:32:29
@organization: BJUT
将组织器官批量抽取出来存放在不同的文件夹中
'''

import shutil
import os


# 包含10个关键解剖结构的文件夹
originalFolderPath = 'G:\\耳部CT数据集\\LabelDicomCropSymmetry_UnCombine'
# 抽取后写入的文件夹
targetFolderPath = 'G:\\耳部CT数据集\\LabelDicomCropSymmetry_UnCombine_Split'

for patientFolderName in os.listdir(originalFolderPath):
    print(patientFolderName)
    subFolderPath = os.path.normpath(os.path.join(originalFolderPath, patientFolderName))
    # 特别注意名字不要重名以免名字拼接造成不必要的麻烦
    targetPatientFolderPath = os.path.normpath(os.path.join(targetFolderPath, patientFolderName))
    # 遍历11个耳部关键解剖结构，将该结构分别存入对应的文件夹下面
    for organName in os.listdir(targetFolderPath):
        organFolderPath = os.path.normpath(os.path.join(subFolderPath, organName))
        targetPath = os.path.normpath(os.path.join(targetFolderPath, organName, patientFolderName))
        # # 如果要判断的文件夹不存在则创建该文件夹
        # if not os.path.exists(targetPath):
        #     os.mkdir(targetPath)
        shutil.copytree(organFolderPath, targetPath)
        # for organFileName in os.listdir(organFolderPath):
        #     organFilePath = os.path.normpath(os.path.join(organFolderPath, organFileName))
        #     targetNiiFilePath = os.path.normpath(os.path.join(targetNiiFolderPath, organFileName))
        #     shutil.copy(organFilePath, targetNiiFilePath)