def demo(a, b=10, *args, c=20, **kwargs):
    print(f"a={a}, b={b}, args={args}, c={c}, kwargs={kwargs}")

demo(1)  
# a=1, b=10, args=(), c=20, kwargs={}

demo(1, 2, 3, 4, c=30, d=40, e=50)
# a=1, b=2, args=(3, 4), c=30, kwargs={'d': 40, 'e': 50}
