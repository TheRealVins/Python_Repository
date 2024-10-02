import time as t
import sys as s

def wordsneeded():
    noun1=str(input("Give me a noun: "))
    pluralnoun1=str(input("Give me a plural noun: "))
    verbendsining1=str(input("Give me a verb ending in -ing: "))
    pluralnoun2=str(input("Give me a plural noun: "))
    city1=str(input("Give me a city name: "))
    pluralnoun3=str(input("Give me a plural noun: "))
    adjective1=str(input("Give me an adjective: "))
    noun2=str(input("Give me a noun: "))
    number1=int(input("Give me a number: "))
    noun3=str(input("Give me a noun: "))
    adjective2=str(input("Give me an adjective: "))
    verb1=str(input("Give me a verb: "))
    verb2=str(input("Give me a verb: "))
    pluralnoun4=str(input("Give me a plural noun: "))
    verbendsining2=str(input("Give me a verb ending in -ing: "))
    number2=str(input("Give me a number: "))
    adverb1=str(input("Give me an adverb: "))
    noun4=str(input("Give me a noun: "))
    adjective3=str(input("Give me an adjective: "))

    madlibsgenerator(noun1,pluralnoun1,verbendsining1,pluralnoun2,city1,pluralnoun3,adjective1,noun2,number1,noun3,adjective2,verb1,verb2,pluralnoun4,verbendsining2,number2,adverb1,noun4,adjective3)

def madlibsgenerator(noun1,pluralnoun1,verbendsining1,pluralnoun2,city1,pluralnoun3,adjective1,noun2,number1,noun3,adjective2,verb1,verb2,pluralnoun4,verbendsining2,number2,adverb1,noun4,adjective3):
    story=(f"""In 1981, the U.S launched the first real space \x1B[4m{noun1}\x1B[0m. It was
named \x1B[3mColumbia\x1B[0m and was piloted by two brave \x1B[4m{pluralnoun1}\x1B[0m. 
They had practiced \x1B[4m{verbendsining1}\x1B[0m for two years and were
expert \x1B[4m{pluralnoun2}\x1B[0m. \x1B[3mColumbia\x1B[0m took off from \x1B[4m{city1}\x1B[0m
using its powerful first-stage \x1B[4m{pluralnoun3}\x1B[0m and soared off into the
\x1B[4m{adjective1}\x1B[0m blue \x1B[4m{noun2}\x1B[0m. At an altitude of \x1B[4m{number1}\x1B[0m
feet, it went into orbit around the \x1B[4m{noun3}\x1B[0m. For people watching
from Earth, it was a/an \x1B[4m{adjective2}\x1B[0m sight to \x1B[4m{verb1}\x1B[0m!
Who could really \x1B[4m{verb2}\x1B[0m that there were two \x1B[4m{pluralnoun4}\x1B[0m
in space? It was mind \x1B[4m{verbendsining2}\x1B[0m. After \x1B[4m{number2}\x1B[0m orbits,
the shuttle landed \x1B[4m{adverb1}\x1B[0m at an air force \x1B[4m{noun4}\x1B[0m.
It was a/an \x1B[4m{adjective3}\x1B[0m day for the U.S. Space Program.""")
    
    for char in story:
        t.sleep(0.1)
        s.stdout.write(char)
        s.stdout.flush()

wordsneeded()
    