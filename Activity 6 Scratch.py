"""
name=input("Enter a name: ").lower()
list1=[]
for char in name: 
    x1 = ord(char)
    final = x1-96
    list1.append(final)

print(sum(list1))

def cc():
    word = input("enter the original word")
    key = int(input("input any integer: "))
    list1=[]
    for char in word:
        x1=ord(char)
        final= x1 + key
        finalchr= chr(final)
        list1.append(finalchr)
    for i in list1:
        print(i,end="")

cc()
    
"""

