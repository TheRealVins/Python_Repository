import time as t
import sys as s

def message():
    x="hello000000000000000000000\nhello000000000000000000000\nhello000000000000000000000\nhello000000000000000000000\nhello000000000000000000000"
    for char in x:
        t.sleep(0.01)
        s.stdout.write(char)
        s.stdout.flush()
def message1():
    x1="i am going to show it to you anyway"
    for char in x1:
        t.sleep(0.01)
        s.stdout.write(char)
        s.stdout.flush()

print("Password is your name!")
print("+====================+")
password=str(input("Password: "))
correctpass="Gian"
while password!=correctpass:  
    password=str(input("Wrong! Try Again: "))
else:
    message1=str(input("hawayu?"))
    message2=str(input("i have a message \ndo you want to see it? (y/n):"))
    if message2=="y"or message2=="Y":
        message()
    if message2=="n"or message2=="N":
        message1()
        message()
    else:
        print("What did you say?")