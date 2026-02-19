import os 

directory="osmoduledemo2"
parentdir="D:/pythonprojectsand all/OSMOD"
path=os.path.join(parentdir,directory)
os.makedirs(path)
print("Directory %s' created" % directory)



