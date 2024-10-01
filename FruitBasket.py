print("Catch and eat any of these fruits: ('apple','orange,'mango','guava')")
howmany=int(input("How many fruits would you like to catch? "))

def fruits(howmany):
    basket=[]
    choosefruit=str(input("Choose a fruit to catch. Press A, O, M, or G. :"))
    if choosefruit.upper == "A":
        basket.append("Apple")
    elif choosefruit.upper == "O":
        basket.append("Orange")
    elif choosefruit.upper == "M":
        basket.append("Mango")
    elif choosefruit.upper == "G":
        basket.append("Guava")
