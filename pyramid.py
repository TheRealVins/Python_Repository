
rows = int(input("Enter number of rows: "))

for i in range(rows):
    for l in range(i+1):
        print("* ", end="")                                     #half pyramid without arithmetics
    print()


rows=int(input("Enter the number of rows: "))



for i in range(rows): 
    for j in range(i+1):                                    #half pyramid with arithmetics
        print(j+1," ",end="")
    print()


rows = int(input("Enter number of rows: "))

for i in range(rows,0,-1):
    for l in range(i-1):
        print("*", end="")                 #inverted half pyramid without arithmetics
    print()


x=int(input("Enter the number of rows: "))

for i in range(x,0,-1):
    for j in range(1,i+1):
        print(j," ", end="")                #inverted halfpyramid with arithmetics
    print()


rows = int(input("Enter number of rows: "))  #5

k = 0 #1,2

for i in range(1, rows+1):                   #1-6 ; 1,2,3,4,5
    for space in range(1, (rows-i)+1):       #1-4
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()

"""