import sys
import matplotlib
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
matplotlib.use("Qt5Agg")
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QSizePolicy, QPushButton,QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os
from PyQt5.QtWidgets import *

class Mydemo(FigureCanvas):
    def __init__(self):
        super(Mydemo, self).__init__()
    def initUi(self,parent=None, width=5, height=4, dpi=100):
        plt.rcParams['font.family'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(2, 1, 1)
        self.axes1 = self.fig.add_subplot(2, 1, 2)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)       #是否跟随外部控件放大缩小
        FigureCanvas.updateGeometry(self)
        self.btn_start = QtWidgets.QPushButton("读取文件夹",self)
        self.btn_start.clicked.connect(self.openfile)

        self.layout = QVBoxLayout(self)
        self.figure1 = Mydemo(width=5, height=4, dpi=100)
        self.layout.addWidget(self.figure1)
        data = list(range(1000))
        self.figure1.axes.plot(data)
        self.figure1.axes1.plot(data)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "一颗数据小白菜"))


    def openfile(self):
        openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '', 'Excel files(*.xlsx , *.xls)')
class Try(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()



    def DataRead(self,FilePath):
        fileList=[]
        files = os.listdir(FilePath)
        for f in files:
            if (os.path.isfile(FilePath + '/' + f)):
                # 添加文件
                fileList.append(f)  #所有文件名
        return fileList



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Try()
    ui.show()
    sys.exit(app.exec_())