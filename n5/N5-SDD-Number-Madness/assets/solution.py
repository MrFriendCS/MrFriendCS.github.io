# Title: N5 SDD Number Madness
# Author: Mr Friend
# Date: 23 Aug 2023

# Declare variables
first = 0
second = 0
answer = 0
add = 0
subtract = 0
multiply = 0
divide = 0.0  # Divide produces real

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

# Display add and subtract
print()
print(str(second) + " added to " + str(first) + " is " + str(add))
print(str(second) + " subtracted from " + str(first) + " is " + str(subtract))

# Display multiply and divde
print()
print(str(first) + " multiplied by " + str(second) + " is " + str(multiply))
print(str(first) + " divided by " + str(second) + " is " + str(divide))
