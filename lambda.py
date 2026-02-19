double= lambda x: x*x
sum = lambda x,y,z: x+y+z
avg = lambda x,y,z: (x+y+z)/3
cube = lambda x: x*x*x
def passfuntofun(func, val):
    return val*func(val)


print(double(5))
print(sum(2,5,6))
print(avg(23,54,65))
print(cube(7))
#passing function to function
print(passfuntofun(cube,2))
print(passfuntofun(double,2))

print(passfuntofun(lambda x: x*x*x*x*x,2 ))


