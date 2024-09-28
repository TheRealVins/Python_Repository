import random as r
roll=str(input("Would you like to roll the dice? (y/n) "))
while roll.lower()=="y":
    randomint=r.randint(1,6)
    print(randomint)
    roll=str(input("Would you like to roll the dice again? (y/n) "))
else:
    print("Thank you for rolling the dice.")