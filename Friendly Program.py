"""

Define a function with function name Friendly Program. The function should
execute the following commands sequentially.

1. Greet the user with Hi there! I’m Siri.
2. Ask the name of the user and save it on variable name.
3. Greet the user with Hello <name>!.
4. Ask the birth year of the user and save it on variable birth.
5. Compute the age of the user this year and save it on age.
6. Display the age of the user in a friendly manner.
7. Display the joke What do you call a bear with no teeth? and on the 
next line display the answer A gummy bear! Try to create it using only
one line of code.
8. Display a goodbye remark in a friendly manner.

"""

def Friendly_Program():
    print("Hi there! I’m Siri.")
    name=str(input("What is your name? "))
    print(f"Hello {name}!")
    birth=int(input("What is your birthyear? "))
    age=2024-birth
    print(f"Hello {name}!, You are {age} years old.")
    print("What do you call a bear with no teeth?\nA gummy bear!")
    print(f"Goodbye {name}! See you next time!")
Friendly_Program()

"""
Members: 

Urrutia, Divino Samuel I.

"""