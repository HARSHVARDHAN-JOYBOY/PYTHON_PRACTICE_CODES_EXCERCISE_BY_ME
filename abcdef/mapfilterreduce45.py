from functools import reduce

num=list(map(int,input("Enter list of random numbers !").split()))  #this accepts all numbers as integer list using map

odds=list(filter(lambda x:x%2!=0,num)) #this seperates odd elements using filter and lambda function

cubes=list(map(lambda x:x**3,odds)) #this makes cube of seperated odd elements using map function with lambda

sums=reduce(lambda x,y:x+y,cubes) # this uses reduce to sum the elements with lambda func

print(f"All Numbers are : {num}")
print(f"Odd Numbers are : {odds}")
print(f"Cubes of Odd Numbers are : {cubes}")
print(f"Sum of all cubes  : {sums}")




