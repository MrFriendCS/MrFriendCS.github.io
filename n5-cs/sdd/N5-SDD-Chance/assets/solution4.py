# Title: N5 SDD - Chance Part 4
# Author: Mr Friend
# Date: 12 Nov 2026

"""Using program analysis."""

# Import module
import random

# Declare variables
compNum: int = 0
childNum: int = 0

# Pick random number: 1 - 9
compNum = random.randint(1, 9)

# Only accept valid answers: 1 - 10
while childNum < 1 or childNum > 10:
    
    # Display the number and get answer
    childNum = int(input("What number is one bigger than " + str(compNum) + "? "))

    if childNum < 1 or childNum > 10:
        # Error message
        print("\nNumber must be from 1 to 10")

# Is answer correct?
if childNum == compNum + 1:
    print("\nCorrect - Well done!")

# Is answer too big?
elif childNum > compNum + 1:
    print("Too big!")
    print(str(childNum + 1) + " is one bigger than " + str(childNum))

# Is answer too small?
elif childNum < compNum:
    print("Too small!")
    print(str(childNum + 1) + " is one bigger than " + str(childNum))

# Is answer same as number?
else:
    print("That's the same!")
    print(str(childNum + 1) + " is one bigger than " + str(childNum))
