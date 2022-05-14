import random

number = random.randint(1,9)

chances=0

print("Guess a number between 1 and 9 :-")

while chances < 5:
    guess=int(input("enter your guess :-"))
    if guess == number :
        print("CONGRATULATIONS!!! YOU WON!!") 
        break
    if not chances < 5:
        print("YOU LOSE !!! THE NUMBER IS :",number)
        
