import random as r
x=int(input("enter a number: "))
randomint=r.randint(1,100)
if x < randomint:
    print("Too low")
elif x > randomint:
    print("Too high")
else:
    print('yes')
while x!=randomint:
    x=int(input("enter a number: "))
    if x < randomint:
        print("Too low")
    elif x > randomint:
        print("Too high")
    else:
        print('yes')

