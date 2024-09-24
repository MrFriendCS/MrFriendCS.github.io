# Title: H SDD Network Usernames
# Author: Mr Friend
# Date: 23 Nov 2023

#
# Sub-programs
#

def getData():
    """Read pupil data from file.  Return parallel arrays."""
    # Declare local variables
    forenames = [""] * 25
    surnames = [""] * 25
    ages = [0] * 25
    line = ""
    data = [""]* 3

    # Connect to file
    file = open("batch1.csv", "r")

    # Loop for each pupil
    for index in range(len(ages)):
        # Read row of data from file
        line = file.readline()

        # Split data at commas
        data = line.split(",")

        # Store data in parallel arrays
        forenames[index] = data[0].strip()
        surnames[index] = data[1].strip()
        ages[index] = int(data[2].strip())

    # Close connection to file
    file.close()

    # Return arrays
    return forenames, surnames, ages

def makeUsernames(forenames, surnames, ages):
    """Generate an array of usernames using forenames, and surname if needed"""

    # Declare local variables
    usernames = [""] * len(forenames)
    usernameU = ""
    usernameL = ""
    digit = 0
    letter = ""

    # Loop for each pupil
    for index in range(len(forenames)):

        # Get first 6 charcters of username
        if len(forenames[index]) >= 6:
            usernameU = forenames[index][0:6]

        else:
            # Add forename
            usernameU = forenames[index]

            # Add letters from surname
            usernameU = usernameU + surnames[index][0:6-len(usernameU)]

        # Convert any uppercase to lowercase
        for letter in usernameU:
            usernameL = usernameL + u2l(letter)

        # Add single digit
        usernameL = usernameL + str(getDigit(ages[index]))

        # Add signle leter
        usernameL = usernameL + getLetter(surnames[index][0])

        # Store username in array
        usernames[index] = usernameL

        # Reset usernameL
        usernameL = ""

    # Return usernames
    return usernames

def findOldest(ages):
    """Finds the oldest age in an array of ages"""

    # Declare local variables
    oldest = 0

    # Assign first age as oldest
    oldest = ages[0]

    # Loop for each reamining ageage
    for index in range(1, len(ages)):

        # Check to see if older
        if ages[index] > oldest:
            # Update oldest
            oldest = ages[index]

    # Return oldest age
    return oldest

def summary(forenames, surnames, ages, oldest):
    """Display a list of the oldest pupils in the batch"""

    # 4.1 Display "The oldest pupils are aged " + oldest
    print("The oldest pupils are aged " + str(oldest))

    # 4.2 Display "They are: "
    print("\nThey are:\n")

    # 4.3 Loop for twenty five pupils
    for index in range(25):

        # 4.4 If current pupil's age is same as oldest then
        if ages[index] == oldest:

            # 4.5 Display pupil's name
            print(forenames[index] + " " + surnames[index])

        # 4.6 End if
    # 4.7 End loop

def writeData(usernames, forenames, surnames):

    # Create a file
    file = open("usernames1.csv", "w")

    # Loop for each pupil
    for index in range(len(usernames)):
        # Write username
        file.write(usernames[index] + ",")
        # Write forename
        file.write(forenames[index] + ",")
        # Write surname
        file.write(surnames[index] + "\n")

    # Close file
    file.close()

def u2l(upper):
    """Converts an uppercase character to lowercase"""

    # Declare local variables
    upperASCII = 0
    lowerASCII = 0
    lower = ""

    # Character to ASCII
    upperASCII = ord(upper)

    # Convert if A to Z
    if upperASCII >= 65 and upperASCII <= 90:
        lowerASCII = upperASCII + 32
        lower = chr(lowerASCII)
    else:
        lower = upper

    # Return character
    return lower

def getDigit(age):
    """Returns remainder plus 1 of number divided by 9"""

    # Declare local variables
    remainder = 0
    plus1 = 0

    # Calculate remainder
    remainder = age % 9

    # Add 1
    plus1 = remainder + 1

    # Return result
    return plus1

def getLetter(upper):
    """Returns next lower lowercase letter in alphabet"""

    # Declare local variables
    lower = ""
    lowerASCII = 0
    nextASCII = 0
    next = ""

    # Convert uppercase to lower
    lower = u2l(upper)

    # Convert to ASCII
    lowerASCII = ord(lower)

    # Next character
    nextASCII = lowerASCII + 1

    # Wrap alphabet around
    if nextASCII == 123:
        nextASCII = 97

    # Convert to character
    next = chr(nextASCII)

    # Return result
    return next


#
# Main Program
#

# Declare global variables
firstNames = [""] * 25
lastNames = [""] * 25
ages = [0] * 25
usernames = [""] * 25
oldest = 0

# Get pupils' data
firstNames, lastNames, ages = getData()

# Generate network usernames
usernames = makeUsernames(firstNames, lastNames, ages)

# Find age of oldest pupil
oldest = findOldest(ages)

# Display summary data
summary(firstNames, lastNames, ages, oldest)

# Write data to file
writeData(usernames, firstNames, lastNames)
