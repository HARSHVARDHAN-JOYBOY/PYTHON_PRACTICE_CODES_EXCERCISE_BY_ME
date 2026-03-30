# import os

# def arrangefiles(list_of_files,extentions):
#     filesjpg=[file for file in list_of_files if file.endswith(extentions)]
#     print(filesjpg)
#     if not (os.path.exists("Images")):
#         os.mkdir("Images")



#     for i,file in enumerate(filesjpg):
#         os.rename(file,f"Images/Photo_{i+1}{extentions}")

# if __name__=="__main__":
#     files=os.listdir()
     
#     arrangefiles(files,".jpg")
#make it ADVANCE by taking some inputs

import os

# def fileOrg(fileslist,extens):
#     filetxt=[file for file in fileslist if file.endswith(extens)]
#     print(filetxt)


# if __name__=="__main__":
#     files=os.listdir()
#     fileOrg(files,".txt")
def check_file_exists(file,extens):
    files=os.listdir()
    filesl=[file for file in files if file.find(extens)]
    f3=file+"."+extens

    if f3 in filesl:
        return True
    else:
        return False







def Create():
    try:
        fname=input("Enter a name for your Folder ")

        if (os.path.exists(fname)):
            print("Enter another name for folder cause it already exists !")
            Create()
            
        else:
            os.makedirs(fname)
            print("Folder Created !")
            # exit()
    except Exception as e:
        print(f"change the name of folder It already exists ! {e}")

def Createf():
    files=os.listdir()
    try:
        filename=input("Enter a name of file :")
        extens="."+input("Enter extension type :")
        filen=filename+extens

        filesextens=[file for file in files if file.find(extens)]
        if filen in filesextens:
            print("try another name it is already exists :")
            Createf()
        else:
            with open(filen,"w") as f:
                print("File created !")
            return
        
    except FileExistsError as e:
        print(f"File Exists ! {e}")
    except IOError:
        print("IO error")
    except PermissionError:
        print("permission error")
    except Exception:
        print("An unexpected error occured !")

def Readf():
    try:
        file1=input("Enter name of file to open : ")
        extens1=input("Enter Extenstion : ")
        f2=file1+"."+extens1
        files=os.listdir()
        filelist=[file for file in files if file.find(extens1)]

        if f2 not in filelist:
            print("Sorry this file does not exixts ! \n Create new one! ")  
            return
        else:
            with open(f2,"r") as f:
                print(f"Content of {f2} file is : \n{f.read()}")
            

    except FileNotFoundError:
        print("File not found ! ")


def Writef():
    try:
        f1=input("Enter a name of file you want to edit: ")
        exten1=input("Enter extenstion of that file : ")
        filen=f1+"."+exten1

        file_list=check_file_exists(f1,exten1)
        
        if file_list:
            print("Enter something to add into file : ")
            list1=[]
            while True:
                content=input()
                if content.strip().upper()=="END":
                    break
                list1.append(content)

            with open(filen,"a") as f:
                for l in list1:
                    f.write(l + "\n")
                print("Content writed ! ")
        else:
            print("File does not exists ! ")
            Writef()


    except FileNotFoundError:
        print("File not found ! ")

def Rename():
    try:
        f1=input("Enter a name of file you want to Rename: ")
        exten1=input("Enter extenstion of that file : ")
        filen=f1+"."+exten1
        newname=input("Enter a new name to rename the file : ")
        new2=newname +"."+ exten1
        
        os.rename(filen,new2)
        print(f"the file was renamed as {new2} !")

    except FileNotFoundError:
        print("File not found ! ")

def Deletef():
    try:
        f1=input("Enter a name of file you want to Delete: ")
        exten1=input("Enter extenstion of that file : ")
        filen=f1+"."+exten1
        
        if (os.path.exists(filen)):
            ch1=input("Enter \'Proceed\' to delete or anything to stop deletion process ! ")
            if ch1.upper()=="PROCEED":
                os.remove(filen)
                print(f"{filen} was removed !")
            else :
                print("Deletion Stoped ! ")
                return 0
        else:
            print("File not found !")
    except FileNotFoundError:
        print("File not found ! ")

while True:

    print("\n-----MENU_FILES_MANAGER-----")
    print("CLICK 0 for Creating Folders : ")
    print("CLICK 1 for Creating Files : ")
    print("CLICK 2 for Read Files : ")
    print("CLICK 3 for Write into Files : ")
    print("CLICK 4 for Rename Files : ")
    print("CLICK 5 for Delete Files : ")
    print("CLICK 6 for Exiting : ")
    ch=int(input("\n Enter Your Choice : "))

    match ch:
        case 0:
            Create()
        case 1:
            Createf()
        case 2:
            Readf()
        case 3:
            Writef()
        case 4:
            Rename()
        case 5:
            Deletef()
        case 6:
            print("Exiting Program !")
            exit()
        case default:
            print("wronge choice !")
