# Title: N5 SDD RPS
# Author: Mr Friend
# Date: 21 Nov 2025

# Get extra code
import random

# Initialise variables
compRPS = 0
userRPS = ""
winner = ""

# Display header
print("Rock Paper Scissors")
print("-------------------")

# Computer picks RPS
# 0 = Rock, 1 = Paper, 2 = Scissors
compRPS = random.randint(0, 2)

# User picks RPS
print()
userRPS = input("RPS: ")

# Loop until user value is valid
while userRPS != "r" and userRPS != "p" and userRPS != "s":
    
    # Display error message
    print("Only 'r', 'p', or 's' can be used.")
    
    # User picks RPS
    userRPS = input("RPS: ")

# Blank line
print()


# Decide who one
if compRPS == 0 and userRPS == "p":
    
    print("Paper wraps rock!")
    winner = "You"

elif compRPS == 0 and userRPS == "s":
    
    print("Rock blunts scissors!")
    winner = "Computer"

elif compRPS == 1 and userRPS == "r":
    
    print("Paper wraps rock!")
    winner = "Computer"

elif compRPS == 1 and userRPS == "s":
    
    print("Scissors cut paper!")
    winner = "You"

elif compRPS == 2 and userRPS == "r":
    
    print("Rock blunts scissors!")
    winner = "You"

elif compRPS == 2 and userRPS == "p":
    
    print("Scissors cut paper!")
    winner = "Computer"
    
else:
    
    print("Draw!")
    winner = "No one"

# Display the winner
print()
print("Winner: " + winner)

# Display the footer
print("===================")
    