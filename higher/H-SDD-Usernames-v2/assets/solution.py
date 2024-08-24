# Title: H SDD Usernames v2
# Author: Mr Friend
# Date: 26 Aug 2023

# Import module
import random

#
# Subprograms
#

def leftSub(text):
    """Return the first three characters of a string"""

    # Declare local variable
    subString = ""

    # Extract substring
    subString = text[ :3]

    # Return substring
    return subString

def rightSub(text):
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
tempArray = ""
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
    tempArray = line.split(",")

    # Extract names
    firstName = tempArray[0].strip()
    lastName = tempArray[1].strip()

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
