import os

if(not os.path.exists("tempfile")):
    os.mkdir("tempfile")
file="temp.txt"
dir="Temppro"

parent="D:/pythonprojectsand all/OSMOD"
path0=os.path.join(parent,dir)
path=os.path.join(path0,file)

if(not os.path.exists("Temppro")):
    os.mkdir("Temppro")

os.chdir("Temppro")

fp=open(file,'w')
fp.write("Jay SiyaRam")
fp.close()
fp=open(file,'r')
text=fp.read()
print(text)
fp.close()

os.remove(path)
os.chdir(parent)
os.rmdir("Temppro")

