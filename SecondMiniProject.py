import random as r

def guessthenumber(x,randomint):
    if x < randomint:
        return("Too low!")
    elif x > randomint:
        return("Too high!")  

x=int(input("Enter a number: "))
randomint=r.randint(1,100)
while x!=randomint:
    print(guessthenumber(x,randomint))
    x=int(input("Wrong! Guess again: "))
else:
    print("You have guessed the number! Congratulations!")


    

