# Title: N5 SDD Number Game
# Author: Mr Friend
# Date: 22 Sep 2023

"""Using structure diagram."""

# Import module
import random

# Declare variables
compNum = 0
childNum = 0

# Pick random number: 1 - 9
compNum = random.randint(1, 9)

# Display the number and get answer
childNum = int(input("What number is one bigger than " + str(compNum) + "? "))

# Is answer correct?
if childNum == compNum + 1:
    print("\nCorrect - Well done!")

# Is answer too big?
if childNum > compNum + 1:
    print("Too big!")
    print(str(num1 + 1) + " is one bigger than " + str(num1))

# Is answer too small?
if childNum < compNum:
    print("Too small!")
    print(str(num1 + 1) + " is one bigger than " + str(num1))

# Is answer same as number?
if childNum == compNum:
    print("That's the same!")
    print(str(num1 + 1) + " is one bigger than " + str(num1))
