# Title: N5 SDD Menu Options (Group Task)
# Author: Mr Friend
# Date 26 Oct 2023

# Import module
import random

# Declare variables
option = 0
value1 = 0.0
value2 = 0.0
result = 0.0
dp = 0
phrase = ""
loop = 0
value = 0.0
total = 0.0

# Display Menu Options
print("Menu")
print("----")
print("1. Add two values together")
print("2. Divide one value by another, and round result")
print("3. Raise one value by the power of another")
print("4. Calculate the length of a word or phrase")
print("5. Pick a random value")
print("6. Add any number of values together")

# Get user choice
while option < 1 or option > 6:
    option = int(input("\nOption: "))

    # Check if valid
    if option < 1 or option > 6:
        # Error message
        print("\tOption must be 1 to 6")

#
# Options
#

# 1. Add two values together
if option == 1:
    # Get values
    value1 = float(input("\nEnter first value: "))
    value2 = float(input("Enter second value: "))

    # Calculate answer
    answer = value1 + value2

    # Display answer
    print("\n\t" + str(value1) + " + " + str(value2) + " = " + str(answer))

# 2. Divide one value by another, and round result
elif option == 2:
    # Get values
    value1 = float(input("\nEnter the dividend: "))

    while value2 == 0:
        value2 = float(input("Enter the divisor: "))

        # Check if valid
        if value2 == 0:

            # Eroor message
            print("\tDivision by zero is not allowed!\n")

    dp = int(input("Decimal places: "))

    # Calculate answer
    answer = value1 / value2

    # Round result
    answer = round(answer, dp)

    # Display answer
    print("\n\t" + str(value1) + " / " + str(value2) + " = " + str(answer) + " (" + str(dp) + " dp)")

# 3. Raise one value by the power of another
elif option == 3:
    # Get values
    value1 = float(input("\nEnter fthe base: "))
    value2 = float(input("Enter the exponent: "))

    # Calculate answer
    answer = value1 ** value2

    # Display answer
    print("\n\t" + str(value1) + " ** " + str(value2) + " = " + str(answer))

# 4. Calculate the length of a word or phrase
elif option == 4:

    while len(phrase) < 2:
        # Get phrase
        phrase = input("\nEnter word / phrase: ")

        # Check if valid
        if len(phrase) < 2:

            # Error message
            print("\tThat doesn't count as a word or phrase!")

    # Calculate answer
    answer = len(phrase)

    # Display answer
    print("\n\tThe length of '" + phrase + "' is " + str(answer) + " characters")

# 5. Pick a random value
elif option == 5:
    # Get values
    value1 = int(input("\nEnter minimum value value: "))
    value2 = int(input("Enter maximum value: "))

    # Pick random value
    answer = random.randint(value1, value2)

    # Display answer
    print("\n\tA random value from " + str(value1) + " to " + str(value2) + " is " + str(answer))

# 6. Add any number of values together
elif option == 6:

    # Get number of values
    while loop < 2:
        loop = int(input("\nEnter number of values to add: "))

        # Check if valid
        if loop < 2:
            print("Must be a minimum of 2")

    # Declare array
    values = [0.0] * loop

    # Get values
    for index in range(loop):
        # Get value
        value = float(input(str(index + 1) + ". Value: "))

        # Store value
        values[index] = value

        # Increase total
        total = total + value

    # Display answer
    print("\n\tValues")
    print("\t------")

    # Traverse 1D array
    for index in range(loop):
        print("\t" + str(index + 1) + ": " + str(values[index]))

    # Display total
    print("\n\tTotal of the " + str(loop) + " values is " + str(total))
