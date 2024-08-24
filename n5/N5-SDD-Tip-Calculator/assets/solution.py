# Title: Tip Calculator
# Author: Mr Friend
# Date: 28 Sep 2022

# Initialise variables
amount = 0.0
cost = 0.0
percentage = 0.0
tip = 0.0
total = 0.0
individual = 0.0

# Loop 4 times
for counter in range(4):

    # Get valid amount
    amount = float(input("Person " + str(counter + 1) + ": "))

    # Check valid
    while amount < 0 or amount > 25:
        # Error message
        print("Amount must be from 0 to 25")
        # Re-enter amount
        amount = float(input("Person " + str(counter + 1) + ": "))

    # Add amount to cost
    cost = cost + amount

# Get valid percentage
percentage = float(input("\nTip percent: "))

# Check valid
while percentage < 0 or percentage > 20:
    # Error message
    print("Percentage must be from 0 to 20")
    # Re-enter percentage
    percentage = float(input("Tip percent: "))

# Calculate tip
tip = cost * (percentage / 100)

# Round tip to 2 dp
tip = round(tip, 2)

# Calculate total
total = cost + tip

# Display cost
print("\nCost: £" + str(cost))

# Display tip
print("Tip: £" + str(tip))

# Display total
print("\nTotal: £" + str(total))

# Calculate individual cost
individual = total / 4

# Round individual to 2 dp
individual = round(individual, 2)

# Display individual cost
print("\nEach pays: £" + str(individual))
