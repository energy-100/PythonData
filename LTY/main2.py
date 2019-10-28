from LTY import demo2
import numpy as np
from functools import reduce
z=3
size=10000000
rodata=[]
file = open("alexa_100k.txt")
for line in file:
    line = line.rstrip('\n')
    rodata.append(line)
rodata=rodata[0:1000]
print(rodata)
res=demo2.WESA(rodata,size,z)
#print(res)
data=[]
for i,temp in enumerate(res):
    for j in range(0,31):
        k=temp%2
        if (k==1):
            data.append(i*31+j+1)
        temp=temp>>1
print(data)
str='edewqsw22w3.com'
tempchar=[]
for a in str:
    tempchar.append(ord(a))
tempchar = np.array(tempchar, dtype=int)
# print(temp)
#res=reduce(lambda x, y: x*z+y,temp)%size
result = reduce(lambda x, y: x * z + y, tempchar) % size
print(result)
if(result in data):
    print("存在！")
else:
     print("不存在！")



