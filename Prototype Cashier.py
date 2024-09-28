combo=str(input("Enter your order here: "))
combo2=str(input("Would you like to order more (Write No if you dont want to Order): "))


prcombo1=150
prcombo2=175
prcombo3=120

prcombi1= prcombo1 + prcombo2
prcombi2= prcombo1 + prcombo3
prcombi3= prcombo2 + prcombo3
prcombi4= prcombo3 + prcombo3
prcombi5= prcombo2 + prcombo2

if combo=="Combo 1":
    print("This contains Chicken, Rice, and Drinks")
    print("----------------------------------------------------")
    print("The price for this combo is " + str(prcombo1))
    print("----------------------------------------------------")
if combo=="Combo 2":
    print("This contains Chicken, Rice, Fries, and Drinks")
    print("----------------------------------------------------")
    print("The price for this combo is " + str(prcombo2))
    print("----------------------------------------------------")
if combo=="Combo 3":
    print("This contains Burger Steak, Fries, And Drinks")
    print("-----------------------------------------------------")
    print("The price for this combo is " + str(prcombo3))
    print("----------------------------------------------------")

if combo2=="Combo 1":
    print("This contains Chicken, Rice, and Drinks")
    print("----------------------------------------------------")
    print("The price for this combo is " + str(prcombo1))
    print("----------------------------------------------------")
if combo2=="Combo 2":
    print("This contains Chicken, Rice, Fries, and Drinks")
    print("----------------------------------------------------")
    print("The price for this combo is " + str(prcombo2))
    print("----------------------------------------------------")
if combo2=="Combo 3":
    print("This contains Burger Steak, Fries, And Drinks")
    print("-----------------------------------------------------")
    print("The price for this combo is " + str(prcombo3))
    print("----------------------------------------------------")

if combo=="Combo 1":
    if combo2=="Combo 2":
        print("The Total for your order is: " +str(prcombi1))

if combo=="Combo 1":
    if combo2=="Combo 3":
        print("The Total for your order is: " +str(prcombi2))

if combo=="Combo 2":
    if combo2=="Combo 3":
        print("The Total for your order is: " +str(prcombi3))

if combo=="Combo 2":
    if combo2=="Combo 2":
        print("The Total for your order is: " +str(prcombi5))

if combo=="Combo 3":
    if combo2=="Combo 3":
        print("The Total for your order is: " +str(prcombi4))

if combo=="Combo 1":
    if combo2=="No":
        print("The Total for your order is: " +str(prcombo1))

if combo=="Combo 2":
    if combo2=="No":
        print("The Total for your order is: " +str(prcombo2))

if combo=="Combo 3":
    if combo2=="No":
        print("The Total for your order is: " +str(prcombo3))

