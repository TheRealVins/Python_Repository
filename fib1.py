def perlyn():
    x=int(input("Enter any Value: ")) #enter the first value
    y=int(input("Enter another Value: ")) #enter the second value
    chinarot=x+y #or any formula that you want
    print("Si",x,"at",y,"ay chinarot at lumabas ay", str(chinarot) + ".")
    """ (explanation for line 5)
    since we cannot concatenate integer to string, 
    i typecasted the variable 'chinarot', from integer 
    to string to concatenate to the given string line.
    """
perlyn()
