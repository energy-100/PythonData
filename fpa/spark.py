#!usr/bin/env python
# encoding:utf-8
# import numpy as np
#import mmh3
from bitarray import bitarray
# import pickle
from pyspark.sql import SparkSession
spark = SparkSession \
     .builder \
     .config("spark.debug.maxToStringFields",1000) \
     .appName("BloomFilter") \
     .getOrCreate()
# sc = spark.sparkContext
print('SessionCreate')
data_from_json = spark.read.json('C:/netflow.json')
# data_from_json.take(1)
data_from_json.printSchema()  # 查看数据结构，便于解析
data_from_json.withColumn("DNS"
                          , data_from_json["_source"]["netflow"]["appHost"]).show(5)
rdd1 = data_from_json.withColumn("DNS", data_from_json["_source"]["netflow"]["appHost"])
rdd2 = rdd1.select('DNS')
rdd2.show()
rdd3 = rdd2.dropDuplicates()  # 过滤重复域名


def f(dns, seed):
    data = 0
    for temp in dns:
        data = data * seed + ord(temp)
        #       data+=ord(temp)
    return data

rdd4=rdd3.rdd.map(lambda row: [f(row[0], 1) % 772231148,  # 哈希运算
                               f(row[0], 6) % 772231148,
                               f(row[0], 10) % 772231148,
                               f(row[0], 15) % 772231148,
                               f(row[0], 21) % 772231148,
                               f(row[0], 27) % 772231148,
                               f(row[0], 31) % 772231148,
                               f(row[0], 42) % 772231148,
                               ])
rdd4.take(1)

a = rdd4.collect()     # 数据下发到driver上
print(a)
b = bitarray(772231138)
b.setall(0)
# b=np.zeros(772231148)   # 构建零向量布隆存储器
# print(b)
for i in range(len(a)):      # 遍历rdd4 list a
    for j in range(len(a[i])):
        index = a[i][j]
        b[index] = 1
# print(a[i][j])
# print(b)
# del a
# b = open('a.txt', 'w')
# for value in a:
#     b.write(str(value))
# b.close()
# 监测
e = [17286700,
     100856919,
     42936594,
     45593537,
     767498689,
     476731564,
     276304981,
     352023805]
result = True
for i in e:
    result = result and b[i]
if result == 1:
    print("该域名存在，不报警")
else:
    print("该域名不存在未解析，异常报警")
# np.savetxt("result.txt", b)
b.tofile()

