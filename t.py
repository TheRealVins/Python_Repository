print("ATM MACHINE: Good Day!")
pin=int(input("Enter your pin: "))
while pin==str(pin):
    pinagain=input("Invalid Pin! Numeric numbers only. :")
    if pinagain or pin == int(pin,pinagain):
        continue
while pin or pinagain != 1234 :
    pin=int(input("Invalid! Enter your pin again: "))
if pin or pinagain == 1234:
    print(options())
    while True:
        if confirmation() == None:
            break
        print(confirmation())
        