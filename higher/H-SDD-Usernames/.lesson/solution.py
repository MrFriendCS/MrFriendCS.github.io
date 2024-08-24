# Title: H SDD Usernames
# Author: Mr Friend
# Date: 6 Sep 2023

# Import module
import random  # used in subprogram

#
# Subprograms
#

def getUserData():
    """Read first names and last names from file and return as parallel arrays"""

    # Declare local variable and arrays
    line = ""
    tempArray = [""] * 2
    forenames = [""] * 20
    surnames = [""] * 20

    # Make a connection to the file
    file = open("employees.csv", "r")

    # Loop for each employee
    for index in range(len(forenames)):

        # Read a line from the file
        line = file.readline()

        # Split the line into an array
        tempArray = line.split(",")

        # Assign values to parallel arrays
        forenames[index] = tempArray[0].strip()
        surnames[index] = tempArray[1].strip()

    # Close the connection to the file
    file.close()

    # Return parallel arrays
    return forenames, surnames


def createUsernames(forenames, surnames):
    """Create usernames from first names and last names and return as an array"""

    # Declare local variables and array
    number = 0
    substring1 = ""
    substring2 = ""
    username = ""
    usernames = [""] * 20

    # Loop for each employee
    for index in range(len(forenames)):

        # Pick random value
        number = random.randint(3, 5)

        # Get forename substring
        substring1 = left(forenames[index], number)

        # Get surname substring
        substring2 = left(surnames[index], 8-number)

        # Create username
        username = substring1 + substring2

        # Store username
        usernames[index] = username

    # Return usernames
    return usernames


def left(text, number):
    """Returns a left substring.  Pads with underscore if short"""

    # Declare local variable
    substring = ""

    # Create substring
    substring = text[0:number]

    # Ensure substring is long enough
    while len(substring) < number:
        substring = substring + "_"

    # Return substring
    return substring
    

def saveUserData(surnames, forenames, usernames):
    """Save last names, forenames, and usernames to file"""

    # Make a connection to the file
    file = open("usernames.csv", "w")

    # Loop for each employee
    for index in range(len(forenames)):

        # Write row of data
        file.write(surnames[index] + ",")
        file.write(forenames[index] + ",")
        file.write(usernames[index] + "\n")

    # Close the connection to the file
    file.close()


#
# Main program
#

# Declare global arrays
firstNames = [""] * 20
lastNames = [""] * 20
usernames = [""] * 20

# Get user data
firstNames, lastNames = getUserData()

# Create usernames
usernames = createUsernames(firstNames, lastNames)

# Save user data
saveUserData(lastNames, firstNames, usernames)
