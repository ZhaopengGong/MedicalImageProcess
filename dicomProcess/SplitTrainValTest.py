#!/usr/bin/env python
# coding=UTF-8
'''
@Author: 弓照鹏
@LastEditors: 弓照鹏
@organization: BJUT
@Date: 2019-03-17 20:55:11
@LastEditTime: 2019-03-17 20:59:28
将数据集分为训练集 测试集  验证集
'''
import os


def randomNpyFile(image_folder, txt_folder):
    image_jpeg_list = sorted(os.listdir(image_folder))
    # random.shuffle(image_jpeg_list)
    train_list = image_jpeg_list[0:int(len(image_jpeg_list)*0.8)]
    val_list = image_jpeg_list[int(len(image_jpeg_list)*0.8):int(len(image_jpeg_list)*0.9)]
    test_list = image_jpeg_list[int(len(image_jpeg_list)*0.9):]
    train_file_path = os.path.join(txt_folder, "train.txt")
    val_file_path = os.path.join(txt_folder, "val.txt")
    test_file_path = os.path.join(txt_folder, "test.txt")
    train_file = open(train_file_path, 'w')
    for filename in train_list:
        train_file.write(filename)
        train_file.write('\n')
    train_file.close()

    val_file = open(val_file_path, 'w')
    for filename in val_list:
        val_file.write(filename)
        val_file.write('\n')
    val_file.close()

    test_file = open(test_file_path, 'w')
    for filename in test_list:
        test_file.write(filename)
        test_file.write('\n')
    test_file.close()
    print(len(train_list), len(val_list), len(test_list))

if __name__ == "__main__":
    image_folder = 'H:\\耳部CT数据集\\WED图像转换为JPEG'
    txt_folder = 'H:\\耳部CT数据集'
    randomNpyFile(image_folder, txt_folder)