# Title: H SDD Usernames v2
# Author: Mr Friend
# Date: 26 Aug 2023

# Import module
import random

#
# Subprograms
#

def leftSub(text: str) -> str:
    """Return the first three characters of a string"""

    # Declare local variable
    subString = ""

    # Extract substring
    subString = text[ :3]

    # Return substring
    return subString

def rightSub(text: str) -> str:
    """Return the last three characters of a string"""

    # Declare local variable
    subString = ""

    # Extract substring
    subString = text[-3: ]

    # Return substring
    return subString

#
# Main Program
#

# Declare global variables
line = ""
data = [""] * 2
firstName = ""
lastName = ""
digit = 0
username = ""

# Open file
file = open("names.csv", "r")

# Read first line
line = file.readline()

# Loop for each line
while line != "":
    # Split line at comma
    data = line.split(",")

    # Extract names
    firstName = data[0].strip()
    lastName = data[1].strip()

    # Pick random digit
    digit = random.randint(1, 9)

    # Create username
    username = leftSub(firstName) + rightSub(lastName) + str(digit)

    # Display result
    print(username + " - " + firstName + " " + lastName)

    # Read next line
    line = file.readline()

# Close file
file.close()
