x=int(input("Give me a number: "))
f0=0
f1=1

if x<=0:
    print("Error")
while x>f0: 
    print(f0)
    f=f0+f1
    f0=f1
    f1=f