import sys
import matplotlib
import os
matplotlib.use("Qt5Agg")
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QSizePolicy, QWidget,QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
import numpy as np
from PyQt5.QtGui import QIcon

from PyQt5.QtCore import *

class Mydemo(FigureCanvas):
    def __init__(self, parent=None, width=100, height=50, dpi=100):

        plt.rcParams['font.family'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        self.fig = Figure(figsize=(width, height))
        self.axes = self.fig.add_subplot(1, 1, 1)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

# class SecondWindow(QWidget):
#     def __init__(self, parent=None):
#         super(SecondWindow, self).__init__(parent)
#         self.resize(200, 200)
#         self.setStyleSheet("background: black")
#         self.f1=Mydemo(width=5, height=3, dpi=100)
#         self.setWindowTitle('人体延迟发光数据画图软件')
#         self.grid = QGridLayout()
#         self.grid.setSpacing(10)
#         self.setLayout(self.grid)
#     def handle_click(self):
#         if not self.isVisible():
#             self.show()
#
#     def handle_close(self):
#         self.close()

class Try(QWidget):
    close_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle('人体延迟发光数据画图软件')
        self.setWindowIcon(QIcon('xyjk.png'))
        self.openfile_name = ""
        self.filenme = ""
        self.paratext = ""
        self.ordata=[]
        self.plotlist=[]
        self.fun=0
        self.initUi()


    def tab1UI(self):

        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        self.figure1 = Mydemo(width=5, height=3, dpi=100)
        self.grid.addWidget(self.figure1, 1, 0, 1, 1)

        self.figure2 = Mydemo(width=5, height=3, dpi=100)
        self.grid.addWidget(self.figure2, 1, 1, 1, 1)

        self.figure3 = Mydemo(width=5, height=3, dpi=100)
        self.grid.addWidget(self.figure3, 2, 0, 1, 1)

        self.figure4 = Mydemo(width=5, height=3, dpi=100)
        self.grid.addWidget(self.figure4, 2, 1, 1, 1)

        self.listwidget1 = QListWidget(self)
        self.grid.addWidget(self.listwidget1, 3, 0, 1, 1)
        self.listwidget1.clicked.connect(lambda: self.listwidget1_clicked())

        self.listwidget2 = QListWidget(self)
        self.grid.addWidget(self.listwidget2, 3, 1, 1, 1)
        self.listwidget2.clicked.connect(lambda: self.listwidget2_clicked())

        self.listwidget3 = QListWidget(self)
        self.grid.addWidget(self.listwidget3, 4, 0, 1, 2)
        self.listwidget3.clicked.connect(lambda: self.listwidget3_clicked())

        self.loadfileButton = QPushButton("Load File", self)
        self.loadfileButton.clicked.connect(self.openfile)
        self.grid.addWidget(self.loadfileButton, 5, 0, 1, 1)

        self.loadfileButton = QPushButton("big", self)
        # self.loadfileButton.clicked.connect(self.big)
        self.grid.addWidget(self.loadfileButton, 5, 1, 1, 1)

        self.loadfileButton = QPushButton("Delete File", self)
        self.loadfileButton.clicked.connect(self.fitting)
        self.grid.addWidget(self.loadfileButton, 6, 0, 1, 1)

        self.loadfileButton = QPushButton("Save Image", self)
        self.loadfileButton.clicked.connect(self.SaveImage)
        self.grid.addWidget(self.loadfileButton, 6, 1, 1, 1)

        self.loadfileButton = QPushButton("openchild", self)
        self.loadfileButton.clicked.connect(self.openchild)
        self.grid.addWidget(self.loadfileButton, 7, 0, 1, 1)

        self.loadfileButton1 = QPushButton("child", self)
        self.grid.addWidget(self.loadfileButton1, 7, 1, 1, 1)

        self.openfile_name = "C:/Users/ENERGY/Desktop/工作文件/lhy"
        files = self.FileRead(self.openfile_name + "/处理后的原始数据")
        self.listwidget1.clear()
        self.listwidget1.addItems(files)
        self.tab1.setLayout(self.grid)

        self.openfile_name = "C:/Users/ENERGY/Desktop/工作文件/lhy"
        files=self.FileRead(self.openfile_name+ "/处理后的原始数据")
        self.listwidget1.clear()
        self.listwidget1.addItems(files)

    def initUi(self):
        print()
        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.setLayout(self.grid)

        self.figure1 = Mydemo(width=5, height=3, dpi=100)
        self.grid.addWidget(self.figure1,1,0,1,1)

        self.figure2 = Mydemo(width=5, height=3, dpi=100)
        self.grid.addWidget(self.figure2,1,1,1,1)

        self.figure3 = Mydemo(width=5, height=3, dpi=100)
        self.grid.addWidget(self.figure3,2,0,1,1)

        self.figure4 = Mydemo(width=5, height=3, dpi=100)
        self.grid.addWidget(self.figure4,2,1,1,1)

        self.listwidget1 = QListWidget(self)
        self.grid.addWidget(self.listwidget1,3,0,1,1)
        self.listwidget1.clicked.connect(lambda: self.listwidget1_clicked())



        self.listwidget2 = QListWidget(self)
        self.grid.addWidget(self.listwidget2,3,1,1,1)
        self.listwidget2.clicked.connect(lambda: self.listwidget2_clicked())

        self.listwidget3 = QListWidget(self)
        self.grid.addWidget(self.listwidget3,4,0,1,2)
        self.listwidget3.clicked.connect(lambda: self.listwidget3_clicked())

        self.loadfileButton = QPushButton("Load File",self)
        self.loadfileButton.clicked.connect(self.openfile)
        self.grid.addWidget(self.loadfileButton,5,0,1,1)

        self.loadfileButton = QPushButton("big",self)
        # self.loadfileButton.clicked.connect(self.big)
        self.grid.addWidget(self.loadfileButton,5,1,1,1)

        self.loadfileButton = QPushButton("Delete File",self)
        self.loadfileButton.clicked.connect(self.fitting)
        self.grid.addWidget(self.loadfileButton,6,0,1,1)

        self.loadfileButton = QPushButton("Save Image",self)
        self.loadfileButton.clicked.connect(self.SaveImage)
        self.grid.addWidget(self.loadfileButton,6,1,1,1)

        self.loadfileButton = QPushButton("openchild",self)
        self.loadfileButton.clicked.connect(self.openchild)
        self.grid.addWidget(self.loadfileButton,7,0,1,1)

        self.loadfileButton1 = QPushButton("child",self)
        self.grid.addWidget(self.loadfileButton1,7,1,1,1)



        self.openfile_name = "C:/Users/ENERGY/Desktop/工作文件/lhy"
        files=self.FileRead(self.openfile_name+ "/处理后的原始数据")
        self.listwidget1.clear()
        self.listwidget1.addItems(files)

    def openchild(self):
        print("fdsfsfsdf")


    def SaveImage(self):

        filename1 , _=os.path.splitext(QListWidgetItem(self.listwidget1.currentItem()).text())
        filename2 , _=os.path.splitext(QListWidgetItem(self.listwidget1.currentItem()).text())
        filename3 , _=os.path.splitext(QListWidgetItem(self.listwidget1.currentItem()).text())
        filename4 , _=os.path.splitext(QListWidgetItem(self.listwidget1.currentItem()).text())
        print("保存位置",self.openfile_name+"/"+filename1+"双曲线拟合图"+".jpg")
        # try:
        #     self.figure1.axes.savefig(self.openfile_name+"/"+filename1+"双曲线拟合图"+".png")
        # except Exception as err:
        #     print(err)
        #
        # self.figure2.axes.savefig(self.openfile_name+"/"+filename2+"指数拟合图"+".png")
        # self.figure3.axes.savefig(self.openfile_name+"/"+filename3+"双曲线积分拟合图"+".png")
        # self.figure4.axes.savefig(self.openfile_name+"/"+filename4+"指数积分拟合图"+".png")


        try:
            self.figure1.show()
        except Exception as err:
            print(err)

        self.figure2.show()
        self.figure3.show()
        self.figure4.show()


    def openfile(self):
        self.openfile_name = QFileDialog.getExistingDirectory(self, "请选择数据文件的根目录")
        files=self.FileRead(self.openfile_name+ "/处理后的原始数据")
        self.listwidget1.clear()
        self.listwidget1.addItems(files)

    def fitting(self):
        self.filenme=QListWidgetItem(self.listwidget1.currentItem()).text()
        self.paratext=QListWidgetItem(self.listwidget2.currentItem()).text()
        print(self.openfile_name + "/../处理后的原始数据/"+self.filenme)
        aaa=self.DataRead(self.openfile_name + "/../处理后的原始数据/"+self.filenme)
        self.ordata=np.loadtxt(self.openfile_name + "/../处理后的原始数据/"+self.filenme)
        self.ordata=self.ordata.astype(np.float64)
        print(self.ordata.dtype)
        self.figure1.fig.canvas.draw_idle()
        self.figure1.axes.clear()
        # self.figure1.axes1.clear()
        self.figure1.axes.plot(self.ordata[:, 0], self.ordata[:, 1])
        # self.figure1.axes1.plot(self.ordata[:, 0], self.ordata[:, 1])
        self.figure1.axes.set_ylabel('cps')
        self.figure1.axes.set_title('实验数据', color='black')



    def listwidget1_clicked(self):
        item = QListWidgetItem(self.listwidget1.currentItem()).text()
        self.ordata=np.loadtxt(self.openfile_name + "/处理后的原始数据/"+item)
        self.listwidget2.clear()
        if(os.path.exists(self.openfile_name+"\双曲线拟合\\"+item)):
            self.listwidget2.addItem("双曲线拟合")
            para=self.DataRead(self.openfile_name+"\双曲线拟合\\"+item)
            paras = [float(i) for i in para[0].strip('/n').split()]
            print("进入单击")
            self.plot(self.ordata[:,0],paras)
            print("单击结束")

        if (os.path.exists(self.openfile_name + "\指数拟合\\" + item)):
            self.listwidget2.addItem("指数拟合")
            para = self.DataRead(self.openfile_name + "\指数拟合\\" + item)
            paras = [float(i) for i in para[0].strip('/n').split()]
            print("进入指数单击")
            self.plot(self.ordata[:, 0], paras)
            print("单击结束")

        if (os.path.exists(self.openfile_name + "\双曲线积分形式拟合\\" + item)):
            self.listwidget2.addItem("双曲线积分形式拟合")
            para = self.DataRead(self.openfile_name + "\双曲线积分形式拟合\\" + item)
            paras = [float(i) for i in para[0].strip('/n').split()]
            self.plot(self.ordata[:, 0], paras)

        if (os.path.exists(self.openfile_name + "\指数积分形式拟合\\" + item)):
            self.listwidget2.addItem("指数积分形式拟合")
            para = self.DataRead(self.openfile_name + "\指数积分形式拟合\\" + item)
            paras = [float(i) for i in para[0].strip('/n').split()]
            print("进入单击")
            self.plot(self.ordata[:, 0], paras)
            print("单击结束")


    def listwidget2_clicked(self):
        item = QListWidgetItem(self.listwidget2.currentItem()).text()
        fitdata=self.DataRead(self.openfile_name+"\\"+item+"\\"+QListWidgetItem(self.listwidget1.currentItem()).text())
        print("fitdata",fitdata)
        self.listwidget3.clear()
        self.listwidget3.addItems(fitdata)
        self.SaveImage()


    def listwidget3_clicked(self):
        paras=QListWidgetItem(self.listwidget2.currentItem()).text().split()
        print("//////////////////////////////////")
        map(lambda x:float(x),paras)
        print(type(paras))
        self.plot(self.ordata[:, 0],paras)

    def plot(self,xdata,para):
        # print("进入plot",para)
        print(para[-1])
        if(para[-1]==4):  #双曲线画图
            print("进入画图")
            self.figure1.fig.canvas.draw_idle()
            self.figure1.axes.clear()
            xfit = np.linspace(xdata[0],xdata[-1],1000)
            yfit = self.creatFittingata(xfit,para)
            # print(self.ordata[:,0])
            # print(self.ordata[:,1])
            self.figure1.axes.scatter(self.ordata[:,0], self.ordata[:,1],s=0.5)
            self.figure1.axes.plot(xfit, yfit)
            # print(xfit)
            # print(yfit)
            self.figure1.axes.set_ylabel('cps')
            self.figure1.axes.set_xlabel('t')
            self.figure1.axes.set_title('双曲线拟合(${I}$ = ${I_0}$*(1+${t}$/${\\tau}$)${^{-\gamma}}$+D)', color='black')
        elif (para[-1] == 2):  # 指数画图
            self.figure2.fig.canvas.draw_idle()
            self.figure2.axes.clear()
            xfit = np.linspace(xdata[0],xdata[-1],1000)
            yfit = self.creatFittingata(xfit,para)
            # print(self.ordata[:,0])
            # print(self.ordata[:,1])
            self.figure2.axes.scatter(self.ordata[:,0], self.ordata[:,1],s=0.5)
            self.figure2.axes.plot(xfit, yfit)
            # print(xfit)
            # print(yfit)
            self.figure2.axes.set_ylabel('cps')
            self.figure2.axes.set_xlabel('t')
            self.figure2.axes.set_title('指数拟合(${I}$ = ${I_0}$e${^{-t/\\tau}}$+D)', color='black')

        elif (para[-1] == 6):  # 双曲线积分画图
            self.figure3.fig.canvas.draw_idle()
            self.figure3.axes.clear()
            dt=para[-2]
            xfit = np.linspace(xdata[0], xdata[-1]+dt, 1000)
            yfit = self.creatFittingata(xfit, para)
            xbar = np.asarray(self.ordata[:, 0]) + (dt / 2)
            ybar = np.asarray(self.ordata[:, 1]) / dt
            self.figure3.axes.bar(xbar, ybar, width=dt, alpha=0.5)
            # print(self.ordata[:,0])
            # print(self.ordata[:,1])
            self.figure3.axes.plot(xfit, yfit)
            # print(xfit)
            # print(yfit)
            self.figure3.axes.set_ylabel('cps')
            self.figure3.axes.set_xlabel('t')
            self.figure3.axes.set_title('双曲线积分拟合(${I}$ =$\int_t^{t+ \Delta t}$(${I_0}$*(1+${t}$/${\\tau}$)${^{-\gamma}}$+D)dt)', color='black')

        elif (para[-1] == 5):  # 指数积分画图
            self.figure4.fig.canvas.draw_idle()
            self.figure4.axes.clear()
            dt = para[-2]
            xfit = np.linspace(xdata[0], xdata[-1] + dt, 1000)
            yfit = self.creatFittingata(xfit, para)
            xbar = np.asarray(self.ordata[:, 0]) + (dt / 2)
            ybar = np.asarray(self.ordata[:, 1]) / dt
            self.figure4.axes.bar(xbar, ybar, width=dt, alpha=0.5)
            self.figure4.axes.plot(xfit, yfit)
            self.figure4.axes.set_ylabel('cps')
            self.figure4.axes.set_xlabel('t')
            self.figure4.axes.set_title(
                '指数积分拟合(${I}$ =$\int_t^{t+ \Delta t}$(${I_0}$e${^{-t/\\tau}}$+D)dt)', color='black')


    def creatFittingata(self,xdata,paras):
        print(paras)
        if (paras[-1]==2 or paras[-1]==5):
            print(1)
            return paras[0] * (np.exp(-(xdata / paras[1]))) + paras[2]
        if (paras[-1]==4 or paras[-1]==6):
            print(2)
            return paras[0] * ((paras[1] + (np.asarray(xdata) / paras[2])) ** (-paras[3])) + paras[4]


    def FileRead(self,FilesPath):
        fileList=[]
        files = os.listdir(FilesPath)
        for f in files:
            if (os.path.isfile(FilesPath + '/' + f)):
                fileList.append(f)  #所有文件名
        # print(fileList)
        return fileList

    def DataRead(self,Filepath):
        dataarray=[]
        data=open(Filepath)
        datalines=data.read().splitlines()
        return datalines




if __name__ == '__main__':



    app = QApplication(sys.argv)
    ui = Try()
    # s = SecondWindow()
    # ui.loadfileButton1.clicked.connect(s.handle_click)
    #
    # f11=ui.figure1.axes
    # s.f1.axes=f11
    # s.grid.addWidget(s.f1)
    # # s.grid.addWidget(f113)
    # ui.loadfileButton1.clicked.connect(ui.hide)
    # ui.close_signal.connect(ui.close)
    ui.show()
    sys.exit(app.exec_())