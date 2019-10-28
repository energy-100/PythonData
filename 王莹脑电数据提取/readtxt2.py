import os
import xlwt
import xlrd
from xlutils.copy import copy
allFileNum = 0
def printPath(level, pathtemp,name):
    path=pathtemp+name+"/"
    if(os.path.exists(pathtemp+"WangYing.xls")):
        book1 = xlrd.open_workbook(pathtemp+"WangYing.xls")
        book = copy(book1)
    else:
        book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet(name, cell_overwrite_ok=True,)
    row = 0
    global allFileNum
    '''''
    打印一个目录下的所有文件夹和文件
    '''
    # 所有文件夹，第一个字段是次目录的级别
    dirList = []
    # 所有文件
    fileList = []
    # 返回一个列表，其中包含在目录条目的名称
    files = os.listdir(path)
    #print(files)
    # 先添加目录级别
    dirList.append(str(level))
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
    # 当一个标志使用，文件夹列表第一个级别不打印
    i_dl = 0
    for dl in dirList:
        if (i_dl == 0):
            i_dl = i_dl + 1
        else:
            # 打印至控制台，不是第一个的目录
            #print('-' * (int(dirList[0])), dl)
            # 打印目录下的所有文件夹和文件，目录级别+1
            printPath((int(dirList[0]) + 1), path + '/' + dl)
    sheet.write(0,0,"编号")
    sheet.write(0,1,"姓名")
    sheet.write(0,2,"Team")
    sheet.write(0,3,"Time")
    sheet.write(0,4,"State")
    sheet.write(0,5,"Point")
    sheet.write(0,6,"max")
    sheet.write(0,7,"latency")

    row=row+1
    filenum = 0
    f = open(pathtemp + "name.txt",encoding = 'UTF-8')
    namedata=f.readlines()
    dict={}
    for line in namedata:
        line = line.split()
        dict[line[0]]=line[1]

    #print(dict)
    for fl in fileList:
        # 打印文件
        #print(fl)
        f = open(path + fl)  # 读取完txt再读txt里面的类容
        #print(path + fl)
        #print(f.read())
        # 'a'表示附加模式，用写入模式‘w'要小心，如果指定文件已经存在，python将再返回文件对象前清空该文件
        #f2 = open("20170610uid.txt", 'a')
        #f2.write(f.read())
        # 以下三行是逐行读取，跟f2.write(f.read())效果一样
        alllines = f.readlines()
        alllinesmain=alllines[5:-1]
        #print("开始")
        for eachLine in alllinesmain:
            #print(eachLine)
            eachLine = eachLine.split()
            eachLine[0]=eachLine[0].replace('-A1,A2',"")
            #print(eachLine[0],"\t",eachLine[1])
            sheet.write(row, 0, fl[0:3])
            sheet.write(row, 1, dict[fl[0:3]])
            sheet.write(row, 2, fl[0])
            sheet.write(row, 3, name[1])
            if (fl[-6]=="+"):
                if(fl[-5]=="3"):
                    sheet.write(row, 4, 7)
                else:
                    sheet.write(row, 4, 8)
            else:
                sheet.write(row, 4, int(fl[-5]))
                #print(fl)
            # if((((filenum)%8)+1)==5):
            #     sheet.write(row, 4, 7)
            # elif((((filenum)%8)+1)==6):
            #     sheet.write(row, 4, 8)
            # elif ((((filenum) % 8) + 1) == 7):
            #     sheet.write(row, 4, 5)
            # elif((((filenum)%8)+1)==8):
            #     sheet.write(row, 4, 6)
            # else:
            #     sheet.write(row, 4, (((filenum)%8)+1))
            sheet.write(row, 5, eachLine[0])
            sheet.write(row, 6, eachLine[4])
            sheet.write(row, 7, eachLine[5])

            row=row+1
        #   f2.write(eachLine)
        #print("结束")
        #f2.close()
        # 随便计算一下有多少个文件
        allFileNum = allFileNum + 1
        #print(allFileNum)
        filenum=filenum+1
    book.save(pathtemp+"WangYing.xls")
if __name__ == '__main__':
    printPath(1, 'C:/Users/ENERGY/Desktop/',"A-T1-N1")
    print("1-done")
    printPath(1, 'C:/Users/ENERGY/Desktop/', "A-T2-N1")
    print("1-done")
