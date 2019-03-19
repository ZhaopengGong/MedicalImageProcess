'''
@Author: 弓照鹏
@LastEditors: 弓照鹏
@Date: 2019-01-28 18:07:33
@LastEditTime: 2019-03-15 11:04:07
@organization: BJUT
一个测试的类
'''

import numpy as np


path  = "H:\\耳部CT数据集\\cube_label_npy\\JJMQW\\valid\\00101092L.npy"
npy_file = np.load(path)
print(np.unique(npy_file))