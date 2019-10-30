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
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset


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
    plt.figure(figsize=(10, 10))
    plt.subplot(2, 1, 1)
    ylist=[]
    yfitlist=[]
    colors=[]
    paras=[]
    col_labels=[]
    row_labels=[]
    colorlist=['black','red','blue','yellow','green']
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
    title=titletext[0]+titletext[1]+"实验数据图"
    # title=ftitletext+"实验数据图"
    colornum=0
    dt=0
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
            dt=float(eachdata[2])
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
            plt.scatter(x,y,color=color,label=re.sub(r'[A-Za-z]',"", fl.split("-")[1]),marker="*")  #张老师数据
            # plt.scatter(x, y, color=color, label=fl.split(".")[0], marker="*", s=0.8)  # 佳蕾姐数据
        elif(fun==6 or fun==5):
            xbar=np.asarray(x)+(dt/2)
            ybar=np.asarray(y)/dt
            plt.bar(xbar,ybar,color=color,width=dt,alpha=0.5)
            # plt.scatter(x,y,color=color,label=fl.split(".")[0],marker="*",s=0.8)        #佳蕾姐数据
            # plt.scatter(x,y,color=color,label=re.sub(r'[A-Za-z]',"", fl.split("-")[1]),marker="o")
        ylist.append(y)
    fitingpath=""
    #拟合曲线
    if (fun == 1):
        fitingpath=pathtemp+"拟合结果/"
    if (fun == 2):
        fitingpath=pathtemp+"指数拟合结果/"
        paras.append(["测量点", "${I_0}$", "${\\tau}$", "D", "${R^2}$"])
    if (fun == 3):
        fitingpath=pathtemp+"拟合结果/"
    if (fun == 4):
        fitingpath=pathtemp+"双曲线拟合结果/"
    if (fun == 5):
        fitingpath = pathtemp + "指数积分形式拟合结果/"
        paras.append(["测量点", "${I_0}$", "${\\tau}$", "D", "${R^2}$"])
    if (fun == 6):
        fitingpath=pathtemp+"双曲线积分形式拟合结果/"
        paras.append(["测量点","${I_0}$","s2","${\\tau}$","${\gamma}$","D", "${R^2}$"])
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
            rs = float(eachdata[5])
            paras.append([s1,s2,s3,s4,s5,rs])
            col_labels=["s1","s2","s3","s4","s5", "${R^2}$"]
            yfit = s1 * ((s2 + (xfit / s3)) ** (-s4)) + s5
            yfitspot = s1 * ((s2 + (np.asarray(x) / s3)) ** (-s4)) + s5
        elif(fun==2):
            s1 = float(eachdata[0])
            s2 = float(eachdata[1])
            s3 = float(eachdata[2])
            r2 = float(eachdata[3])

            yfit = s1 * (np.exp(-(xfit / s2))) +s3
            yfitspot =  s1 * (np.exp(-(np.asarray(x) / s2))) +s3
            flmain = re.sub(r'[A-Za-z]', "", fl.split("-")[1])
            # flmain=fl  #姐蕾姐数据
            # flmain2 = flmain + "指数拟合" + "(优度：" + eachdata[-3] + ")"
            flmain2 = flmain + "指数拟合"
            paras.append([flmain,s1,s2,s3,r2])
        elif(fun==3):
            s1 = float(eachdata[0])
            s2 = float(eachdata[1])
            s3 = float(eachdata[2])
            s4 = float(eachdata[3])
            s5 = float(eachdata[4])
            r2 = float(eachdata[5])
            paras.append([s1,s2,s3,s4,s5,r2])
            yfit = 0
            yfitspot = 0
        elif(fun==4):
            s1 = float(eachdata[0])
            s2 = float(eachdata[1])
            s3 = float(eachdata[2])
            s4 = float(eachdata[3])
            s5 = float(eachdata[4])
            r2 = float(eachdata[5])
            paras.append([s1,s2,s3,s4,s5,r2])
            yfit = s1 * ((s2 + (xfit / s3)) ** (-s4)) + s5
            yfitspot = s1 * ((s2 + (np.asarray(x) / s3)) ** (-s4)) + s5
            flmain = re.sub(r'[A-Za-z]', "", fl.split("-")[1])         #张老师拟合
            # flmain =fl.split(".")[0]     #佳蕾姐拟合
            flmain = flmain + "双曲线拟合" + "(优度：" + eachdata[-3] + ")"
        elif(fun==5):
            print(eachdata)
            s1 = float(eachdata[0])
            s2 = float(eachdata[1])
            s3 = float(eachdata[2])
            r2 = float(eachdata[3])
            TimeSpan = float(eachdata[5])
            yfit = s1 * np.exp(-(xfit/s2)) + s3
            temp1spot=np.exp(-np.asarray(x)/s2)
            temp2spot=np.exp(-(np.asarray(x)+TimeSpan)/s2)
            yfitspot = s1 * s2*(temp1spot-temp2spot) + s3*TimeSpan
            flmain = re.sub(r'[A-Za-z]', "", fl.split("-")[1])
            paras.append([flmain,s1,s2,s3,r2])
            flmain2 = flmain + "指数积分拟合"
            # flmain=fl  #姐蕾姐数据
            # flmain2 = flmain + "指数积分形式拟合" + "(优度：" + eachdata[-3] + ")"
        elif(fun==6):
            xfit = np.linspace(x[0], x[-1]+(x[1]-x[0]), 1000)
            s1 = float(eachdata[0])
            s2 = float(eachdata[1])
            s3 = float(eachdata[2])
            s4 = float(eachdata[3])
            s5 = float(eachdata[4])
            rs = float(eachdata[5])
            col_labels = ["测量点","s1", "s2", "s3", "s4", "s5", "${R^2}$"]

            # print(s1,s2,s3,s4,s5)
            TimeSpan=float(eachdata[7])
            # fun = float(eachdata[7])
            temp1spot=(1/(1+np.asarray(x)/s3))**(s4-1)
            temp2spot=(1/(1+(np.asarray(x)+TimeSpan)/s3))**(s4-1)
            yfit = s1 * ((s2 + (xfit / s3)) ** (-s4)) + s5
            yfitspot = s1 * s3*(1/(s4-1))*(temp1spot-temp2spot)+s5*TimeSpan
            flmain = re.sub(r'[A-Za-z]', "", fl.split("-")[1]) #张老师数据必要过程
            # flmain = flmain + "双曲线积分拟合" + "(优度：" + eachdata[-3] + ")"
            paras.append([flmain,s1,s2,s3,s4,s5,rs])
            flmain2 = flmain + "双曲线积分拟合"
        yfitlist.append(yfitspot)
        color=colorlist[colornum]

        colornum+=1
        plt.plot(xfit,yfit,color=color,label=flmain2)
        row_labels.append(flmain)
        # for eachLine in alllines:
        #     eachdata = eachLine.split()
        #     x.append(float(eachdata[0]))
        #     y.append(float(eachdata[1]))
    # print(colors)
    # col_labels = ['col1', 'col2', 'col3']
    # row_labels = ['row1', 'row2', 'row3']
    # table_vals = [[11, 12, 13], [21, 22, 23], [28, 29, 30]]
    # row_labels=["1","2"]
    paras=np.array(paras).T
    # plt.table(cellText=paras,colWidths=[4]*len(col_labels),rowLabels=row_labels, colLabels=col_labels,loc='top',fontsize=5.0,picker=0.5)
         #转置
    # plt.table(cellText=paras,rowLabels=row_labels,loc='best', colLabels=col_labels)
    for i in range(len(ylist)):
        print(getIndexes(yfitlist[i],ylist[i]))
    plt.title(title)
    plt.xlabel("time/ms",size=12)
    plt.ylabel("cps",size=12)
    font1={'size': 10}
    plt.legend(prop=font1)
    plt.legend()
    # plt.table(cellText=paras, colWidths=[0.1,0.1], rowLabels=col_labels, loc='best', colLabels=row_labels,in_layout="TRUE",
    #           fontsize=20)  # 转置
    plt.subplot(2, 1, 2,frameon=True, xticks=[], yticks=[])
    plt.gca().spines['right'].set_color('none')
    plt.gca().spines['top'].set_color('none')
    plt.gca().spines['bottom'].set_color('none')
    plt.gca().spines['left'].set_color('none')
    # print(paras)
    # print(len(col_labels))
    the_table=plt.table(cellText=paras, colWidths=[0.12] * len(paras),
               fontsize=5, loc='center',cellLoc='center')
    plt.title('参数列表')
    # the_table=plt.table(cellText=paras, colWidths=[0.2] * len(col_labels), rowLabels=col_labels,
    #           colLabels=row_labels, fontsize=5, alpha=0.5,loc='center',cellLoc='center')
    the_table.set_fontsize(20)
    the_table.scale(2.5, 2.58)
    plt.show()

# printPath("C:/Users/ENERGY/Desktop/finall2/处理后的原始数据/")
# printPath("C:/Users/ENERGY/Desktop/新建文件夹 (2)/")
# printPath("C:/Users/ENERGY/Documents/WeChat Files/wxid_0092780902712/FileStorage/File/2019-10/20190924/",0)
printPath("C:/Users/ENERGY/Desktop/工作文件/finall2/",5,1)
# printPath("C:/Users/ENERGY/Desktop/工作文件/佳蕾姐曲线/",4,0)


# printPath("C:/Users/ENERGY/Desktop/新建文件夹 (3)/",0)

