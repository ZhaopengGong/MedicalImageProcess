from conver_xy import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
# 引入我们创建的线程
from ConvertCoordinateWorkThread import ConvertCoordinateWorkThread


class ConvertCoordinateWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(ConvertCoordinateWindow, self).__init__()
        self.setupUi(self)

        self.sourceLabel_btn.clicked.connect(self.openSourceLabelDirectory)
        self.HF_source_path_btn.clicked.connect(self.openHouseFieldDirectory)
        self.conver_coordinate.clicked.connect(self.converCoordinate)

    # 选择原始标注数据的文件夹
    def openSourceLabelDirectory(self):
        source_label_folder = QFileDialog.getExistingDirectory()
        # 重新选择的时候隐藏校准的提示信息
        self.convert_process_label.setText("")
        self.sourceLabel_path_edit.setText(source_label_folder)

    # 选择生成的转换后数据的文件夹
    def openHouseFieldDirectory(self):
        house_field_folder = QFileDialog.getExistingDirectory()
        # 重新选择的时候隐藏校准的提示信息
        self.convert_process_label.setText("")
        self.grayValue_path_edit.setText(house_field_folder)

    # 坐标转换
    def converCoordinate(self):
        label_root_dir = self.sourceLabel_path_edit.toPlainText()
        coordinate_root_dir = self.grayValue_path_edit.toPlainText()
        # 新建对象，传入参数
        self.convertCoordinateWorkThread = ConvertCoordinateWorkThread(label_root_dir, coordinate_root_dir)
        self.convertCoordinateWorkThread.start()
        # 连接工作进程的信号槽当工作进程执行完毕的时候发来信号，界面显示坐标校准完毕
        self.convertCoordinateWorkThread.finishSignal.connect(self.convertCoordinateEnd)
        self.convertCoordinateWorkThread.convertProcessSignal.connect(self.convertCoordinateProcess)

    def convertCoordinateProcess(self, info):
        self.convert_process_label.setText(info)

    def convertCoordinateEnd(self):
        self.convert_process_label.setText('校准完毕')