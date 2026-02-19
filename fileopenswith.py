# or you can also do this
f=open("io.txt",'r')

with open("io.txt","r") as s:
    content= f.read()
    print(content) 
    # here f.close() is already done by default even if error occurs it closes file on its own