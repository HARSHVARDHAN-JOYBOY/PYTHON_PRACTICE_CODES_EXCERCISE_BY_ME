hindi_dict={}

print("Enter a hindi word with its meaning in english !")
while True:
    hindi=input("Enter a hindi word and if you want to stop then enter 'stop' !").strip()
    if hindi.lower()=="stop":
        break
    english=input(f"Enter a meaning of {hindi}: ").strip()
    hindi_dict[hindi]=english
    print(f" Added Succesfully {hindi} : {english}")

print("Dictionary is created successfully so you can now see the meaning of words !")
while True:
    look=input("Enter a hindi word if you want to know the meaning if not so you can enter exit to exit ! :").lower()
    if look=="exit":
        print(" Good Bye :) ... ")
        break
    elif look in hindi_dict:
        print(f"Meaning of Hindi Word is {hindi_dict[look]} ")
    else:
        print("No Record of this word !!! ")

