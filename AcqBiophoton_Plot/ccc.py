import matplotlib
import matplotlib.cm as cmx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
import random


import os
def printPath(pathtemp):
    path=pathtemp
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
    i=1
    fig = plt.figure()
    ax = fig.gca(projection='3d')
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
        z=np.linspace(i*0.01,i*0.01,len(x))
        i+=1
        z=z.tolist()
        # print(z)
        # print(x)
        # print(y)
        #ax.plot(x,y,z,label=fl)
        # plt.plot(x,y,label=fl)
        color = plt.cm.Set2(random.choice(range(plt.cm.Set2.N)))
        #dz = hist.flatten()
        ax.bar(x,y,zs=z, zdir='y',alpha=1,label=fl)

    ax.set_title("3D")
    ax.set_xlabel("time/ms")
    ax.set_ylabel("cps")
    ax.set_zlabel("曲线编号")
    # plt.legend()
    plt.show()
# printPath("C:/Users/ENERGY/Desktop/finall2/处理后的原始数据/")
printPath("C:/Users/ENERGY/Desktop/新建文件夹 (2)/处理后的原始数据/")

