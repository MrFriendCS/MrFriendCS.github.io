# Title: N5 SDD Summer Tasks Part 2
# Author: Mr Friend
# Date: 25 Aug 2025


# Get extra code
import random

# Initilise variables
numbers = 0
maximum = 0
value = 0
sumText = ""
sumTotal = 0
answer = 0

# Get number of numbers from user
while numbers < 2 or numbers > 5:
    numbers = int(input("How many numbers: "))
    
    # Check value
    if numbers < 2 or numbers > 5:
        print("Value must be between 2 and 5.\n")

# Get maximum value from user
while maximum <= 0:
    maximum = int(input("Largest number: "))
    
    # Check value
    if maximum <= 0:
        print("Value must be greater than 0.\n")

# Create problem
for counter in range(numbers):
    
    # Generate value to add
    value = random.randint(1, maximum)
    
    # Add value to text
    sumText = sumText + "  " + str(value)
    
    # Add value to total
    sumTotal = sumTotal + value

# Display problem
print("\nAdd the following numbers together:")
print(sumText)

# Get value from user
answer = int(input("\nWhat is the sum? "))

# Display result
if answer == sumTotal:
    print("\nCorrect!")
else:
    print("\nWrong.  It's " + str(sumTotal) + "!")
