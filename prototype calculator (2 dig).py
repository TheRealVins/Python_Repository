def operation_s(num1, num2):
    txt="The Two Numbers you want to {operations} is {num1} and {num2}.".format(operations=operation, num1=num1, num2=num2)

    print(txt)

    result_add=num1+num2
    result_subtract=num1-num2
    result_multiply=num1*num2
    result_divide=num1/num2
    
    if operation == str("Add"):
        return result_add
    if operation == str("Subtract"):
        return result_subtract
    if operation == str("Multiply"):
        return result_multiply
    if operation == str("Divide"):
        return result_divide

num1=int(input("Enter your First number: "))
num2=int(input("Enter your Second number: "))
operation=str(input("Enter the operation you want (Add, Subtract, Multiply, Divide): "))

print("The Result is: ", operation_s(num1, num2))
