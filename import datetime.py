import datetime

def ariesinrange(date1, start_date, end_date):
    if start_date <= date1 <= end_date:
        print("Hi, {name}! Your are {age} years old and your zodiac sign is {zodiac}".format(name=name, age=age, zodiac=aries1))
    else: 
        return aries    inrange(date1, start_date, end_date)
aries1="Aries"
start_date= datetime.date(1,3,21)
end_date= datetime.date(2024,4,19)


name=str(input("What is your name?:"))
age=int(input("What is your age?: "))
zodiac=(input("When is your birthday? (Format: Year-Month-Day e.g: 2006-08-26):"))
year, month, day = map(int, zodiac.split('-'))
date1= datetime.date(year, month, day)

