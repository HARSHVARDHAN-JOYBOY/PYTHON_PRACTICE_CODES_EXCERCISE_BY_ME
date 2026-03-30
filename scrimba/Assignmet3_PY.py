# Create a Python program that showcases file handling techniques and robust exception handling to effectively manage errors and manipulate files.
# Develop a Python 
# Daily Notes Management System program  for a that demonstrates file handling and exception handling techniques.
# A user wants to maintain a personal notes file named daily_notes.txt. The program should allow the user to create, write, append, and analyze the contents of this file.
# named daily_notes.txt if it does not already exist.
# (multiple lines of notes) into the file.
# to the same file without deleting existing data.
# the complete contents of the file.

# Count and display:
# Total number of lines
# Total number of words
# Total number of characters
# Implement proper to handle:
# FileNotFoundError
# PermissionError
# IOError
# ValueError
# Any other unexpected exception
# Ensure that the file is properly closed using:
# The with statement (preferred), or
# The finally block
# The program should:
# Be menu-driven and user-friendly
# Display meaningful error messages
# Write up Questions:
# 1. Explain how the given Python program demonstrates file handling operations.
# 2. Describe how exception handling is implemented in the Daily Notes Management System program.
# ref : link :https://www.w3schools.com/python/python_file_write.asp


import os

FILE="new101file.txt"

def create():
    try:
        with open(FILE,'x') as f:
            print("File created !")
        return 
    except FileExistsError:
        print("File exists !")
    except PermissionError:
        print("Permission Error !")
    except ValueError:
        print("Value Error !")
    except IOError:
        print("I/O Error !")
    except Exception as e:
        print("Unexpected Error Occured !",e)

def Editfile():
    try : 
        print("Enter content you want to write in file(write END in next line to stop wrinting) : ")
        lines=[]
        while True:
            content=input()
            if content.strip().upper() =="END":
                break
            lines.append(content)   

        with open("new101file.txt","a") as f:
            for l in lines:
                f.write(l+"\n")
            print("Data Writed Successfully ")
    
    except ValueError:
        print("Value Error Wrong data entered ")


def overwrite():
    try:
        
        print("Waring the privious written content will be erased and new content will overwrited on it !!! ")
        msg=input("enter NO to exit / Rollback ")
        if msg.upper()=="NO":
            print("Overwriting Rollbacked !")
            return
        
        print("Enter content you want to write in file(write END in next line to stop wrinting) : ")
        lines=[]
        while True:
            content=input()
            if content.strip().upper()=="END":
                break
            lines.append(content)
        with open(FILE,"w") as f:
            for l in lines:
                f.write(l+"\n")
            print("Content writed succesfully !")

    except ValueError:
        print("Value Error !")



    pass
def Readfile():
    try:  
        print(f"Reading the File {FILE}")
        with open(FILE,"r") as f:
            i=1
            lines=f.readlines()
            for l in lines:
                print(f"{i} - "+l)
                i+=1
    except FileNotFoundError:
        print("File not found !")

def Deletef():
    try:
        msg=input("enter NO to exit / Rollback ")
        if msg.upper()=="NO":
            print("Delete process Rollbacked !")
            return
        if os.path.exists(FILE):
            os.remove(FILE)
            print("FILE DELETED !")
    except FileNotFoundError:
        print("File Not found !")

def Nolines():
    try :
        lines=[]
        with open(FILE,"r") as f:
            str=f.read().split("\n")
            for l in str:
                lines.append(l)

        # print(type(lines))
        print(f"Total Number of Lines current in \n {FILE} : \"{len(lines)-1}\"")


    except FileNotFoundError:
        print("File not Found ! ")

def Nowords():
    try :
        lines=[]
        with open(FILE,"r")as f:
            str1=f.read().split()
            for l in str1:
                lines.append(l)
        print(f"Number of Words in File \n \"{FILE}\": {len(lines)} ")
    except FileNotFoundError:
        print("File Not Found ! ")



def Nochars():
    try:
        lines=[]
        with open(FILE,"r")as f:
            str2=f.read().replace(" ","").replace("\n","")
            str2=str2.strip()
            for l in str2:
                lines.append(l)
        print(lines)
        print(f"Number of Words in \n {FILE} : {len(lines)} ")


    except FileNotFoundError:
        print("File Not Found ! ")
while True:


    print("\n\n\n\n------Welcome to Daily Notes Management System program------")
    print("Press 1 : for creating File' ")
    print("Press 2 : Editing file without overwriting the content' ")
    print("Press 3 : Editing file overwriting the content' ")
    print("Press 4 : Read file' ")
    print("Press 5 : Delete file' ")
    print("Press 6 : Number of Lines' ")
    print("Press 7 : Number of Words' ")
    print("Press 8 : Number of characters' ")
    print("Press 9 : Exit' ")

    try :
        ch=int(input("Enter your choice : "))
    except ValueError:
        print("Value Error Wrong Input ! ")


    match ch:
        case 1:
            create()
        case 2:
            Editfile()
        case 3:
            overwrite()
        case 4:
            Readfile()
        case 5:
            Deletef()
        case 6:
            Nolines()
        case 7:
            Nowords()
        case 8:
            Nochars()
        case 9:
            print("exiting File program !")
            exit()
        case _:
            print("Invalid Choice !!!")

