class fibo:
    def __init__(self,n):
        self.n=n
    def fib(self,k):
        if k<=1:
            return k
        else :
            return self.fib(k-1)+self.fib(k-2)

    def fibona(self):
        for i in range(self.n):
            print(self.fib(i),end=" ")


f=fibo(10)
f.fibona(                   )