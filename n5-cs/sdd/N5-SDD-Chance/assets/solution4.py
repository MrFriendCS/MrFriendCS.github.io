# Title: N5 SDD - Chance Part 4
# Author: Mr Friend
# Date: 20 Nov 2026

# Get extra code
import random

# Initialise variables
compNum: int = 0
childNum: int = 0

# Pick a random number: 1 - 9
compNum = random.randint(1, 9)

# Display header
print("Plus 1 Game")
print("-----------")
print()

# Display number
print("What is 1 more than " + str(compNum) + "?")

# Blank line
print()

# Get valid answer
childNum = int(input("Answer: "))

# Check answer is valid: 1 - 10
while childNum < 1 or childNum > 10:
    
    # Blank line
    print()
    
    # Display error message
    print("Answer must be between 1 and 10.")
    
    # Get valid answer
    childNum = int(input("Answer: "))

# Blank line
print()

# Is answer correct?
if childNum == compNum + 1:
    
    print("Correct!")

# Is answer the same?
elif childNum == compNum:
    
    print("That number is the same.")
    print("The answer is " + str(compNum + 1) + ".")

# Is answer too big?
elif childNum > compNum + 1:
    
    print("That number is too big.")
    print("The answer is " + str(compNum + 1) + ".")

# Is answer too small?
else:
    
    print("That number is too small.")
    print("The answer is " + str(compNum + 1) + ".")

# Display footer
print("===========")
