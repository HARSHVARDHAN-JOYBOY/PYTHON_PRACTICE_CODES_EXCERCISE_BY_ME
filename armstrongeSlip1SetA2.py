s=0
rem=1
n=int(input("enter a number to cheak it is armstrong or not"))
temp=n
while n>0:
    rem=n%10
    s+=rem **3
    n=n//10

if temp==s:
    print(s,"Is Armstronge Number")

else:
    print(s,"Is Not Armstronge")
    
