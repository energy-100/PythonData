import matplotlib.pyplot as plt
import numpy as np
def pest(list0,list1,list2,list3,list4):
    x=range(len(list0))
    list0=np.array(list0)
    list1=np.array(list1)
    list2=np.array(list2)
    list3=np.array(list3)
    list4=np.array(list4)
    l0=[]
    l1=[]
    l2=[]
    l3=[]
    l4=[]
    for i in range(len(list0)):
        l0.append(float(list0[i] - np.min(list0)) / (np.max(list0) - np.min(list0)))
        l1.append(float(list1[i] - np.min(list1)) / (np.max(list1) - np.min(list1)))
        l2.append(float(list2[i] - np.min(list2)) / (np.max(list2) - np.min(list2)))
        l3.append(float(list3[i] - np.min(list3)) / (np.max(list3) - np.min(list3)))
        l4.append(float(list4[i] - np.min(list4)) / (np.max(list4) - np.min(list4)))

    plt.plot(x,l0,label='s1')
    #plt.plot(x,l1,label='s2')
    plt.plot(x,l2,label='s3')
    plt.plot(x,l3,label='s4')
    plt.plot(x,l4,label='s5')
    plt.show()


def s3s4(list1,list2):
    plt.plot(list1,list2);
    plt.show()



#pest([1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9])