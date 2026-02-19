x=4
print(x)
def func():
    global x

    x=5
    y=6

func()
print(x)
#print(y)