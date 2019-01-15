import matplotlib.pyplot as plt
import numpy as np

# image_file_path = 'F:/DeepLearing/source_code/miccai17-mmwhs-hybrid/image/0001.npy'
# label_file_path = 'F:/DeepLearing/source_code/miccai17-mmwhs-hybrid/label/0001.npy'

# image_file = (np.load(image_file_path))[:,:,150]
# label_file = (np.load(label_file_path))[:,:,150]

# fig = plt.figure()
# ax1 = fig.add_subplot(121)
# ax1.imshow(image_file, cmap=plt.cm.gray)
# ax2 = fig.add_subplot(122)
# ax2.imshow(label_file, cmap=plt.cm.gray)

# plt.show()


label_file_path = 'C:/Users/Administrator/Desktop/image/DG/0005_left.npy'
label_file = (np.load(label_file_path))[0,:,:,24]
for x in range(48):
    for y in range(48):
        if label_file[x,y] == 1 or label_file[x,y]== 9 or label_file[x,y]== 10 or label_file[x,y]== 11:
            label_file[x,y] = 0
plt.imshow(label_file, cmap=plt.cm.gray)
plt.show()