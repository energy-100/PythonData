import os
path = 'G:/第一时点6事件avg'
for file in os.listdir(path):
    print(file)
    if os.path.isfile(os.path.join(path,file))==True:
        Newname= file.replace(' Averaged-', '-')
        # Newname= file.replace('T1','T2')
        os.rename(os.path.join(path,file),os.path.join(path,Newname))