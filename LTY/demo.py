import numpy as np
def do(sign):
    a = np.zeros(52)
    for i in sign:
        a[i]=1;
        #print(a[i])
    #print(a)
    return a
