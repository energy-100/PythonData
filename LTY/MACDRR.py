# -*- coding=utf-8 -*-
import csv    #加载csv包便于读取csv文件

#csv_file=open('MA_L.csv',encoding='gb18030')    #打开csv文件
csv_file=open('MA_L.csv',encoding='utf-8',errors='ignore')    #打开csv文件
csv_file2=open('MA_M.csv',encoding='utf-8',errors='ignore')
csv_file3=open('MA_S.csv',encoding='utf-8',errors='ignore')
data=dict()
csv_reader_lines = csv.reader(csv_file)
for one_line in csv_reader_lines:
    keys=str(one_line[0])
    value=str(one_line[1])
    data[keys]=value
    #print(data.get(keys))
print(len(data))
csv_reader_lines = csv.reader(csv_file2)
for one_line in csv_reader_lines:
    keys=str(one_line[0])
    value=str(one_line[1])
    data[keys]=value
    #print(data.get(keys))
print(len(data))
csv_reader_lines = csv.reader(csv_file3)
for one_line in csv_reader_lines:
    keys = str(one_line[0])
    value = str(one_line[1])
    data[keys] = value
    #print(data.get(keys))
print(len(data))


