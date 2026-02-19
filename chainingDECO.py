def star(func):
    def wrapper(*args, **kwargs):
        print("⭐" * 10)
        func(*args, **kwargs)
        print("⭐" * 10)
    return wrapper

def shout(func):
    def wrapper(*args, **kwargs):
        print("🔥", end=" ")
        func(*args, **kwargs)
        print(" 🔥")
    return wrapper

@star
@shout
def hello(name):
    print(f"Hello {name}")

hello("Harsh")
