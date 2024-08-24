# Title: H SDD Variables
# Author: Mr Friend
# Date: 28 Sep 2023

"""
A program to demonstrate the difference between global and local variables.
"""

#
# Subprogram
#

def count():
    """
    Increments a variable, either local or global, by one and display the value.
    """
    # Use local variable
    number = 0  # Comment out this line, or line 14

    # Use global variable
    # global number  # Comment out this line, or line 11

    # Loop 5 times
    for counter in range(5):

        # Increment variable
        number = number + 1

        # Display variable
        print("Subprogram: " + str(number))


#
# Main program
#

# Declare global variable
number = 0

# Display variable
print("\nMain program: " + str(number)+"\n")

# Call subprogram
count()

# Display variable
print("\nMain program: " + str(number))
