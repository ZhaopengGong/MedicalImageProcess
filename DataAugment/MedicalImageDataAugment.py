'''
@Author: 弓照鹏
@LastEditors: 弓照鹏
@Date: 2018-12-29 19:59:59
@LastEditTime: 2018-12-29 20:41:36
@organization: BJUT
'''
import tensorflow as tf
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt


def random_rotate_image(image, num):
    with tf.Graph().as_default():
        def random_rotate_image_func(image):
            #旋转角度范围
            angle = np.random.uniform(low=-25.0, high=25.0)
            return misc.imrotate(image, angle, 'bicubic')
        for i in range(num):
            image_rotate = tf.py_func(random_rotate_image_func, [image], tf.uint8)
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            sess.run(tf.local_variables_initializer())
            results = sess.run(image_rotate)
            image_2d = image_rotate
            image_2d_scaled = (np.maximum(image_2d, 0) / image_2d.max() if image_2d.max() else 1) * 255.0
            image_2d_scaled = np.int(image_2d_scaled)
            plt.imshow(image_2d_scaled, cmap=plt.cm.gray)
            plt.show()


npy_file = "D:/workspace/MedicalImageWorkspace/FCN-BoundingBox/original_npy/0001.npy"
my_npy = np.load(npy_file)
random_rotate_image(my_npy[:,:, 25], 1)