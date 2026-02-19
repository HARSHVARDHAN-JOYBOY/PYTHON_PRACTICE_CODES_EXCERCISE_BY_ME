unique = set()

print("Enter eight numbers !! ")
for i in range(8):
    num = int(input(f"Enter No {i+1} in dictionary : "))
    unique.add(num)

#unique.set(num)

print(f"Unique numbersa are")
for num in unique:
    print(num)