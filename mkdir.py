import os

ndir=r"D:\pythonprojectsand all\OSMOD\abcdef"
try:
    os.mkdir(ndir)
except FileExistsError as e:
    print(f"This {ndir}",e)
 
nesteddir= r"D:\pythonprojectsand all\OSMOD\grandpa\papa\baby"
try:
    os.makedirs(nesteddir,exist_ok=True)
    print(f"Successfully created {nesteddir}")
except Exception as e:
    print("Some error occured",e)

dir1=r"D:\pythonprojectsand all\OSMOD\abcdefgh"

if not os.path.exists(dir1):
    os.mkdir(dir1)
    print(f"Created after check ",dir1)
else:
    print("File already exists")
 

