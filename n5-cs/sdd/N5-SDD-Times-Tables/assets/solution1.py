# Title: N5 Times Tables
# Author: Mr Friend
# Date: 18 Sep 2025

# Initialise variables
table = 0

# Display header
print("Times Table Generator")
print("---------------------")
print()

# Get table from user
table = int(input("Which times table? "))

# Dsiplay text
print()
print("Times table:")
print()

# Loop for each value
for counter in range(1, 11):
    
    # Display a value
    print("  " + str(counter) + " x " + str(table) + " = " + str(counter * table))

# Display the footer
print()
print("=====================")