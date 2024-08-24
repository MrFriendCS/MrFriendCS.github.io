# Title: N5 SDD Number Guess
# Author: Mr Friend
# Date: 2 Dec 2021

# Import module
import random

# Declare variables and data structures

compValue = 0
userValue = 0
correct = False
guess = 0
guesses = ["first", "second", "last"]

# Pick the number
compValue = random.randint(1, 10)

print("I've picked a number between 1 and 10.")

# Loop until correct or 3 guesses
while guess < 3 and correct == False:
    userValue = int(input("\nWhat is your " + guesses[guess] + " guess? "))

    # Only accept 1 to 10 as guesses
    while userValue < 1 or userValue > 10:
        print("\nOnly values from 1 to 10 are accepted.")
        userValue = int(input("What is your " + guesses[guess] + " guess? "))

    if userValue == compValue:
        print("\nCorrect!")
        correct = True
    elif userValue > compValue:
        print("\nToo high!")
    else:
        print("\nToo low!")

    # Increment the number of guesses
    guess = guess + 1

if correct == False:
    print("\nThe correct value was " + str(compValue) + ".")
