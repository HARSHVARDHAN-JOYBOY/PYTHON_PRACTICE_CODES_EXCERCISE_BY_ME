def cube(x):
    return x*x*x
#traditional method
print(cube(2))
l= [ 12, 3, 65, 6, 24, 74, 53, 21]
new =[]
for item in l:
    new.append(cube(item))
for item in new:
    print(item)

# map method
newl=list(map(cube, l))
print(newl)

#with lambda function 
new2 =list(map(lambda x: x*x, l))
print(new2)









