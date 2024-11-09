import time as t
import sys as s

user_balance=97432.5
user_pin="9876"

def choices():
    print("""Welcome to your bank account Ms. ABC
    0. Logout and Exit
    1. View accound balance
    2. Withdraw Cash
    3. Deposit Cash
    4. Change PIN
    5. Return Card""")

def correctpin():
    enter_pin=input("Please enter your 4-digit PIN: ")
    correctpin(enter_pin)
    if enter_pin==user_pin:
        for char in str("Account Authorized! \n"):
            t.sleep(0.1)
            s.stdout.write(char)
            s.stdout.flush()
        pass
    else:
        print("Wront PIN. Please try again.\n")
        correctpin()

def choices_conditions(number):
    if number==0:
        for char in str("Exiting..."):
            t.sleep(0.1)
            s.stdout.write(char)
            s.stdout.flush()
        print("You have been logged out. Thank you! ")
    elif number==1:
        correctpin()
        for char in str('Loading account balance...'):
            t.sleep(0.1)
            s.stdout.write(char)
            s.stdout.flush()
        print(f"Your Current Balance is {user_balance}")
    elif number==2:
        correctpin()
        for char in "Opening Cash Withdrawal...":
            t.sleep(0.1)
            s.stdout.write(char)
            s.stdout.flush()
        def checking_withdraw():
            withdraw_amount=float(input("Enter the amount you wish to withdraw: "))
            if withdraw_amount>user_balance:
                print(f"Can't withdraw {withdraw_amount}.\nPlease enter a lower amount!")
                checking_withdraw()
            else:
                print(f"Withdrawing {withdraw_amount}")
                confirmation=str(input("Confirm? Y/N: "))
                if confirmation.lower()=="y":
                    print(f"Amount withdrawn: {withdraw_amount}")
                    global updated_balance
                    updated_balance=user_balance-withdraw_amount
                    user_balance=updated_balance
                    print(f"Remaining Balance: {user_balance}")
                else: pass
        checking_withdraw()     
    elif number==3:
        correctpin()
        for char in "Loading Cash Deposit...":
            t.sleep(0.1)
            s.stdout.write(char)
            s.stdout.flush()
        def checking_deposit():
            deposit_amount=float(input("Enter the amount you wish to deposit: "))
            print(f"Withdrawing {deposit_amount}")
            confirmation=str(input("Confirm? Y/N: "))
            if confirmation.lower()=="y":
                print(f"Amount deposited: {deposit_amount}")
                global updated_balance
                updated_balance=user_balance+deposit_amount
                user_balance=updated_balance
                print(f"Remaining Balance: {user_balance}")
            else: pass
        checking_deposit()     



choices()
number=int(input("Enter a number to proceed: "))
print("\n\n")
choices_conditions(number)
    


