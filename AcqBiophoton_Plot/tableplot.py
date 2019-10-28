from matplotlib import pyplot as plt
import numpy as np
randn = np.random.randn
from pandas import *
idx = Index(np.arange(1,7))
df = DataFrame(randn(6, 4), index=idx, columns=['A', 'B', 'C', 'D'])
vals = np.around(df.values,2)
fig = plt.figure(figsize=(9,4))
ax = fig.add_subplot(111, frameon=True, xticks=[], yticks=[])
the_table=plt.table(cellText=vals, rowLabels=df.index, colLabels=df.columns,
colWidths = [0.1]*vals.shape[1], loc='center',cellLoc='center')
the_table.set_fontsize(20)

the_table.scale(2.5,2.58)
plt.show()
