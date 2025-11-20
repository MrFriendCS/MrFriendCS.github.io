# Title: N5 SDD Coin Flipper Part 2
# Author: Mr Friend
# Date: 20 Nov 2025

# Get extra code
import random

# Intialise variables
coin = 0
guess = ""

# Flip coin
coin = random.randint(0, 1)

# Display header
print("Coin Flipper")
print("------------")

# Get guess from user
print()
guess = input("Heads or Tails? ")

# Repeat until guess is valid
while guess != "h" and guess != "t":
    
    # Display error message
    print()
    print("Only 'h' or 't' can be used.")
    
    # Get guess from user
    print()
    guess = input("heads or Tails? ")
    
# Is coin and guess both heads?
if coin == 0 and guess == "h":
    
    # Display correct message
    print()
    print("Correct!  It was heads.")

# Is coin and guess both tails?
elif coin == 1 and guess == "t":
    
    # Display correct message
    print()
    print("Correct!  It was tails.")
    
# Is coin and guess both tails?
else:
    
    # Display incorrect message
    print()
    print("Incorrect!")
    
    # Was it heads
    if coin == 0:
        
        # Display heads message
        print("It was heads!")
        
    else:
        
        # Display tails message
        print("It was tails!")

# Display footer
print()
print("============")