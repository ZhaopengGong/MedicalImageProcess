# -*- coding: utf-8 -*-
# 转换坐标的图形化界面调用了convertCoordinateWindows,ConvertCoordinateWorkThread
import sys
from ConvertCoordinateWindow import ConvertCoordinateWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.processEvents()  # 防止卡死
    myShow = ConvertCoordinateWindow()
    myShow.show()
    sys.exit(app.exec_())