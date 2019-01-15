# -*- coding:utf-8 -*- 
import numpy as np 
import matplotlib.pyplot as plt

npy_file_path = "D:\\workspace\\MedicalImageWorkspace\\FCN-BoundingBox\\groundtruth\\0001.npy"
npy_file = np.load(npy_file_path)
# ground_truth_file_slice = npy_file[:,:,20]
# gt_left_matrix = ground_truth_file_slice[:, 0:int(420/2)]
# gt_right_matrix = ground_truth_file_slice[:, int(420/2):]
# gt_left_matrix_filter = np.where(gt_left_matrix==11)
# print(gt_left_matrix_filter)
plt.imshow(npy_file[:,:,20], cmap=plt.cm.gray)
plt.show()