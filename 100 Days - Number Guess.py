import random

number = random.randint(1,101)  #randomly generated number to guess
print(number)

print("Welcome to the number guessing game. \nI'm thinking of a number from 1-100.")
level = input("Would you like to play 'easy' or 'hard'? ")
attempts = 0
if level == 'hard':
    attempts = 5
else:
    attempts = 10
print(f"You have {attempts} attempts to guess the number")

def user_guess(count):

    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The number was {number}")
    elif guess > number:
        print("Too high. \nGuess again.")
        count -= 1
        print(f"You have {count} attempts left.")
        user_guess(count)
    else:
        print("Too low. \nGuess again.")
        count -= 1
        print(f"You have {count} attempts left.")
        user_guess(count)


user_guess(attempts)