import sys as s

def isitnumber(pin):
    try:
        pin=int(pin)
        correctornot(pin)
    except ValueError:
        wrongpin2=input("===================================\nWrong pin! Enter NUMERICAL characters only: ")
        isitnumber(wrongpin2)
    else:
        pass
    
def correctornot(pin):
    if pin==1234:
        print(options())
        confirmation()
    if pin!=1234:
        wrongpin=input("===================================\nWrong pin! Enter again: ")
        isitnumber(wrongpin)

def options():
    choices=input("""===================================\n[1] - Check Balance
[2] - Withdrawal\n[3] - Deposit\n[4] - Fund Transfer\n[5] - Transaction History\nEnter your transaction: """)
    if choices == '1':
        return("===================================\nYour balance is: $5000\n===================================")
    elif choices == '2':
        return("w")
    elif choices == '3':
        return("D")
    elif choices == '4':
        return("ft")
    elif choices == '5':
        return("TH")
    else: 
        print("Invalid Response! Try Again.")
        return(options())
        
def confirmation():
    another=input("Would you like to make another transaction?\n[y/n]: ")
    if another.lower()=="y":
        print(options())
        print(confirmation())
    elif another.lower()=="n":
        print("Thank you for using my program!")
        s.exit()
    else:
        print("Invalid Response! Try Again.")
        return(confirmation())

def withdrawal():
    withdrawamount=int(input("Enter the amount you want to withdraw: "))
    
    
print("ATM MACHINE: Good Day!\n===================================")
pin=input("\x1B[3mEnter your pin:\x1B[0m ")
print(isitnumber(pin))