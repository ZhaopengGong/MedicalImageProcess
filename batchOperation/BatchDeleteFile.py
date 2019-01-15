import os


folder_path = "E:/桌面文件夹/64例标注数据组合后nii"
for patient_folder in os.listdir(folder_path):
    print("正在处理"+patient_folder)
    sub_folder_path = os.path.join(folder_path, patient_folder)
    filename = os.path.join(sub_folder_path, 'dcmHeaders.mat')
    os.remove(filename)