import os
with open('filedemo.txt','r')as f:
    print(type(f))

    f.seek(10)
    data=f.read(5)
    print(f.tell())
    print(data)

with open('filedemo2.txt','w')as n:
    n.write('JayShreeRAM')   
    n.truncate(3)

with open('filedemo2.txt','r') as r:
    print(r.read())













