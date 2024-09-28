"""
def average():
    numbers = []
    while True:
        x= input("Enter an integer (or 'end' to finish): ")
        if x == "end":
            break
        try:
            number = int(x)
            numbers.append(number)  

        except ValueError:
            continue
    
    if numbers:
        average = sum(numbers) / len(numbers)
        print(f"The average of the entered integers is: {average}")
    else:
        print("No integers were entered.")

average()
"""
def func():
    number=[]
    while True: 
        x=int(input("Enter a number ; (Type any string to end): ")) 
        number.append(x)
    if False: 
        average=sum(number)/len(number)
        print(average)
func()

