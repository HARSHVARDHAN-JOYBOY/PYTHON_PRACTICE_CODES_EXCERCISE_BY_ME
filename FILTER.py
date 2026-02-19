#Filter function
l= [2,12,4,1,42,5,0,8,1,2]
def filter_function(a):
    return a>4

newFil = list(filter(filter_function, l))
print(newFil)
# basically it filters the given list with given function

#with lambda function
newFil2= list(filter(lambda x: x>10,l))
print(newFil2)



newfil3= list(filter(lambda x: x%2 , l))  #it will return the number which returns someting in x%2
print(newfil3)                            #and excludes numbers which returns 0 in x%2
