def isitnumber(pin):
    try:
        pin=int(pin)
        correctornot(pin)
    except ValueError:
        wrongpin2=input("Wrong pin! Enter NUMERICAL characters only: ")
        isitnumber(wrongpin2)
    else:
        pass

def correctornot(pin):
    if pin==1234:
        print(options())
        confirmation()
    if pin!=1234:
        wrongpin=input("Wrong pin! Enter again: ")
        isitnumber(wrongpin)

def options():
    choices=int(input("""[1] - Check Balance
[2] - Withdrawal\n[3] - Deposit\n[4] - Fund Transfer\n[5] - Transaction History\nEnter your transaction: """))
    if choices == 1:
        return("Your balance is: $5000")
    elif choices == 2:
        return("w")
    elif choices == 3:
        return("D")
    elif choices == 4:
        return("ft")
    elif choices == 5:
        return("TH")
        
def confirmation():
    another=input("Would you like to make another transaction?\n[y/n]: ")
    if another.lower()=="y":
        print(options())
        print(confirmation())
    elif another.lower()=="n":
        return("Thank you for using my program!")
        # endprogram()
    else:
        print("Invalid Response! Try Again.")
        return(confirmation())

def endprogram():
    while confirmation():
        if confirmation()== None:
            break

print("ATM MACHINE: Good Day!")
pin=input("Enter your pin: ")
print(isitnumber(pin))