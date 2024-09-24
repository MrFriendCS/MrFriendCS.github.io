# Title: N5 SDD Checkout
# Author: Mr Friend
# Date 31 Aug 2024

# Initialise variables
cost = -1.0
total = 0.0
count = 1

# Display header
print("Kisimul Buth")
print("------------\n")

# Loop for cost of all items
while cost != 0.0:
    
    # Get cost of item
    cost = float(input("Item " + str(count) + ": £"))
    
    # Only accept valid values
    while cost < 0:
        # Error message
        print("\nMinimum value: 0")
        
        # Get cost of item
        cost = float(input("Item " + str(count) + ": £"))
    
    if cost != 0:
        # Increment count
        count = count + 1
        
        # Update total
        total = total + cost
        
# Adjust item count
count = count - 1

# Display total
print("\nTotal")
print("-----")

print("Items: " + str(count))
print("Cost: £" +str(total))

print("=====\n")
