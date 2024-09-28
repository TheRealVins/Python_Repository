x=int(input("First Number:"))
y=int(input("Second Number:"))

def multiorsum(x,y):

    product = (x*y)

    if product <=100:
        return product
    else: 
        return(x+y)

result= multiorsum(x,y)
print(f"The result is {result}.")
