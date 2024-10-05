import sys as s
import collections as c

def movies():   
    global movielist
    movielist= c.deque([])
    for i in range(1,4):
        movie=str(input(f"Enter movie {i} of 3: "))
        movielist.append(movie)
    snacks()

def snacks():
    global snackslist
    snackslist=c.deque([])
    for i in range(1,4):
        snack=str(input(f"Enter snack {i} of 3: "))
        snackslist.append(snack)
    printingofmovies()

def printingofmovies():
    print(f"Movies to watch are: {movielist}")
    print(f"Snacks available are: {snackslist}")
    eat=str(input("Press S each time you finish a snack.\n"))
    eating(eat)

def eating(eat):
    while eat.lower()=="s":
        if len(snackslist)==1:
            print("No more snacks.")
            s.exit()
        snackslist.popleft()
        print(snackslist)
        x=str(input(""))
        eating(x)
    else: 
        print("Invalid Keyword. Try again.")
        eating()

movies()