# Title: N5 SDD Dice
# Author: Mr Friend
# Date: 11 Nov 2026

# Get extra code
import random

# Initialise variables
dice: int = 0
guess: int = 0

# Header
print("Guess the Dice Value")
print("--------------------")
print()

# Throw the dice
dice = random.randint(1, 6)

# Get guess
guess = int(input("What is your guess (1-6)? "))

# Blank line
print()

# Permission options
if guess > dice:
    
    # Too high message
    print("Your guessed too high!")
    
elif guess < dice:
    
    # Too low message
    print("Your guessed too low!")
    
else:
    
    # Correct message
    print("You guessed right!")
    

# Display what the computer picked
print()
print("The computer throw a " + str(dice))

# Footer
print("======================")
