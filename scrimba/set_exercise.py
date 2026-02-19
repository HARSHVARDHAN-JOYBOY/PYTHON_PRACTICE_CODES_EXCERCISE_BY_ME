#Sets - Exercise

#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']


print("\nCheck if Eric and John exist in friends : ")
print('Eric' in friends and 'John' in friends)

print("\ncombine or add the two sets  : ")
print(friends.union(my_friends))
# or
print(friends | my_friends)

print("\nFind names that are in both sets  : ")
print(friends.intersection(my_friends))
# or
print(friends & my_friends)

print("\nfind names that are only in friends  : ")
print(friends-friends.intersection(my_friends))
# or
print(friends.difference(my_friends))
# or
print(friends-my_friends)


print("\nShow only the names who only appear in one of the lists  : ")
print(friends.union(my_friends)-friends.intersection(my_friends))
#or
print(friends.symmetric_difference(my_friends))
#or
print(friends^my_friends)


print("\nCreate a new cars-list without duplicates  : ")
cars=list(set(cars))
print(cars)


