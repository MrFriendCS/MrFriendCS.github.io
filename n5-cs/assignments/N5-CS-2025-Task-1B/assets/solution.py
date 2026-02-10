# Title: 2025 CS Task 1B
# Author: Mr Friend
# Date: 24 Oct 2025

# Get extra code
import random

#Initialise variables
fruit = ""
counter = 0
decision = "yes"
randomNumber = 0

# initialise a data structure and store the mystery fruits
mysteryFruits = ["apple", "banana", "blueberry", "kiwi",
                 "mango", "orange", "peach", "pineapple",
                 "raspberry", "strawberry"]

# initialise a data structure to store the user's fruit selections
userFruits = [""] * 6


# Get and store valid fruit selection
while decision == "yes" and counter < 6:
    
    # Get fruit
    fruit = input("\nEnter a fruit for the drink: ")
    
    # Is length valid?
    while len(fruit) < 4:
        
        # Error message
        print("\nFruits must have a minimum of 4 letters.")
        
        # Get fruit
        fruit = input("Enter a fruit for the drink: ")

    # Store fruit
    userFruits[counter] = fruit
    
    # Add 1 to counter
    counter = counter + 1
    
    # Get and store decision
    decision = input("\nAdd another fruit? ")

# Generate a random number between 0 and 9
randomNumber = random.randint(0, 9)

# Display the fruits you entered were
print("\nThe fruits you entered were: \n")

# Display all user entered fruit names
for index in range(counter):
    
    print("\t" + userFruits[index])
    
# Display the mystery fruits is
print("\nThe mystery fruits is: \n")

# Display the randomly slected mystery fruit
print("\t" + mysteryFruits[randomNumber])

# Add 1 to counter
counter = counter + 1

# If counter < 3
if counter < 3:
    
    # Display milkshake message
    print("\nMilkshake recommended.")
    
# If counter = 3 or 4
elif counter == 3 or counter == 4:
    
    # Display smoothie message
    print("\nSmoothie recommended.")
    
else:
    
    # Display fruit juice message
    print("\nFruit juice recommended.")
    