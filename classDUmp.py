def applay(func,value):
    return func(value)


def sq(x):return x*x
def cube(x):return x*x*x


print(applay(sq,4))
print(applay(cube,5))