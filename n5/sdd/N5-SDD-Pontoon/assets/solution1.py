# Title: Pontoon
# Author: Mr Friend
# Date: 17 Nov 2022

# import module
import random

# Declare variables
card = 0
total = 0
twist = ""

# Deal 2 cards
for counter in range(2):
    
    # Pick a random card
    card = random.randint(2, 11)
    print("You drew a " + str(card))
    # Calculate the total
    total = total + card

# Another card?
twist = input("\nStick or twist? ")

# Allow another card if not bust
while twist[0] == "t" and total <= 21:
    # Pick a random card
    card = random.randint(2, 11)
    
    # Swap ace for 1 if total too high
    if card == 11 and total > 10:
        card = 1
    
    print("You drew a " + str(card))

    # Calculate the total
    total = total + card

    # Twist or bust?
    if total <= 21:
        twist = input("\nStick or twist? ")
    else:
        print("\nBust!")

# Display score
print("\nYou scored " + str(total))
