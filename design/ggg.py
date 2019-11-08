
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

class MyFigure(FigureCanvas, QWidget):
    def __init__(self,parent=None, minWidth=600,  minHeight=380,  dpi=120):
        #第一步：创建一个创建Figure
        self.fig = Figure(figsize=(8, 8), dpi=dpi)
        #第二步：在父类中激活Figure窗口
        super(MyFigure,self).__init__(self.fig) #此句必不可少，否则不能显示图形
        #第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = self.fig.add_subplot(111)
        self.setMinimumSize(minWidth, minHeight)
        FigureCanvas.updateGeometry(self)
    #第四步：就是画图，【可以在此类中画，也可以在其它类中画】
    #画日分布图
    def drawDayChart(self):
        periodHour=['0'+str(i) if i<10 else str(i) for i in range(24)]
        periodDict=dict(zip(periodHour,  [0]*24))
        with open('configFiles/history.txt',  'r') as f:
            lines=f.readlines()
            for line in lines:
                period=line[11:13]
                periodDict[period]+=1
        periodDictKeys=periodDict.keys()
        periodDictValues=periodDict.values()
        #实现刷新的条件1
        self.axes.clear()
        rects=self.axes.bar(periodDictKeys,  periodDictValues,  align='edge',  width=0.9,  color='green')
        #实现刷新的条件2
        self.fig.canvas.draw_idle()
        self.axes.set_ylabel('番茄钟个数')
        self.axes.set_title('番茄钟日分布', color='blue')
        for rect in rects:
            x=rect.get_x()
            y=rect.get_height()
            if(y==0):
                continue
            self.axes.text(x,  1.01*y,  str(y),  va='bottom')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MyFigure()
    ui.show()
    sys.exit(app.exec_())