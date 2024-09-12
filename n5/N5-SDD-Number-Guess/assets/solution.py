# Title: N5 SDD Number Guess
# Author: Mr Friend
# Date: 3 Sep 2024

# Import module
import random

# Initialise variables
compValue = 0
guess = 0
found = False
life = 3
guesses = ["last", "second", "first"]

# Pick random number
compValue = random.randint(1, 10)

# Display header
print("Number Guess")
print("------------")
print("I've picked a number between 1 and 10.")

# Repeat until guess is correct or no lives left
while life > 0 and found != True:
    
    #Get valid guess
    guess = int(input("\nWhat is your " + guesses[life-1] + " guess? "))

    # Only accept 1 to 10 as guesses
    while guess < 1 or guess > 10:
        print("Only values from 1 to 10 are accepted.")
        userValue = int(input("\nWhat is your " + guesses[life] + " guess? "))
    
    # Is guess correct?
    if guess == compValue:
        # Yes
        found = True
    
    else:
        # No
        life = life - 1
        
        # Is guess too high?
        if guess > compValue:
            # Yes
            print("Too high!")
        else:
            # No
            print("Too low!")

# Guessed correctly?
if found == True:
    # Yes
    print("Correct!")

else:
    # No
    print("\nThe correct value was " + str(compValue) + ".")
