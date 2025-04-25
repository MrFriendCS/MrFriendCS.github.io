# Title: N5 SDD Gross Cost
# Author: Mr Friend
# Date: 23 Aug 2023

# Declare variables and array
items = 0
cost = 0.0
net = 0.0
gross = 0.0
netTotal = 0.0
grossTotal= 0.0
costs = [0.0] * 5

# Get number of ingredients
count = int(input("How many ingredients? "))

# Ensure number is valid
while count < 3 or count > 5:
    print("Invalid.  Only 3, 4, or 5 ingredients allowed")
    count = float(input("How many ingredients? "))

print("\nNet")
print("-------------")

# Get costs of ingredients
for index in range(count):
    # Get net cost of ingredient
    cost = float(input("Cost " + str(index +1) + ": "))
    
    # Ensure net cost is valid
    while cost <= 0 or cost >= 10:
        print("Invalid.  Must be less than £10")
        cost = int(input("Item " + str(index +1) + ": "))
        
    # Store net cost
    costs[index] = cost

    # Calculate net total
    netTotal = netTotal + cost

# Display net total
print("-------------")
print("£ " + str(round(netTotal, 2)))
print("-------------")

# Display gross values
print("\nGross")
print("-------------")

for index in range(count):

    # Calculate gross
    gross = round(costs[index] * 4, 2)
    
    print("Item " +str(index + 1) + ": " + str(gross))

    # Calculate gross total
    grossTotal = grossTotal + gross

# Display gross total
print("-------------")
print("£ " + str(round(grossTotal, 2)))
print("-------------")