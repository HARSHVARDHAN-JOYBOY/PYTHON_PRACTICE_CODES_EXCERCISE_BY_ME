def upper(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs).upper()
    return wrapper

def exclaim(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)+" !!!"
    return wrapper

def flags(func):
    def wrapper(*args,**kwargs):
        return "🚩🚩🚩"+func(*args,**kwargs)
    return wrapper


@upper
@exclaim
@flags
def greet():
    return "jay shri ram"


print(greet())