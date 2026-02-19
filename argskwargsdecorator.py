def deco(func):
    def wrapper():
        print("Before Function execution !!! ")
        func()
        print("After Function Execution !!! ")
    return wrapper
@deco
def greetings():
    print("I am A Function !!! ")

greetings()