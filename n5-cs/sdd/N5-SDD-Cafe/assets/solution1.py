# Title: N5-SDD-Cafe
# Author: Mr Friend
# Date: 11 Dec 2025

# Initialise variables
noOfItems = 0
itemNumber = 0.0
cost = 0.0
total = 0.0

items = ["First", "Second", "Third", "Forth", "Fifth"]
costs = [1.50, 1.75, 1.00, 2.50, 2.25]

# Header
print("Cafe Tangasdale")
print("---------------")
print()

# Enter number of items
numberOfItems = int(input("How many different items: "))

# Check if number of items is valid
while numberOfItems < 1 or numberOfItems > 5:
    
    # Display error message
    print()
    print("Invalid. Please enter a number between 1 and 5.")
    
    # Re-enter number of items
    numberOfItems = int(input("How many different items: "))

# Display the menu
print()
print("Enter a number for each item:")
print(" 1 = Tea, 2 = Coffee, 3 = Can")
print(" 4 = Toastie, 5 = Cake")
print()

# Loop for each item
for index in range(numberOfItems):
    
    # Enter item number
    itemNumber = int(input(items[index] + " item: "))
    
    # Check if item number is valid
    while itemNumber < 1 or itemNumber > 5:
        
        # Display error message
        print()
        print("Invalid. Please enter a number between 1 and 5.")
        
        # Re-enter item number
        itemNumber = int(input(items[index] + " item: "))
    
    # Look up cost
    cost = costs[itemNumber - 1]
    
    # Update total
    total = total + cost

# Display total
print()
print("Order total: £" + str(total))

# Footer
print()
print("Only Bitcoin accepted")
print("=====================")
