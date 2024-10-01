def options():
    choices = input("""[1] - Check Balance
[2] - Withdrawal
[3] - Deposit
[4] - Fund Transfer
[5] - Transaction History
Enter your transaction: """)
    if choices == '1':
        return "Your balance is: $5000"
    elif choices == '2':
        return "Withdrawal selected."
    elif choices == '3':
        return "Deposit selected."
    elif choices == '4':
        return "Fund Transfer selected."
    elif choices == '5':
        return "Transaction History selected."
    else:
        return "Invalid choice. Please try again."
        options()

def confirmation():
    another = input("Would you like to make another transaction? [y/n]: ").lower()
    if another == "y":
        print(options())
        confirmation()
    elif another == "n":
        print("Thank you for using my program!")
    else:
        print("Invalid response! Try again.")
        confirmation()

def isitnumber(pin):
    try:
        pin = int(pin)
        correctornot(pin)
    except ValueError:
        wrongpin = input("Wrong pin! Enter NUMERICAL characters only: ")
        isitnumber(wrongpin)

def correctornot(pin):
    if pin == 1234:
        print(options())
        confirmation()
    else:
        wrongpin = input("Wrong pin! Enter again: ")
        isitnumber(wrongpin)

print("ATM MACHINE: Good Day!")
pin = input("Enter your pin: ")
isitnumber(pin)

