# Title: N5 SDD RPS
# Author: Mr Friend
# Date: 21 Nov 2025

# Get extra code
import random

# Initialise variables
compRPS = 0
userRPS = ""
winner = ""

# Computer picks RPS
# 0 = Rock, 1 = Paper, 2 = Scissors
compRPS = random.randint(0, 2)

print(compRPS)

# User picks RPS
userRPS = input("RPS: ")


while userRPS != "r" and userRPS != "p" and userRPS != "s":
    
    print("Only 'r', 'p', or 's' can be used.")
    
    # User picks RPS
    userRPS = input("RPS: ")

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
    
    print("Rock blunts cissors!")
    
    winner = "You"

elif compRPS == 2 and userRPS == "p":
    
    print("Scissors cut paper!")
    
    winner = "Computer"
    
else:
    
    print("Draw!")
    
    winner = "No one"
    
print("Winner: " + winner)
    