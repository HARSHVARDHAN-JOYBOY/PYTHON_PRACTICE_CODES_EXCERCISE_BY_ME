import threading
import time

def sq(num):
    #    return  num**2
    for n in num:
        print(f"Square of {n} : {n**2}")
        time.sleep(1)
def cube(num):
    # return num**3
    for n in num:
        print(f"Cube of {n} : {n**3}")
        time.sleep(1)

num=list(map(int,input("enter numbers : ").split()))

t1=threading.Thread(target=sq, args=(num,))
t2=threading.Thread(target=cube, args=(num,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Both Threads finished !")