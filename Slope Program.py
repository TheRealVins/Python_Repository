def slope(x1,x2,y1,y2,/):
    if x1==x2:
        return("The line is vertical; slope is undefined.")
    m=int((y2-y1)/(x2-x1))
    b=int(y1-m*x1)
    print(f"Slope (m): {m}")
    print(f"Y-Intercept (b): {b}")
    if b>=0:
        return(f"Line Equation: y = {m}x+{b}")
    else:
        return(f"Line Equation: y = {m}x+(-{b})")

x1=int(input("x1: "))
x2=int(input("x2: "))
y1=int(input("y1: "))
y2=int(input("y2: "))

print(slope(x1,x2,y1,y2))