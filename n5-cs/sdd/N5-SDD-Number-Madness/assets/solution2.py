# Title: N5 SDD Number Madness Part 1
# Author: Mr Friend
# Date: 26 Aug 2025

# Declare variables
first = 0
second = 0
answer = 0
add = 0
subtract = 0
multiply = 0
divide = 0.0  # Division answers are real
difference = 0

# Display header
print("Number Madness!")
print("---------------")

# Get values from user
print()
first = int(input("What is the first value? "))
second = int(input("What is the second value? "))

# Calculate answers
add = first + second
subtract = first - second
multiply = first * second
divide = first / second
difference = first**2 - second**2

# Display add and subtract
print()
print(str(second) + " added to " + str(first) + " is " + str(add))
print(str(second) + " subtracted from " + str(first) + " is " + str(subtract))

# Display multiply and divde
print()
print(str(first) + " multiplied by " + str(second) + " is " + str(multiply))
print(str(first) + " divided by " + str(second) + " is " + str(divide))

# Display difference of two squares
print()
print("The square of " + str(first) +
      " minus the square of " + str(second) +
      " is " + str(difference))
