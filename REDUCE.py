from functools import reduce
num= [34,45,54,545,5,76,8,68,56,455,5]

def mysum(x,y):
    return x+y

sum= reduce(mysum,num)
print(sum)
# simply reduce function ek function  as parameter leta hai or sari data jo list me ya kisi DS me hai usko given function data by data one by one applay kari hai







