# this is use to write into the file but it replaces whole previous data with new simply it overwrites the data

# f=open("io.txt","w")
# string='''
# hey my name is harshvardhan and i gone be .......
# the king of the billionaires
# '''
# f.write(string)
# f.close()

# this one is use to append something in file without replacing the whole content

f=open("io.txt","a")
string='''
i will be the first billionaire of our bloodline 
'''
f.write(string)
f.close()

# this one is use to read and print the data without  
f=open("io.txt","r")
data=f.read()
print(data)
f.close()
