import random

secret = random.randint(1, 10)

guess = 0
attempts = 0

print("Welcome to the Number Guessing Game!")

while guess != secret:
    guess = input("Guess a number between 1 and 10: ")
    attempts = 1

    if guess > secret:
        print("Too low!")
    elif guess < secret:
        print("Too high!")
    else:
        print("Correct!")

print("You guessed it in", attempts, "attempts!")
