# Title: Calculate ISBN-13 Check Digit
# Author: Mr Friend
# Date: 24 Sep 2022

# Define function
def check(isbn):
    '''Returns the check digit, as a character, of an ISBN-13, using first 12 values'''

    # Declare local variables and array
    checkDigit = 0
    value = 0
    sum = 0
    multiplier = "131313131313"

    # Calculate sum of values
    for index in range(12):
        value = int(isbn[index]) * int(multiplier[index])
        sum = sum + value
        
    # Calculate check digit
    checkDigit = sum % 10

    if checkDigit > 0:
        checkDigit = 10 - checkDigit    

    return str(checkDigit) 
        
# Declare Global variable and array
checkDigit = ""
isbns = [""] * 1000

# Read values from file
file = open("Part ISBNs.csv", "r")
for index in range (len(isbns)):
    isbns[index] = file.readline().strip()

file.close()

# Get check digits for all values
for index in range (len(isbns)):
    # Get check digit
    checkDigit = check(isbns[index])

    # Add check didgit to ISBN
    isbns[index] = isbns[index] + checkDigit

# Write values to file
file = open("ISBNs.csv", "w")

for index in range (len(isbns)):
    file.write(isbns[index] + "\n")

file.close()
