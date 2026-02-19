import os
from functools import reduce

def filterfunc(a):
    if a%2==0:
        return a
try:
    with open("Func.txt",'w') as f:
        txt=list(map(int,input("Enter Random numbers in file : ").split()))
        f.write(" ".join(map(str,txt)))

    with open("sq.txt",'w') as s:
        txt2=list(map(lambda x: x**2,txt))
        s.write(" ".join(map(str,txt2)))
    with open("Evennums.txt",'w') as ev:
        txt3=list(filter(filterfunc,txt))
        ev.write(" ".join(map(str,txt3)))
    with open("Reduced.txt",'w') as r:    #reduce function reduces the list to single value
        txt4= reduce(lambda x,y:x+y,txt)
        r.write(str(txt4))



except Exception as e:
    print("An Error ocuured ❌❌❌",e)
