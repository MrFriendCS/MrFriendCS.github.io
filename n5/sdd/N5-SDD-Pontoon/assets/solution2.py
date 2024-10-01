# Title: Pontoon
# Author: Mr Friend
# Date: 1 Oct 2024

# import module
import random

# Initialise variables
noOfPlayers = 0
name = ""
card = 0
twist = ""
bust = False

# Display header
print("Pontoon")
print("-------\n")

# Get valid number of players
while noOfPlayers < 2 or noOfPlayers > 8:
    
    # Get number of players
    noOfPlayers = int(input("How many players? "))
    
    # Check
    if noOfPlayers < 2 or noOfPlayers > 8:
        
        # Error message
        print("\nOnly 2 to 8 players allowed.")


# Initialise arrays
names = [""] * noOfPlayers
scores = [0] * noOfPlayers

# Get players' names
print("\nEnter names")
print("-----------")


# Repeat for each player
for index in range(noOfPlayers):
    
    # Get name
    name = input("Player " + str(index+1) + ": ")
    
    # Get valid name
    while len(name) < 2:
        
        # Error message
        print("\nNames must have a minimum of 2 letters.")
        
        # Get name
        name = input("Player " + str(index+1) + " name: ")
    
    # Store player's name
    names[index] = name


# Repeat for each player
for index in range(noOfPlayers):
    
    # Pick a value for two cards
    cardScore = random.randint(4, 21)
    
    # Store player's score
    scores[index] = cardScore


# Repeat for each player
for index in range(noOfPlayers):

    # Reset variables
    twist = ""
    bust = False
    
    # Display player's name and score
    print("\nPlayer " + str(index+1) + ": " + names[index])
    print("Score: " + str(scores[index]))
        
    # Repeat until stick or bust
    while twist != "stick" and not bust:

        # Reset variables
        twist = ""
        
        while twist != "twist" and twist != "stick":
        
            # Get stick or twist
            twist = input("\nTwist or Stick? ")
            
            # Check
            if twist != "twist" and twist != "stick":
                
                # Error message
                print("Only use 'twist' or 'stick'.")
            
        # twist?
        if twist == "twist":

            # Pick a value for a card
            cardScore = random.randint(2, 11)
            
            # Card = 11 and score > 10?
            if cardScore == 11 and scores[index]:
                
                # Set card value to 1
                cardScore = 1
            
            # Display card value
            print("Card: " + str(cardScore))
                
            # Add card value to card score
            scores[index] = scores[index] + cardScore
            
            # Is score > 21?
            if scores[index] > 21:
            
                # Set bust to true
                bust = True
                
                # Display bust
                print("Bust!")


# Display results
print("\nResults")
print("-------")

# Repeat for each player
for index in range(noOfPlayers):
    
    # Display palyer's name and score
    print(names[index] + ": " + str(scores[index]))
    
# Display footer
print("=======\n")
