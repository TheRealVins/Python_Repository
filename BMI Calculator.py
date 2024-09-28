def printallinfo(lastname,firstname,age, weight, height):
        return(f"""===================================
Full name: {firstname} {lastname}
Age:{age}
Weight (In Kg): {weight} Kg
Height (In cm): {height} cm
===================================""")

def convertcmtoftin(lastname,firstname,height):
    x=height/float(30.48)
    return(f"""===================================
Full name: {firstname} {lastname}
Converted Height to Feet and Inches: {x:.2f} 
===================================""")

def computedbmi(lastname,firstname,height,weight):
    weightinpounds=weight*2.205
    heightininches=height/2.54
    imperialformula=703*(weightinpounds/heightininches**2)
    return(f"""===================================
Full name: {firstname} {lastname}
Body Mass Index (BMI): {imperialformula:.2f} 
===================================""")


lastname=str(input("What is your Last Name: "))
firstname=str(input("What is your First Name?: "))
age=int(input("What is your age:"))
weight=float(input("What is your weight (kg)?: "))
height=float(input("What is your height (cm)?: "))

while(True):
    option=str(input("""A. Your Information\nB. Your height in Feet and inches\nC. Your BMI\nD. End the program\nChoose:"""))
    if option.lower()=="a": 
        print(printallinfo(lastname,firstname,age, weight, height))
    elif option.lower()=="b": 
        print(convertcmtoftin(lastname,firstname,height))
    elif option.lower()=="c":
        print(computedbmi(lastname,firstname,height,weight))
    elif option.lower()=="d":
        print("""===================================\nThank you for using my program!\n===================================\n""")
        break


