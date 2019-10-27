import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a * np.exp(-b * x) + c

file = open('1.txt')
data=list()
temp=0
for line in file:
    if(temp==1):
        str=line.strip()
        if(str!=''):
            data.append(int(str))
            #data.append(str);
            #print(str)
        continue
    if(line.find('Data:')!=-1):
        print("find!")
        temp=1
        continue
file.close()
# for i in data:
#     print(i);
print(len(data))

#transy=np.fft.fft(data)
X=list(range(1,len(data)+1))
plt.plot(X[0:50],data[0:50])

popt, pcov = curve_fit(func, X[0:50], data[0:50])
# popt数组中，三个值分别是待求参数a,b,c
y2 = [func(i, popt[0], popt[1], popt[2]) for i in X[0:50]]
plt.plot(X[0:50], y2, 'r--')
print (popt)
plt.show()

