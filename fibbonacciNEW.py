class fibo:
    def __init__(self,n):
        self.n=n

    def fibonacci(self):
        first,sec=0,1
        seris=[]
        for _ in range(self.n):
            seris.append(first)
            first,sec=sec,first+sec
        return seris
    
fib=fibo(5)
print(fib.fibonacci())