def rep(n):
    def deco(func):
        def wrapper(*args,**kwargs):
            for _ in range(n):
                func(*args,**kwargs)
        return wrapper
    return deco


@rep(1)
def sayhi(name):
    print(f"Jay Shri Ram {name} bhau !!! ")\
    

# sayhi("Harsh")

names=input("Enter names : ").split()
for n in names:
    sayhi(n)
