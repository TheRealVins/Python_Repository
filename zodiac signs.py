def zod(name1, age1, month1, day):
    ariestxt= "Hi {name}! You are {age} years old, and your zodiac sign is {zodiac}.".format(name=name1, age=age1, zodiac="Aries")
    taurustxt= "Hi {name}! You are {age} years old, and your zodiac sign is {zodiac}.".format(name=name1, age=age1, zodiac="Taurus")
    geminitxt= "Hi {name}! You are {age} years old, and your zodiac sign is {zodiac}.".format(name=name1, age=age1, zodiac="Gemini")
    cancertxt= "Hi {name}! You are {age} years old, and your zodiac sign is {zodiac}.".format(name=name1, age=age1, zodiac="Cancer")
    leotxt= "Hi {name}! You are {age} years old, and your zodiac sign is {zodiac}.".format(name=name1, age=age1, zodiac="Leo")
    ariesmonth = ["March", "April"]
    taurusmonth = ["April", "May"]
    geminimonth = ["May", "June"]
    ariesrange1= range(21,32)
    ariesrange2= range(1,20)
    taurusrange1 = range(20,31)
    taurusrange2 = range(1,21)
    geminirange1 = range(21,32)
    geminirange2 = range(1,22)
    cancerrange1 = range(22,31)
    cancerrange2 = range(1,23)

    if month1 in ariesmonth:
        if day in ariesrange1 or day in ariesrange2:
            return ariestxt
    if month1 in taurusmonth:
        if day in taurusrange1 or day in taurusrange2:
            return taurustxt
    if month1 in geminimonth:
        if day in geminirange1 or day in geminirange2:
            return geminitxt

            

name1=str(input("What is your name?: "))
age1=int(input("What is your age?: "))
month1=str(input("What is the month of your birth?: "))
day=int(input("When is the day of your birth?: "))

print(zod(name1, age1, month1, day))