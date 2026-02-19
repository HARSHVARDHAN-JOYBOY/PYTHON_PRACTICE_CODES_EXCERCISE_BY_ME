import os

usr_fol= input("Enter a name of a folder to create")

user_path=os.path.join(r"D:\pythonprojectsand all\OSMOD\habsspace",usr_fol)

try:
    os.mkdir(user_path)
    print("User folder created on request ")
except FileExistsError:
    print("This file already exists ")
  
