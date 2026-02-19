import threading
import time

def tables(num):
    for n in num:
        for i in range(11):
            print(f"{n} * {i} : {n*i} \n")
    time.sleep(2)

def evenodd(num):
    evens=[]
    odds=[]
    for n in num:
        if n%2==0:
            evens.append(n)
        else:
            odds.append(n)
    time.sleep(2)
    print(f"\n\n Evens Are : {evens} \n")
    print(f"Odds Are : {odds} \n")

num=list(map(int,input("Enter the list of random numbers : ").split()))

t1=threading.Thread(target=tables,args=(num,))
t2=threading.Thread(target=evenodd,args=(num,))

t1.start()
t2.start()

t1.join()
t2.join()

print("All Threads Executed Successfully !!! ")


