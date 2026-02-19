import threading
import time


a=list(map(int,input("Enter a list by numbers ").split()))
def worker(n,num):
    print(f"Thread {n} is Starting ! \n")
    print(f"Square of this number is {num*num} \n")
    time.sleep(2)
    print(f"thread {n} is Finishing ! \n")

threads=[]
for idx,num in enumerate(a): 
        thread = threading.Thread(target=worker, args=(idx,num))
        threads.append(thread)
        thread.start()

for thread in threads:
    thread.join()  # it will wait until all threads for finishing

print(" \n All Threads Completed !!!")

