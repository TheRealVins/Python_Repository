import random as r

#https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/

roll=str(input("Would you like to roll the dice? (y/n) "))
while roll.lower()=="y":
    randomint=r.randint(1,6)
    print(randomint)
    roll=str(input("Would you like to roll the dice again? (y/n) "))
else:
    print("Thank you for rolling the dice.")