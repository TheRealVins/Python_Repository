def options():
    choices=input("""[1] - Check Balance
[2] - Withdrawal\n[3] - Deposit\n[4] - Fund Transfer\n[5] - Transaction History\nEnter your transaction: """)
    if choices == str(1):
        return("Your balance is: $5000")
    elif choices == str(2):
        return("w")
    elif choices == str(3):
        return("D")
    elif choices == str(4):
        return("ft")
    elif choices == str(5):
        return("TH")
        
def confirmation():
    another=str(input("Would you like to make another transaction?\n[y/n]: "))
    if another.lower()=="y":
        return(options())
    if another.lower()=="n":
        print("Thank you for using my program!")
        return None
    else:
        print("Invalid Response! Try Again.")
        return(confirmation())


print("ATM MACHINE: Good Day!")
pin=int(input("Enter your pin: "))
while str(pin):
    pinagain=input("Invalid Pin! Numeric numbers only. :")
while pin or pinagain != 1234 :
    pin=int(input("Invalid! Enter your pin again: "))
if pin == 1234:
    print(options())
    while True:
        if confirmation() == None:
            break
        print(confirmation())
        