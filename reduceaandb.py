from functools import reduce
num=[1,4,8,3,8,9,5,7,75,89,36]
def sum1(a,b):
    return a+b

print(sum(num))
c=reduce(sum1,num)
print(c)