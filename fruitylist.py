fruits=[]
n=int(input("enter the number of fruits you want to enter !:"))

while(n!=0):
    fru=input("enter name of fruit ! :")
    fruits.append(fru)
    n-=1
    print(fruits)