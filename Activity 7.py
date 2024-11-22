import sys as s #module for force exit
import re 

def choices():
    choice=input("""--------------------
Welcome to my program! 
Enter the number to the feature you want to test out!
--------------------
1 = Word Count
2 = Character count
3 = Capitalization
4 = Word search
5 = Replacement
6 = Sorting
* = End the program
--------------------
Enter your option here: """)
    response(choice,paragraph)

def response(choice, paragraph):
    splitted= paragraph.split()
    if choice=="1":
        choice1(splitted)
        confirmation()
    elif choice=="2":
        choice2(splitted)
        confirmation()
    elif choice=="3":
        choice3(paragraph)
        confirmation()
    elif choice=="4":
        choice4(splitted)
        confirmation()
    elif choice=="5":
        choice5(paragraph)
        confirmation()
    elif choice=="6":
        choice6(splitted)
        confirmation()
    elif choice=="*":
        print("--------------------\nThank you for trying my program!\n--------------------")
        s.exit()
    else: 
        print("--------------------\nInvalid Response. Try again.\n--------------------")
        choices()

def choice1(splitted):
    length=len(splitted)
    print(f"--------------------\nThe number of words in the paragraph that you entered is {length}.\n--------------------")

def choice2(splitted):
    list1=[]
    for i in splitted:
        lenghtofword=len(i)
        list1.append(lenghtofword)
        summary = sum(list1)
    print(f"--------------------\nThe character count for your paragraph is {summary}.\n--------------------")

def choice3(paragraph):
    capitalchoice=input("""--------------------\nInput '1' to capitalize the first letter of each sentence.
Input '2' to capitalize all the words.\n--------------------
Enter your choice here: """)
    sentences = re.split(r'(?<=[.!?]) +', paragraph)
    if capitalchoice == "1":
        sentences = [sentence.capitalize() for sentence in sentences]
        print(' '.join(sentences))
    elif capitalchoice == "2":
        sentences = [' '.join([word.capitalize() for word in sentence.split()]) for sentence in sentences]
        print(' '.join(sentences))
    else:
        print("--------------------\nOnly enter integer. Try again.\n--------------------")
        choice3(paragraph)
    

def choice4(splitted):
    findthatword=input("Enter the word you want to search:")
    occurence=splitted.count(findthatword)
    if occurence>0:
        print(f"--------------------\nThe word {findthatword} is used {occurence} times in the paragraph.\n--------------------")
    else:
        print(f"--------------------\nThe word {findthatword} did not occur in the paragraph.\n--------------------")

def choice5(paragraph):
    word=input("Enter the word you want to replace:")
    replacement=input("Enter the new word you want for the said word:")
    z=re.sub(r'\b' + re.escape(word) + r'\b', replacement, paragraph)
    print(f"--------------------\nThe new paragraph with the replaced words.\n{z}\n--------------------")

def choice6(splitted):
    z=sorted(splitted)
    print(f"--------------------\nHere is the sorted list for all the words in the sentence.\n{z}\n--------------------")
                
def confirmation():
    proceed=str(input("Do you want to try more features? (Y/N): "))
    if proceed == 'y'.lower():
        choices()
    elif proceed == 'n'.lower():
        print("--------------------\nThank you for trying my program!\n--------------------")
        s.exit()
    else:
        print("--------------------\nInvalid Input. Please put Y or N only.\n--------------------")
        confirmation()

paragraph=str(input("Enter the paragraph here:")).lower()
choices()
    