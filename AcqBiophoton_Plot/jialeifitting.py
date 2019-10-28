import matplotlib
import matplotlib.cm as cmx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import re
import numpy as np
import math
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
import random
import numpy as np


import os

def getIndexes(y_predict, y_data):
    y_predict=np.array(y_predict)
    y_data=np.array(y_data)
    n = y_data.size
    # SSE为和方差
    SSE = ((y_data - y_predict) ** 2).sum()
    # MSE为均方差
    MSE = SSE / n
    # RMSE为均方根,越接近0，拟合效果越好
    RMSE = np.sqrt(MSE)

    # 求R方，0<=R<=1，越靠近1,拟合效果越好
    u = y_data.mean()
    SST = ((y_data - u) ** 2).sum()
    SSR = SST - SSE
    R_square = SSR / SST
    return SSE, MSE, RMSE, R_square


def printPath(pathtemp,fun,num):
    marklist=["^","o","d"]
    ylist=[]
    yfitlist=[]
    colors=[]
    colorlist=['black','blue','red']
    # pathtemp=eval(repr(pathtemp).replace('\\', '@'))
    path=pathtemp+"处理后的原始数据/"
    # 所有文件夹，第一个字段是次目录的级别
    dirList = []
    # 所有文件
    fileList = []
    # 返回一个列表，其中包含在目录条目的名称
    files = os.listdir(path)
    #print(files)
    # 先添加目录级别
    for f in files:
        if (os.path.isdir(path + '/' + f)):
            # 排除隐藏文件夹。因为隐藏文件夹过多
            if (f[0] == '.'):
                pass
            else:
                # 添加非隐藏文件夹
                dirList.append(f)
        if (os.path.isfile(path + '/' + f)):
            # 添加文件
            fileList.append(f)
    titletext=fileList[0].split()
    #print(fileList[0])
    # title=titletext[0]+titletext[1]+"实验数据图"
    title=fileList[0]+"实验数据图"
    colornum=0
    dt=0
    markernum=0
    for fl in fileList:
        x=[]
        y=[]

        # 打印文件
        #print(fl)
        f = open(path + fl)  # 读取完txt再读txt里面的类容
        alllines = f.readlines()

        for eachLine in alllines:
            eachdata = eachLine.split()
            x.append(float(eachdata[0]))
            y.append(float(eachdata[1]))
            #dt=float(eachdata[2])
        # print(z)
        # print(x)
        # print(y)
        #ax.plot(x,y,z,label=fl)
        # plt.plot(x,y,label=fl)
        #color = plt.cm.Set2(random.choice(range(plt.cm.Set2.N)))
        #dz = hist.flatten()
        # color = plt.cm.Set2(random.choice(range(plt.cm.Set2.N)))
        # colors.append(color)
        color=colorlist[colornum]
        colornum+=1
        if(fun==4 or fun==2):
            # plt.scatter(x,y,color=color,label=re.sub(r'[A-Za-z]',"", fl.split("-")[1]),marker="*",s=0.8,facecolors='none')  #张老师数据
            plt.scatter(x, y, color=color, label=fl.split(".")[0].split("-")[0], marker=marklist[markernum], s=20)  # 佳蕾姐数据
        elif(fun==6):
            xbar=np.asarray(x)+(dt/2)
            ybar=np.asarray(y)/dt
            plt.bar(xbar,ybar,color=color,width=dt,alpha=0.5,marker=marklist[markernum])
            # plt.scatter(x,y,color=color,label=fl.split(".")[0],marker="*",s=0.8)        #佳蕾姐数据
            # plt.scatter(x,y,color=color,label=re.sub(r'[A-Za-z]',"", fl.split("-")[1]),marker="o")
        ylist.append(y)
        markernum+=1
    fitingpath=""
    #拟合曲线
    if (fun == 1):
        fitingpath=pathtemp+"拟合结果/"
    if (fun == 2):
        fitingpath=pathtemp+"指数拟合结果/"
    if (fun == 3):
        fitingpath=pathtemp+"拟合结果/"
    if (fun == 4):
        fitingpath=pathtemp+"双曲线拟合结果/"
    if (fun == 5):
        fitingpath = pathtemp + "拟合结果/"
    if (fun == 6):
        fitingpath=pathtemp+"双曲线积分形式拟合结果/"
    print("fitingpath"+fitingpath)
    files = os.listdir(fitingpath)
    # print(files)
    # 先添加目录级别

    fileList2=[]
    #print(files)
    for f in files:
        if (os.path.isdir(fitingpath + '/' + f)):
            #print(f)
            # 排除隐藏文件夹。因为隐藏文件夹过多
            if (f[0] == '.'):
                pass
            else:
                # 添加非隐藏文件夹
                dirList.append(f)
        if (os.path.isfile(fitingpath + '/' + f)):
            #print(f)
            # 添加文件
            fileList2.append(f)
    #print(fileList2)
    colornum=0
    for fl in fileList2:
        # 打印文件
        f = open(fitingpath + fl)  # 读取完txt再读txt里面的类容
        print(f)
        alllines = f.readlines()
        eachdata=alllines[num].split()
        print(eachdata[0])
        xfit=np.linspace(x[0],x[-1],1000)
        yfit=0
        yfitspot=0
        flmain=""
        if(fun==1):
            s1 = float(eachdata[0])
            s2 = float(eachdata[1])
            s3 = float(eachdata[2])
            s4 = float(eachdata[3])
            s5 = float(eachdata[4])
            fun = float(eachdata[7])
            yfit = s1 * ((s2 + (xfit / s3)) ** (-s4)) + s5
            yfitspot = s1 * ((s2 + (np.asarray(x) / s3)) ** (-s4)) + s5
        elif(fun==2):
            s1 = float(eachdata[0])
            s2 = float(eachdata[1])
            s3 = float(eachdata[2])
            fun = float(eachdata[5])
            yfit = s1 * (np.exp(-(xfit / s2))) +s3
            yfitspot =  s1 * (np.exp(-(np.asarray(x) / s2))) +s3
            flmain = re.sub(r'[A-Za-z]', "", fl.split("-")[1])
            # flmain=fl  #姐蕾姐数据
            #flmain = flmain + "指数拟合" + "(优度：" + eachdata[-3] + ")"        #张老师数据
        elif(fun==3):
            s1 = float(eachdata[0])
            s2 = float(eachdata[1])
            s3 = float(eachdata[2])
            s4 = float(eachdata[3])
            s5 = float(eachdata[4])
            fun = float(eachdata[7])
            yfit = 0
            yfitspot = 0
        elif(fun==4):
            s1 = float(eachdata[0])
            s2 = float(eachdata[1])
            s3 = float(eachdata[2])
            s4 = float(eachdata[3])
            s5 = float(eachdata[4])
            fun = float(eachdata[7])
            yfit = s1 * ((s2 + (xfit / s3)) ** (-s4)) + s5
            yfitspot = s1 * ((s2 + (np.asarray(x) / s3)) ** (-s4)) + s5
            #flmain = re.sub(r'[A-Za-z]', "", fl.split("-")[1])         #张老师拟合
            flmain =fl.split(".")[0].split("-")[0]    #佳蕾姐拟合
            flmain = flmain + "双曲线拟合" + "(优度：" + eachdata[-3] + ")"
        elif(fun==5):
            s1 = float(eachdata[0])
            s2 = float(eachdata[1])
            s3 = float(eachdata[2])
            s4 = float(eachdata[3])
            s5 = float(eachdata[4])
            fun = float(eachdata[7])
            yfit = s1 * math.exp(-(xfit/s2)) + s3
            yfitspot = s1 * ((s2 + (np.asarray(x) / s3)) ** (-s4)) + s5
        elif(fun==6):
            xfit = np.linspace(x[0], x[-1]+(x[1]-x[0]), 1000)
            s1 = float(eachdata[0])
            s2 = float(eachdata[1])
            s3 = float(eachdata[2])
            s4 = float(eachdata[3])
            s5 = float(eachdata[4])
            print(s1,s2,s3,s4,s5)
            TimeSpan=float(eachdata[7])
            # fun = float(eachdata[7])
            temp1=(1/(1+xfit/s3))**(s4-1)
            temp2=(1/(1+(xfit+TimeSpan)/s3))**(s4-1)
            temp1spot=(1/(1+np.asarray(x)/s3))**(s4-1)
            temp2spot=(1/(1+(np.asarray(x)+TimeSpan)/s3))**(s4-1)
            yfit = s1 * ((s2 + (xfit / s3)) ** (-s4)) + s5
            yfitspot = s1 * s3*(1/(s4-1))*(temp1spot-temp2spot)+s5*TimeSpan
            #flmain = re.sub(r'[A-Za-z]', "", fl.split("-")[1]) #张老师数据必要过程
            flmain = flmain + "双曲线积分拟合" + "(优度：" + eachdata[-3] + ")"
        yfitlist.append(yfitspot)
        color=colorlist[colornum]
        colornum+=1
        plt.plot(xfit,yfit,color=color,label=flmain,linewidth=1)
        # for eachLine in alllines:
        #     eachdata = eachLine.split()
        #     x.append(float(eachdata[0]))
        #     y.append(float(eachdata[1]))
    # print(colors)

    for i in range(len(ylist)):
        print(getIndexes(yfitlist[i],ylist[i]))
    # plt.title(title.split(".")[0])
    plt.text(2.5, 80000, "${I}$ = ${I_0}$*(1+${t_0}$/${\\tau}$)${^{-\gamma}}$+D", size=28,style="italic")
    plt.xlabel("time/ms",size=12)
    plt.ylabel("cps",size=12)
    font1={'size': 20}
    plt.legend(prop=font1)
    plt.show()

# printPath("C:/Users/ENERGY/Desktop/finall2/处理后的原始数据/")
# printPath("C:/Users/ENERGY/Desktop/新建文件夹 (2)/")
# printPath("C:/Users/ENERGY/Documents/WeChat Files/wxid_0092780902712/FileStorage/File/2019-10/20190924/",0)
#printPath("C:/Users/ENERGY/Desktop/工作文件/finall2/",6,0)
printPath("C:/Users/ENERGY/Desktop/工作文件/佳蕾姐曲线/",4,0)
# printPath("C:/Users/ENERGY/Desktop/工作文件/张老师穴位/",4,0)


# printPath("C:/Users/ENERGY/Desktop/新建文件夹 (3)/",0)

