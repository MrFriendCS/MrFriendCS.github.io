# Title: N5 SDD Mean
# Author: Mr Friend
# Date: 21 Aug 2024

# Initialise variables
noOfValues = 0
value = 0.0
sum = 0.0
mean = 0.0

# Display header
print("Mean Calculator")
print("---------------")
print()

# Get number of values
noOfValues = int(input("How many values? "))

# Display a blank line
print()

# Loop for number of values
for counter in range(noOfValues):
    
    # Get value
    value = float(input("Value " + str(counter + 1) + ": "))
    
    # Add value to sum
    sum = sum + value
    
# Calculate mean
mean = sum / noOfValues

# Display a blank line
print()

# Display results
print("Sum: " + str(sum))
print("Mean: " + str(mean))
