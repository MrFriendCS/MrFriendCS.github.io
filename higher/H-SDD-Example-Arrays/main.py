# Title: H SDD Arrays
# Author: Mr Friend
# Date: 28 Sep 2023

"""
A program to demonstrate the difference between global and local arrays.
"""

#
# Subprogram
#

def count():
    """
    Fills an array, either local or global, with values.
    """
    # Use local / global array
    numbers = [0] * 5  # Comment out this line to use global array

    # Loop 5 times to fill array
    for index in range(5):
        numbers[index] = index + 1

    # Display array
    print("Subprogram: " + str(numbers))


#
# Main program
#

# Declare global array
numbers = [0] * 5

# Display array
print("\nMain program: " + str(numbers)+"\n")

# Call subprogram
count()

# Display array
print("\nMain program: " + str(numbers))
