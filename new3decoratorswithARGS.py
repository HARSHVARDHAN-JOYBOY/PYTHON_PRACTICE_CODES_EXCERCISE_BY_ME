def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(3)
def square(a):
    b=a*a
    print(f"Square of {a} is {b} ! ")

square(5)
