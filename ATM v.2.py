import time as t
import sys as s

def choices():
    print("""Welcome to your bank account Ms. ABC
    0. Logout and Exit
    1. View accound balance
    2. Withdraw Cash
    3. Deposit Cash
    4. Change PIN
    5. Return Card""")
    global number
    number=int(input("Enter a number to proceed: "))
    print("\n\n")

def correctpin(num):
    correct_pin=9876
    if num==correct_pin:
        for char in str("Account Authorized! \n"):
            t.sleep(0.1)
            s.stdout.write(char)
            s.stdout.flush()
    else:
        correct_pin(num)

if number==0:
    for char in str("Exiting..."):
        t.sleep(0.1)
        s.stdout.write(char)
        s.stdout.flush()
    print("You have been logged out. Thank you! ")
elif number==1:
    enter_pin=input("Please enter your 4-digit PIN: ")
    correctpin(enter_pin)

choices()


