import random as r

def guessthenumber(x,randomint):
    if x < randomint:
        return("Too low")
    elif x > randomint:
        return("Too high")  

x=int(input("enter a number: "))
randomint=r.randint(1,10)
while x!=randomint:
    print(guessthenumber(x,randomint))
    x=int(input("enter a number: "))
else:
    print("You have guessed the number!")


    

