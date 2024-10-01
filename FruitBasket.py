import sys as s

def func(howmany):
    global basket
    basket=[]
    for i in range(1,howmany+1):
        x=str(input(f"Fruits {i} to {howmany}: "))
        if x == "a" or x == "A":
            basket.append("Apple")
        elif x == "o" or x == "O":
            basket.append("Orange")
        elif x == "m" or x == "M":
            basket.append("Mango")
        elif x == "g" or x == "G":
            basket.append("Guava")
        else:
            print("Invalid Fruit. Enter again.")
            func(howmany)

def eat1():
    print("Your basket now has:",basket)
    eat=str(input("Press E to eat a fruit. "))
    while eat == "e" or eat == "E":
        if len(basket)==1:
            print("Takaw mo naman! ")
            s.exit()
        basket.pop(-1)
        eat1()

print("Catch and eat any of these fruits: ('apple','orange','mango','guava')")
howmany=int(input("How many fruits would you like to catch? "))
print("Choose a fruit to catch. Press A, O, M, or G.")
func(howmany)
eat1()


