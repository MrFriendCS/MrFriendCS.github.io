# Title: N5 CS 2020 Task 2B
# Author: Mr Friend
# Date: 18 Jan 2020

# Import random module
import random

# Declare variables
numberOfItems = 0
bill = 0.00
roundedBill = 0.0
itemType = ""
randomNumber = 0

# Get number of bill items from user
numberOfItems = int(input("How many items are there to bill? "))

# Loop for the number of items
for counter in range(numberOfItems):
    
    # Get valid item type from user
    itemType = input("Enter the item type:")
    while itemType != "c" and itemType != "b" and itemType != "t":
        # Display error message
        print("Item type must be: c, b, or t")
        # Re-enter item type
        itemType = input("Enter the item type:")
    
    # Add item to bill
    if itemType == "c":
        bill = bill + 2.25
    
    elif itemType == "t":
        bill = bill + 1.85
    else:
        bill = bill + 3.05

# Store a random integer between 1 and 10
randomNumber = random.randint(1, 10)

# Decide how much of a discount
if randomNumber == 1:
    bill = 0.00

if randomNumber >= 2 and randomNumber <= 6:
    bill = bill / 2

# Display random integer
print("The random value is " + str(randomNumber))

# Round bill to 2 decimal places
roundedBill = round(bill, 2)

# Display customer's final bill to 2 decimal places
print("The final bill is £" + str(roundedBill))
