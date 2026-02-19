import os
file=open("tempee.txt",'r')
i=1
while True:
    
    line= file.readline()
    if not line:
        break
    if line =="":
        continue
    m1=int(line.split(",")[0])
    m2=int(line.split(",")[1])
    m3=int(line.split(",")[2])

    avg=m1+m2+m3/300
    print(f"Average of student {i} is {avg}")
    print(f" Marks of student {i} in Math is {m1}")
    print(f" Marks of student {i} in OS is {m2}")
    print(f" Marks of student {i} in PYTHON is {m3}")
    if not line:
        break
    print(line)
    
