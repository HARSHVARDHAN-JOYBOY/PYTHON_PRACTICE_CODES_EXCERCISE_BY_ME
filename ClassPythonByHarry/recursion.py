'''
recursion in python 
fibonacci series =
0 1 1 2 3 5 8 13 ....and so on 
'''
def fibo(n):
    if (n==0 or n==1):
        return n
    return fibo(n-2)+ fibo(n-1)

print(fibo(6))


'''
fibo(6)
fibo(4)+fibo(5)
fibo(2)+fibo(3)+fibo(3)+fibo(4)
fibo(0)+fibo(1)+fibo(1)+fibo(2)+fibo(1)+fibo(2)+fibo(2)+fibo(3)
0+1+1+fibo(0)+fibo(1)+1+fibo(0)+fibo(1)+fibo(0)+fibo(1)+fibo(1)+fibo(2)
0+1+1+0+1+1+0+1+0+1+1+fibo(0)+fibo(1)
0+1+1+0+1+1+0+1+0+1+1+0+1

:8 will be the final answer :)
'''