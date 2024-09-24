# Title: Password Generator
# Author: Mr Friend
# Date: 11 Oct 2022

# Import module
import random

#
# Functions and procedures
#

def generatePassword():
    '''Generate and return a password'''
    # Local variables
    length = 0
    rndNumber = 0
    localPassword = ""
    character = ""

    # 1.1 Pick random number of characters (8 to 12)
    length = random.randint(8, 12)

    # 1.2 Loop for each character
    for counter in range(length):

        # 1.2.1 Generate a random number
        rndNumber = random.randint(0, 9)

        # 1.2.2 If value is

        # 1.2.2.1 0, special character
        if rndNumber == 0:
            character = getChr(33, 42)

        # 1.2.2.2 1, digit
        elif rndNumber == 1:
            character = getChr(48, 57)

        # 1.2.2.3 2-5, upper
        elif rndNumber <= 5:
            character = getChr(65, 90)

        # 1.2.2.4 6-9, lower
        else:
            character = getChr(97, 122)

        # 1.2.3 Add character to password
        localPassword = localPassword + character

    # 1.3 Return password
    return localPassword

def getChr(lower, upper):
    '''Pick and return a character between the lower and upper values, at random'''
    # Local varaiable
    letter = ""
    value = 0

    # Pick character
    value = random.randint(lower, upper)
    letter = chr(value)

    # Return character
    return letter

def validatePassword(localPassword):
    '''Checks a password to see if it matches the requirements.  Returns Boolean.'''

    # Local variables
    localValid = False
    lengthV = False
    specialV = False
    digitV = False
    upperV = False
    lowerV = False
    value = 0

    # Loop for each character
    for index in range(len(localPassword)):

        # Get ASCII value of current character
        value = ord(localPassword[index])

        # Contains special character?
        if value >= 33 and value <= 42:
            specialV = True

        # Contains a digit?
        elif value >= 48 and value <= 57:
            digitV = True

        # Contains an uppercase letter?
        elif value >= 65 and value <= 90:
            upperV = True

        # Contains a lowercase letter?
        elif value >= 97 and value <= 122:
            lowerV = True

    # Password long enough?
    if len(localPassword) >= 8 and len(localPassword) <= 12:
        lengthV = True

    # Is everything valid?
    if lengthV and specialV and digitV and upperV and lowerV:
        localValid = True

    # Return result
    return localValid

def displayResult(localPassword, localValid):
    '''Display password and its status'''

    # Declare local variable
    status = ""

    # Decide the status
    if localValid:
        status = "valid"
    else:
        status = "invalid"

    # Display the result
    print("The password " + localPassword + " is " + status + ".")
    
#
# Main program
#

# Global variables
passowrd = ""
valid = False

# Generate password
password = generatePassword()

# Vaildate password
valid = validatePassword(password)

# Display result
displayResult(password, valid)
