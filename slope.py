x1=int(input("input x1: "))
y1=int(input("input y1: "))
x2=int(input("input x2: "))
y2=int(input("input y2: "))
def func(x1,y1,x2,y2):

    if x1==x2:
        return("The line is vertical, therefore, the slope is undefined.")

func(x1,y1,x2,y2)

m=(y2-y1)/(x2-x1)
b=y1-m*x1

if b<=0:
    print("Line Equation y=", m, "x+",b)
else:
    print("Line Equation y=",m, "x+",(-b))
