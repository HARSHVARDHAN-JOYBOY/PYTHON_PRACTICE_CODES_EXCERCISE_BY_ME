import os
try:    
    file=open("new1200.txt",'x')
    with open("new1200.txt",'w') as f:
        f.write("Jay Shri Ram")
    with open("new1200.txt",'rt') as rt:
        txt=rt.read()
        print(txt)    
    with open("new1200.txt",'a') as a:
        a.write(" or Jay Mahakal")    
    with open("new1200.txt",'rb') as rb:
        txt=rb.read()
        print(txt)    
    file.close()
    
except IOError:
    print("IO error occured" + file)

os.remove("new1200.txt")    
