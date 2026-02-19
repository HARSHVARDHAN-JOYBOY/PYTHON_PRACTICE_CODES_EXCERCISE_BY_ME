class logger:
    def __init__(self,func):
         self.func=func

    def __call__(self, *args, **kwargs):
         print(f"[LOG] calling {self.func.__name__}")
         return self.func(*args,**kwargs)
    

@logger
def sayhi(name):
     print(f"Hi {name}")


sayhi("Harsh")