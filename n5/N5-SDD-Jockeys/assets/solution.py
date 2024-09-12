# Title: Jockey Selector
# Author: Mr Friend
# Date: 12 Sep 2024

# Initialise variables
height = 0.0
weight = 0.0

# Display header
print("Jockey Selector")
print("---------------\n")

# Get values from user
height = float(input("Height (m): "))
weight = float(input("Weight (kg): "))

# Blank line
print()

# Check criteria
if height <= 1.00 and weight <= 15.0:
    # Criteria met
    print("You are a potential jockey")

elif height > 1.00 and weight <= 15.0:
    print("You do not meet the height criteria")
    
elif height <= 1.00 and weight > 15.0:
    print("You do not meet the weight criteria")
    
else:
    print("You do not meet the height or weight criteria")
    
# Display footer
print("===============")