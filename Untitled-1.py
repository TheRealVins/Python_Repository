import re 

punctuation="The cat chased the mouse? The mouse chased the dog?"
exclamation="The cat chased the mouse! The mouse chased the dog!"
dot="The cat chased the mouse. The mouse chased the dog."

p= re.split(r'(?<=[.!?]) +', punctuation)
e= re.split(r'(?<=[.!?]) +', exclamation)
d= re.split(r'(?<=[.!?]) +', dot)

print(p)
print(e)
print(d)