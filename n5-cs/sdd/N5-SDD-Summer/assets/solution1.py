# Title: N5 SDD Summer Tasks
# Author: Mr Friend
# Date: 25 Aug 2025


# Initilise variables
value = 0
root = 0
result = ""

# Get value from user
value = int(input("Enter a value: "))

# Calculate result
root = value ** 0.5

# Check if decimal places
if root == round(root):
    
    # Round to 0 dp
    result = str(round(root))
    
else:
    
    # Round to 3 dp
    result = str(round(root, 3))
    
# Display result
print("The root of " + str(value) + " is " + result)
