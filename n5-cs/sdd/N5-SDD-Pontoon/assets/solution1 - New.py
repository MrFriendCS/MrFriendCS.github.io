# Title: Pontoon
# Author: Mr Friend
# Date: 18 Dec 2025

# import module
import random

# Declare variables
card = 0
total = 0
twist = ""

# Display Header
print("Craigston Casino")
print("    Pontoon!")
print("----------------")
print()

# Loop 2 times
for counter in range(2):
    
    # Pick a random card value from 2 to 11
    card = random.randint(2, 11)
    
    # If card value is 11 and total score > 10
    if card == 11 and total > 10:
        
        # Set card value to 1
        card = 1
    
    # Display card value
    print("Card " + str(counter + 1) + ": " + str(card))
    
    # Add card value to total score
    total = total + card

# Get valid stick or twist from user, if total score < 21
if total < 21:

    # Another card?
    twist = input("\nStick or twist? ")

    # Check answer is valid
    while twist != "s" and twist != "t":
        
        # Error message
        print("Enter 's' or 't'.")
        
        # Another card?
        twist = input("\nStick or twist? ")

# Start conditional loop for twist and total < 21
while twist == "t" and total < 21:
    
    # Pick a random card value from 2 to 11
    card = random.randint(2, 11)
    
    # If card value is 11 and total score > 10
    if card == 11 and total > 10:
        
        # Set card value to 1
        card = 1
    
    # Display card value
    print()
    print("You drew a " + str(card))

    # Add card value to total score
    total = total + card
    
    # If total score > 21
    if total > 21:
        
        # Display "Bust!"
        print("\nBust!")
        
    elif total < 21:
        
        # Get valid stick or twist from user
        
        # Another card?
        twist = input("\nStick or twist? ")

        # Check answer is valid
        while twist != "s" and twist != "t":
            
            # Error message
            print("Enter 's' or 't'.")
            
            # Another card?
            twist = input("\nStick or twist? ")

# Display total score
print("\nYou scored " + str(total))

# Display footer
print()
print("www.gambleaware.org")
print("===================")
