#DECISION STRUCTURES

def simple():
    var = float(input("Enter a number: "))
    if var > 15:
        print("This number is greater than 15.")
    if var > 10:
        print("This number is greater than 10.")
    if var > 5:
        print("This number is greater than 5.")

simple()

def two_way():
    var = float(input("Enter a number: "))
    if var > 5:
        print("This number is greater than 5.")
    else:
        print("This number is less than or equal to 5.")
    if var > 10:
        print("This number is greater than 10.")
    if var > 15:
        print("This number is greater than 15.")
    

two_way()

def multi_way1():
    var = float(input("Enter a number: "))
    if var > 5:
        if var > 10:
            if var > 15:
                print("This number is greater than 15.")
            else:
                print("This number is greater than 10.")
        else:
            print("This number is greater than 5")
    else:
        print("This number is less than or equal to 5.")

multi_way1()



def multi_way2():
    var = float(input("Enter a number: "))
    if var > 5:
        print("This number is greater than 5.")
    elif var > 10:
        print("This number is less than or equal 15 but greater than 10.")
    elif var > 15:
        print("This number is greater than 5 but less than or equal to 15.")
    else:
        print("This number is less than or equal to 5.")

multi_way2()

#DEFINITE LOOP SAMPLES

def defloop():
    n = int(input("Enter an integer: "))
    for var in range(n):
        print("Hello!")
        
        
defloop()


for loopvar in [1,2,3,4,5]:
    print(loopvar)
    print(loopvar*2)


n = int(input("Enter an integer: "))
n_process = n
for loopvar in range(n_process-1,1,-1):
    n_process *= loopvar
    print(n_process)
print(f"{n}! = {n_process}")


n = int(input("Enter an integer: "))
f1 = 1
f2 = 1
if n>=2:
    print(f"f1: {f1}")
    print(f"f2: {f2}")
    for loopvar in range(3,n+1):
        f = f1+f2
        print(f"f{loopvar}: {f}")
        f1 = f2
        f2 = f
elif n == 1:
    print(f1)
else:
    print("No fibonacci number")


n = int(input("Enter the number of values"))
_sum = 0
for loopvar in range(n):
    x = float(input("Enter any value: "))
    _sum += x
print(f"The average is {_sum/n}.")

#INDEFINITE LOOP SAMPLES

_sum = 0
_count = 0
moredata = 'yes'
while moredata=='yes':
    x = float(input("Enter any value: "))
    _sum += x
    _count +=1
    moredata = input("Is there another value? type 'yes'")
print(f"The average is {_sum/_count}.")


x = int(input("Enter an integer: "))
f0 = 0
f1 = 1
if x<=0:
    print(f"No Fibonacci numbers less than {x}")
else:
    while x > f0:
        print(f0)
        f = f0+f1
        f0 = f1
        f1 = f
    