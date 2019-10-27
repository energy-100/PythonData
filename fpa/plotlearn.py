import numpy as np

import os

import matplotlib.pyplot as plt

datafile= np.genfromtxt('GP_UC1a_0.csv', delimiter=',')

y=datafile[:,0]

yerr=datafile[:,1]

datafile= np.delete(np.genfromtxt('VEE_UC1a.csv', delimiter=','), 0, 0)

Yte=datafile[220:datafile.shape[0],5]

x=np.arange(54)

plt.figure()

plt.xlim([0,54])

plt.ylim([0.4,0.6])

plt.errorbar(x, y, yerr, fmt='o')

plt.errorbar(x, Yte, fmt='x', color='r')

plt.title("UC1a, output1")

plt.fill_between(x, y-yerr, y+yerr, edgecolor='#3F7F4C', facecolor='#7EFF99')

plt.show()