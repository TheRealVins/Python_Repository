# Variables
x="Fundamentals of"
x1=" Computing 1"
greetings="Hello! "
seq="Sequence Data Types Operations"
list_1=[1,2,3,4,5]
list_2=["a","b","c","d","e"]
tuple_1=(6,7,8,9,10)
tuple_2=("f","g","h","i","j")
string="string methods"
string1="      string methods         "
string2="String Methods String Methods"
string3="STRING METHODS"
string4="String Methods"

#Sequence Data Types Operations
#Strings
def strings(x,x1,greetings,seq):
    print(x+x1)
    print(greetings*2)
    print(seq[0])
    print(seq[0:19])
    print(len(seq))
    print("Z"in seq)

#Lists
def lists(list_1,list_2):
    print(list_1+list_2)
    print(list_2*2)
    print(list_1[4])
    print(list_1[0:3])
    print(len(list_1))    
    print('a' in list_2)

#Tuples
def tuples(tuple_1,tuple_2):
    print(tuple_1+tuple_2)
    print(tuple_2*2)
    print(tuple_1[4])
    print(tuple_1[0:3])
    print(len(tuple_1))    
    print('a' in tuple_2)

#String Methods
def string_methods(string,string1,string2,string3,string4):
    print(string.capitalize())
    print(string.center(25))
    print(string.count("s"))
    print(string.endswith("s"))
    print(string.index("m"))
    print("#".join(string))
    print(string.ljust(20),"is our topic.")
    print(string3.lower())
    print(string1.lstrip())
    print(string4.replace("String","Integer"))
    print(string2.rindex("Methods"))
    print(string4.rjust(20),"is our topic.")
    print(string1.rstrip())
    print(string4.split())
    print(string4.startswith("A"))
    print(string1.strip())
    print(string.title())
    print(string.upper())
