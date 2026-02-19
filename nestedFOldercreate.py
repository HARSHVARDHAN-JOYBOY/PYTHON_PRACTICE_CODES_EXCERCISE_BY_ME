import os

while True:
    path="D:\pythonprojectsand all\OSMOD\habsspace"
    ch=input("\n \n Enter 'yes' for creating a folders: \n Enter 'li' to get list of folders in directory: \n Enter 'open' to enter into a workspace or change Directory :  \n Enter 'del' to delete a folder or directory : \n Enter 'rename' to Rename the folder : \n Enter 'cur' to see current Directory : \n Enter 'abp' to get Absolute path of file :   \n Enter anything to exit :  \n \n Enter your choice :  ")
    if(ch.lower())=="yes":
        ch2=input("Enter 1 if you want to create a normal folder or Enter 2 for creating nested folder strcture !: ")
        if(ch2.lower()=="1"):
            userfolder= input("Enter a name of folder ! : ")
            uf1=os.path.join(path,userfolder)
            try:
                os.mkdir(uf1)
                ch3=input("Your folder is created successfully enter open to enter in that folder: ")
                if(ch3.lower()=="open"):
                    os.chdir(uf1)
                    print("Current directory is : ",uf1)
                    chh1=input("Enter exit to exit : ")
                    if chh1=="exit":
                        print("We are shifting back to our parent directory : ")
                        os.chdir(path)
                        print("We are exiting now ! ")
                        exit()
                    else:
                        print("We are shifting back to our parent directory : ")
                        os.chdir(path)
                else:
                    print("ok :")
            except FileExistsError as e:
                print("An error occured : ",e)


        elif(ch2.lower()=="2"):
            try:
                userf= input("Enter a parent folder name : ")
                current_path=os.path.join(path,userf)
                os.makedirs(current_path,exist_ok=True)
                print("Created : ",current_path)
                while True:
                    ch4=input("Enter yes if you want to add child folder in it : ").strip().lower()
                    if(ch4=="yes"):
                        folderch=input("Enter a name : ")
                        current_path=os.path.join(current_path,folderch)
                        os.makedirs(current_path,exist_ok=True)
                        print("Created : ",current_path)
                    else:
                        print(" ok exiting the program !")
                        print(os.getcwd())
                        exit()     
            except FileExistsError as e:
                print("An error occured : ",e)
                
        else:
            print("Bhai fir yes kyu dala ? :( i am exiting ")
            exit()

    elif(ch.lower()=="li"):
        directory=input("Enter your diectory path carefully : ")
        items=os.listdir(directory)
        print("Contents of Directory : ")
        for item in items:
            print(item)

    elif(ch.lower()=="open"):
        directory=input("Enter a path to open that perticular workspace please enter carefully : ")
        os.chdir(directory)
        print("Shifting to another directory :",os.getcwd())

    elif(ch.lower()=="del"):
        try:

            while True:
                path3=input("Enter path of folder to delete the path entered will be deleted so please enter accurate path : ")
                chhh=input("Enter yes to confirm : ")
                if chhh.lower()=="yes":
                    os.rmdir(path3)
                    print("Folder deleted Successfully : ")
                    print("Current Directory : ",os.getcwd())
                    break
                else:
                    print("Ok you can re enter the path enter 'yes' to Reenter or enter 'no' to back : ")
                    chhh1=input(" : ")
                    if chhh1.lower()=="yes":
                        print("Ok : ")
                        continue
                    else:
                        print("ok Exiting: ")
                        break
        except FileExistsError as e:
            print("File not found : ",e)
            print("Exiting the program : ")
            exit()

    elif ch.lower()=="rename":
        old=input("Enter the old path : ")
        new=input("Enter the new name of folder in path : ")

        try:
            os.rename(old,new)
            print("Folder renamed succesfully ! : ")
            os.chdir(new)
            print("Current workspace : ",os.getcwd())
        except FileNotFoundError:
            print("Old Folder not found : ")

    elif ch.lower()=="cur":
        print("Current directory : ",os.getcwd())

    elif ch.lower()=="abp":
        file1=input("Enter Name of file along with extention : ")
        try:
            abppath=os.path.abspath(file1)
            print("Absolute path is : ",abppath)
        except FileExistsError as e:
            print("An error occured : ", e)

    else:
        print("Ok fine i am Exiting  !")
        print("\n Program is Exited") 
        exit()   






