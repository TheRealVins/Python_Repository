import sys as s #module for force exit
import re  #for pattern recognition (choice 5)

def choices():
    #Asks the user the options for the program
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
    #calls the function for the inputted choice of the user
    response(choice,paragraph)

def response(choice, paragraph):
    splitted= paragraph.split() #Splits all the words in the paragraph. 
    if choice=="1": #Counts all the words in the paragraph. 
        choice1(splitted)
        confirmation()
    elif choice=="2": #Counts all the characters in the paragraph except spaces. 
        choice2(splitted)
        confirmation()
    elif choice=="3": #Capitalizes either the first word of every sentence or all the words in the paragraph.
        choice3(paragraph)
        confirmation()
    elif choice=="4": #Searches the word that the user wants.
        choice4(splitted)
        confirmation()
    elif choice=="5": #Searches and replaces the word that the user wants.
        choice5(paragraph)
        confirmation()
    elif choice=="6": #Sorts every word in the paragraph using lists.
        choice6(splitted)
        confirmation()
    elif choice=="*":  #Exits the program.
        print("--------------------\nThank you for trying my program!\n--------------------")
        s.exit()
    else: 
        print("--------------------\nInvalid Response. Try again.\n--------------------")
        choices()

def choice1(splitted):
    length=len(splitted) #Gets the length of the splitted paragraph. 
    print(f"--------------------\nThe number of words in the paragraph that you entered is {length}.\n--------------------")

def choice2(splitted):
    list1=[] #Storage for all the words' length in the paragraph.
    for i in splitted: #'For every word in the paragraph'
        lenghtofword=len(i) #Gets the length of the word
        list1.append(lenghtofword) #Appends the value of the length of the word in the list
        sumofallwords = sum(list1) #Adds all the values in the list which contains the character count of every word
    print(f"--------------------\nThe character count for your paragraph is {sumofallwords}.\n--------------------")

def choice3(paragraph):
    #Input for the choices of the user
    capitalchoice=input("""--------------------\nInput '1' to capitalize the first letter of each sentence.
Input '2' to capitalize all the words.\n--------------------
Enter your choice here: """)
    sentences = re.split(r'(?<=[.!?]) +', paragraph) #Splits the paragraph into sentences (Recognizes r'(?<=[.!?]) +')
    if capitalchoice == "1":
        sentences = [sentence.capitalize() for sentence in sentences] #Capitalizes the first letter of each sentence. 
        print(' '.join(sentences))
    elif capitalchoice == "2":
        sentences = [' '.join([word.capitalize() for word in sentence.split()]) for sentence in sentences] #Capitalizes all the words in each sentence. 
        print(' '.join(sentences))
    else:
        print("--------------------\nOnly enter integer. Try again.\n--------------------") #Prints if the user inputs besides 1 and 2
        choice3(paragraph) #Loops through this function again

def choice4(splitted):
    findthatword=input("Enter the word you want to search:") #Inputs the word you want to search
    occurence=splitted.count(findthatword) #Counts all the word in the paragraph that is inputted by the user (line 78)
    if occurence>0: 
        #Prints if the occurence of the word is greater than 0.
        print(f"--------------------\nThe word {findthatword} is used {occurence} times in the paragraph.\n--------------------")
    else:
        #Prints if the word didn't occur. 
        print(f"--------------------\nThe word {findthatword} did not occur in the paragraph.\n--------------------")

def choice5(paragraph):
    word=input("Enter the word you want to replace:") #Inputs the word that will be replaced
    replacement=input("Enter the new word you want for the said word:") #Inputs the word that will be used to replace the previous word
    z=re.sub(r'\b' + re.escape(word) + r'\b', replacement, paragraph) #Splits all the words in the paragraph for recognition
    print(f"--------------------\nThe new paragraph with the replaced words:\n{z}\n--------------------") #Prints the new paragraph with the replaced words.

def choice6(splitted):
    z=sorted(splitted) #Sorts the splitted paragraph in alphabetical order. 
    print(f"--------------------\nHere is the sorted list for all the words in the sentence.\n{z}\n--------------------")
                
def confirmation():
    proceed=str(input("Do you want to try more features? (Y/N): ")) #Asks the user if it wants to continue to the program
    if proceed == 'y'.lower(): #Continue
        choices()
    elif proceed == 'n'.lower(): #End
        print("--------------------\nThank you for using my program!\n--------------------")
        s.exit()
    else: #Prints if the user inputs besides Y or N
        print("--------------------\nInvalid Input. Please put Y or N only.\n--------------------")
        confirmation() #Loops through the function

paragraph=str(input("Enter the paragraph here:")).lower() #Asks the user for the paragraph
choices()




#  Members: 
#  Urrutia, Divino Samuel I.
#
#  https://github.com/TheRealVins/Python_Repository/blob/main/Activity%207.py