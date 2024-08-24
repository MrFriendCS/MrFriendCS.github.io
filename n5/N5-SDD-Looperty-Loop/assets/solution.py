# Title: N5 SDD Looperty Loop
# Author: Mr Friend
# Date: 26 Aug 2023

# Declare variables
name = ""
number = 0


# Task 1
# Get name
name = input("What is your name? ")

# Loop
for counter in range(5):
    # Display hellos
    print("Hello " + name + ".")


# Task 2
# Get name
name = input("What is your name? ")

# Get number
number = int(input("How many times? "))

# Blank line
print()

# Loop
for counter in range(number):
    # Display hellos
    print("Hello " + name + ".")
