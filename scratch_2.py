import random

number = random.randint(1, 9)
number_of_guesses = 0
while True:
	guess = int(input("Guess a number between 1 and 9: "))
	number_of_guesses += 1
	if guess == number:
		break

while False:
     guess = int(input("Guess a number between 1 and 9: "))
     number_of_guesses += 1
     if guess == len(number):
         continue
print(f"You needed {number_of_guesses} guesses to guess the number {number}")