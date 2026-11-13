# Title: N5 SDD Hello Part 4
# Author: Mr Friend
# Date: 12 Nov 2026

# Declare variables
firstName: str = ""
lastName: str = ""
age: int = 0

# Display header
print("Hello!")
print("------")
print()

# Get values from user
firstName = input("What is your first name? ")
lastName = input("What is your last name? ")
age = int(input("What is your age? "))

# Display seperator
print()
print("------")
print()

# Display text
print("Hello " + firstName + " " + lastName + ".")
print("You will be " + str(age + 1) + " at your next birthday.")
