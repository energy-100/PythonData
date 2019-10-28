import matplotlib
import matplotlib.cm as cmx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# x = np.random.rand(30)
# y = np.random.rand(30)
# z = np.random.rand(30)
# cs = np.random.rand(30)

x = []
y = []
z = []
cs = []
cs2=[]

f = open("C:/Users/ENERGY/Desktop/finall/AcqBiophoton_NoA/AcqBiophoton/result.txt")
alllines = f.readlines()
for eachLine in alllines:
    eachLines = eachLine.split()
    x.append(float(eachLines[0]))
    y.append(float(eachLines[2]))
    z.append(float(eachLines[3]))
    cs.append(float(eachLines[6]))
for i in range(len(cs)):
    cs2.append((cs[i]-min(cs))/(max(cs)-min(cs)))
print(cs2)

def scatter3d(x,y,z, cs, colorsMap='jet'):
    cm = plt.get_cmap(colorsMap)
    cNorm = cmx.colors.Normalize(vmin=min(cs), vmax=max(cs))
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)
    fig = plt.figure()
    ax = Axes3D(fig)
    #ax.plot_surface(x, y, z, rstride=1, cstride=1, color=cs)
    ax.scatter(x, y, z, c=scalarMap.to_rgba(cs))
    scalarMap.set_array(cs)
    fig.colorbar(scalarMap)
    plt.show()

scatter3d(x,y,z,cs2)