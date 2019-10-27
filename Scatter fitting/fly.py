import numpy as np
from matplotlib import pyplot as plt
x=[0.1*n for n in range(1000)] ###用generator生成一个【0，100】之间每个数字差0.1的数列
#print x
y=np.cos(x)  ###引入cos函数，这个函数在numpy里头
transy=np.fft.fft(y)
plt.subplot(121),plt.plot(y),plt.title("Original")
plt.subplot(122),plt.plot(transy),plt.title("FFT")
plt.show();
###注意此处绘图不可以用imshow命令只能用plot命令，二维用imshow一维用plot