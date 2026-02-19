def deco(func):
    def wrapper():
        print("Beforer printing or executing any function ! ")
        func()
        print("After executing the function ! ")
    return wrapper

@deco
def yoo():
    print("me hoo ek function ! ")


# f=deco(yoo)
# f()
yoo()