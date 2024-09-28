row= int(input("How man rows?: "))
columns= int(input("How man columns?: "))
sign= int(input("What sign do you want?: "))

for i in range(row):
    for j in range(columns):
        print(sign, end="")

    print()