from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
import pymysql

def func(x, a, b, c):
    return a * np.exp(-b * x) + c

xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
ydata = y + 0.2 * np.random.normal(size=len(xdata))
plt.plot(xdata, ydata, 'b-')
popt, pcov = curve_fit(func, xdata, ydata)
# popt数组中，三个值分别是待求参数a,b,c
y2 = [func(i, popt[0], popt[1], popt[2]) for i in xdata]
plt.plot(xdata, y2, 'r--')
print (popt)
plt.savefig('test.png')
plt.show()