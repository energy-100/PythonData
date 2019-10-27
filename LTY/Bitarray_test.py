from bitarray import bitarray
b=bitarray(772231138)
b.setall(0)
f=open("a.txt","w+b")
b.tofile(f)