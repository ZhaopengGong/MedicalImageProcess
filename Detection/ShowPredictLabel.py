# -*- coding:utf-8 -*- 
import numpy as np 
import matplotlib.pyplot as plt
import cv2

npy_file_path = "H:\\耳部CT数据集\\cube_image_npy\\QT\\valid\\00029167L.npy"
npy_file = np.load(npy_file_path)
image_file_path = 'H:\\WED-DCM2JPG\\00029167_000031.jpg'
# ground_truth_file_slice = npy_file[:,:,20]
# gt_left_matrix = ground_truth_file_slice[:, 0:int(420/2)]
# gt_right_matrix = ground_truth_file_slice[:, int(420/2):]
# gt_left_matrix_filter = np.where(gt_left_matrix==11)
# print(gt_left_matrix_filter)
# print(np.unique(npy_file))
# plt.imshow(npy_file[:,:,20], cmap=plt.cm.gray)
# plt.show()
image_file = cv2.imread(image_file_path)
print(image_file.shape)