import os
try:
    f1="xyz.txt"
    file= open(f1,'w')
    file.write("JaysIyaRaM")
    file.close()
    f=open(f1,'r')
    text=f.read()
    print(f)
    f.close()
except IOError:
    print('problem reading'+ file)    

