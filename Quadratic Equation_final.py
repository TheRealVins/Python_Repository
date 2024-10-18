import math as m 
import sys as s 

#for checking; if the user inputted string or integer
def numberchecker(num):
    try:
        num=int(num)
        pass
    except ValueError:
        userinputneeded()

#for solving the discriminant
def discriminant(a,b,c):
    a,b,c=int(a),int(b),int(c)
    d=(b**2)-(4*a*c)
    print(f"The Discriminant is {d}")
    solutions(a,b,c,d)

#for solving the roots
def solutions(a,b,c,d):
    if d>0:
        x_positive=(-b+m.sqrt(d))/(2*a)
        x_negative=(-b-m.sqrt(d))/(2*a)
        print(f"Since the Discriminant is positive, the result of x is {x_positive} and {x_negative:.5f}.")
        s.exit()
    elif d==0:
        x=(-b)/(2*a)
        print(f"Since the Discriminant is zero, the result of x is {x} only.")
        s.exit()
    elif d<0:
        print(f"Since the Discriminant is negative, the result of x has 2 imaginary real numbers.")
        s.exit()

#gathering the info needed from the user
def userinputneeded():
    a=input("What is the value of a? ")
    numberchecker(a)
    b=input("What is the value of b? ")
    numberchecker(b)
    c=input("What is the value of c? ")
    numberchecker(c)
    discriminant(a,b,c)
    s.exit()

print("The standard form of quadratic equation is ax^2 + bx + c = 0.")
userinputneeded()