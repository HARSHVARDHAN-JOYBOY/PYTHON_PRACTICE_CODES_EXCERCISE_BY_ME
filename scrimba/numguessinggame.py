# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)
# Three Loop Questions:
#1. What do I want to repeat?
#  -> guesses
#2. What do I want to change each time?
#  -> guessed by number by user and number of guesses
#3. How long should we repeat?
#  ->  util user losses,wins or left with no guesses
import random
def numgame():
    a=random.randint(0,9999999999)
    i=0
    print("You have 3 guesses ! ")
    while i<3:
        ch=int(input(f"enter guess no {i+1} : "))
        print(f"You are left with {3-i-1} guesses ! ")
        i=i+1
        if(ch==a):
            print(f"*:* Congrats *:* :) ,you found correct ! {a} is the number !")
            return
        else :
            print("Na ah good luck next time !  ")
            if a>ch:
                print(" go little bit highhhh :) ")
            else :
                print(" go little bit lowwww :) ")
            continue
    print(f"You are left with no guesses ! SORRY YOU LOST :( guess was \"{a}\" !")
    return

print("Number guessing game ! :")
numgame()







  