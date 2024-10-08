import math as m

def discriminant(a,b,c):
    d=(b**2)-(4*a*c)
    print(f"The Discriminant is {d}")
    solutions(a,b,c,d)

def solutions(a,b,c,d):
    if d>0:
        x_positive=(-b+m.sqrt(d))/(2*a)
        x_negative=(-b-m.sqrt(d))/(2*a)
        print(f"Since the Discriminant is positive, the result of x is {x_positive} and {x_negative}.")
    elif d==0:
        x=(-b)/(2*a)
        print(f"Since the Discriminant is zero, the result of x is {x} only.")
    elif d<0:
        a*=2
        d=abs(d)
        a,b,c=str(a),str(b),str(c)
        x_positive_complex="-"+b+"/"+a+"+"+"√"+str(d)+"/"+a
        x_negative_complex="-"+b+"/"+a+"-"+"√"+str(d)+"/"+a
        print(f"Since the Discriminant is negative, the result of x is {x_positive_complex}\x1B[3mi\x1B[0m, and {x_negative_complex}\x1B[3mi\x1B[0m, which are imaginary.")

print("ax^2+bx+c=0")
a=int(input("What is the value of a? "))
b=int(input("What is the value of b? "))
c=int(input("What is the value of c? "))
discriminant(a,b,c)