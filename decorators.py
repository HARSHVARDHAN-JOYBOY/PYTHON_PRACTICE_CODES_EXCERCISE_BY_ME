# def decorator(func):
#     def wrapper():
#         print("I am About to execute the function !")
#         func()
#         print("the function is executed ! ")
#     return wrapper
# @decorator
# def say_hello():
#     print("Hello World !!! ")

# # say_hello()
# f= decorator(say_hello)
# f()
def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(7)
def hello(a):
    print(f"HELOO   {a}")

hello("Ram")    


