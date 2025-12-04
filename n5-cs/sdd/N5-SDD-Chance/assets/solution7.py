# Title: N5 SDD Chance Part 7
# Author: Mr Friend
# Date: 21 Nov 2025

# Get extra code
import random

# Initialise variables
rps = ["r", "p", "s"]
compRPS = ""
userRPS = ""
winner = ""

# Display header
print("Rock Paper Scissors")
print("-------------------")
print()
print("Choose: r, p, or s")

# Computer picks RPS
# 0 = Rock, 1 = Paper, 2 = Scissors
compRPS = rps[random.randint(0, 2)]

# User picks RPS
print()
userRPS = input("Human: ")

# Loop until user value is valid
while userRPS != "r" and userRPS != "p" and userRPS != "s":
    
    # Display error message
    print("Only 'r', 'p', or 's' can be used.")
    
    # User picks RPS
    userRPS = input("Human: ")

# Display computer's choice
print("Computer: " + compRPS)

# Blank line
print()


# Decide who one
if compRPS == "r" and userRPS == "p":
    
    print("Paper wraps rock!")
    winner = "Human"

elif compRPS == "r" and userRPS == "s":
    
    print("Rock blunts scissors!")
    winner = "Computer"

elif compRPS == "p" and userRPS == "r":
    
    print("Paper wraps rock!")
    winner = "Computer"

elif compRPS == "p" and userRPS == "s":
    
    print("Scissors cut paper!")
    winner = "Human"

elif compRPS == "s" and userRPS == "r":
    
    print("Rock blunts scissors!")
    winner = "Human"

elif compRPS == "s" and userRPS == "p":
    
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
    