def isitnumber(num1,num2):
    try:
        num1=int(num1)
        num2=int(num2)
        calculator(num1,num2)
    except ValueError:
        print("Invalid Syntax. Only enter numbers.")
        wrongnum1=input('num1: ')
        wrongnum2=input('num2: ')
        isitnumber(wrongnum1,wrongnum2)

def calculator(num1,num2):
    operation=input("""Select an operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
Your Choice: """)
    if operation=="1":
        print(addition(num1,num2))
    elif operation=="2":
        print(subtraction(num1,num2))
    elif operation=="3":
        print(multiplication(num1,num2))
    elif operation=="4":
        print(division(num1,num2))
    else: 
        print("Wrong Syntax. Try Again. ")
        calculator(num1,num2)

def addition(num1,num2):
    return(num1+num2)
def subtraction(num1,num2):
    return(num1-num2)
def multiplication(num1,num2):
    return(num1*num2)
def division(num1,num2):
    if num2==0:
        return("Division by zero is not allowed.")
    else:
        return(num1/num2)
    
num1=input('num1: ')
num2=input('num2: ')
isitnumber(num1,num2)

