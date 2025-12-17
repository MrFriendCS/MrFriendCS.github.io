# Title: Pontoon
# Author: Mr Friend
# Date: 17 Nov 2022

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

# Deal 2 cards
for counter in range(2):
    
    # Pick a random card
    card = random.randint(2, 11)
    
    # Dsiplay card
    print("Card " + str(counter + 1) + ": " + str(card))
    
    # Calculate the total
    total = total + card


# Another card?
twist = input("\nStick or twist? ")

# Check answer is valid
while twist != "s" and twist != "t":
    
    # Error message
    print("Enter 's' or 't'.")
    
    # Another card?
    twist = input("\nStick or twist? ")

# Allow another card if not bust
while twist == "t" and total <= 21:
    
    # Pick a random card
    card = random.randint(2, 11)
    
    # Swap ace for 1 if total too high
    if card == 11 and total > 10:
        card = 1
    
    # Display card
    print()
    print("You drew a " + str(card))

    # Calculate the total
    total = total + card

    # Busrt or twist?
    if total > 21:
        
        print("\nBust!")
        
    else:
        
        # Another card?
        twist = input("\nStick or twist? ")

        # Check answer is valid
        while twist != "s" and twist != "t":
            
            # Error message
            print("Enter 's' or 't'.")
            
            # Another card?
            twist = input("\nStick or twist? ")

# Display score
print("\nYou scored " + str(total))

# Display footer
print()
print("www.gambleaware.org")
print("===================")
