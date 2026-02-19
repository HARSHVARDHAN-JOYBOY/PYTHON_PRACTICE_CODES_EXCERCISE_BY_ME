# ☕ Coffee Order Queue Challenge
# 1. Set up two variables: one for total price, one for drink count
# 2. Start a while True loop
# 3. Ask for the customer's name
# 4. If the name is "done", break the loop
# 5. Ask for their drink order
# 6. If it's "latte", add 3.50 to total and +1 to drink count
#    If it's "americano", add 3.00 to total and +1 to drink count
#    If it's "espresso", add 2.50 to total and +1 to drink count
# 7. If it's not one of those drinks, print a warning and continue
# 8. After the loop, print total number of drinks and total price 

def coffee_order():
    total,drink_count=0,0
    d=[]
    drinks={"latte":350,"americano":300,"espresso":250}
    while True:
        name=input("Enter customers name : ")
        if name.lower()=="done":
            break
        drink=input("Enter drink name : ")
        if drink in drinks:
            drink_count+=1
            total+=drinks[drink]
            d.append(drink)
        else :
            print("this drink is not available ! ")
            continue
    print(f"Total number of drinks : {drink_count} \n Drinks as listed :{d} \nTotal bill to pay :{total} ")        

coffee_order()
