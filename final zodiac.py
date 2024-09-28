name1=str(input("What is your name?: "))
age1=int(input("What is your age?: "))
month=str(input("When is the month of your birth?: "))
day=int(input("When is the day of your birth?: "))

if month == 'April':
    astro = 'Aries' if (day < 20) else 'Taurus' 
elif month == 'May':
    astro = 'Taurus' if (day < 21) else 'Gemini'
elif month == 'June':
    astro = 'Gemini' if (day < 21) else 'Cancer'
elif month == 'July':
    astro = 'Cancer' if (day < 23) else 'Leo'
elif month == 'August':
    astro = 'Leo' if (day < 23) else 'Virgo'
elif month == 'September':
    astro = 'Virgo' if (day < 23) else 'Libra'
elif month == 'October':
    astro = 'Libra' if (day < 24) else 'Scorpius'
elif month == 'November':
    astro = 'Scorpius' if (day < 22) else 'Sagittarius'
elif month == 'December':
    astro = 'Sagittarius' if (day < 22) else 'Capricornus'
elif month == 'January':
    astro = 'Capricornus' if (day < 20) else 'Aquarius'
elif month == 'February':
    astro = 'Aquarius' if (day < 19) else 'Pisces'
elif month == 'March':
    astro = 'Pisces' if (day < 21) else 'Aries'

txt=f"Hi {name1}! You are {age1} years old and your zodiac sign is {astro}."

print(txt)