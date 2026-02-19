def greet(fx):
    def mfx(*args,**kwargs):
        print("Good mOrning")
        fx(*args,**kwargs)
        print("thnks for using this function !")
    return mfx

@greet
def hello():
    print("Hello World")
@greet
def add(a,b):
    print(a+b)
hello() 
#OR
#greet(hello())
add(1,3)
#OR greet(add)(1,2)  