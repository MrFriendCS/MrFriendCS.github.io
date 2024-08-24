# Title: H SDD Substrings
# Author: Mr Friend
# Date: 22 Aug 2023

#
# Subprograms
#
def left(text, number):
    # Extract substring
    subString = text[ :number]

    # Return substring
    return subString


def right(text, number):
    # Extract substring
    subString = text[-number: ]

    # Return substring
    return subString


def mid(text, start, number):
    # Extract substring
    subString = text[start-1:start+number-1]

    # Return substring
    return subString


#
# Main Program
#

# Declare global variable
text = ""
subString = ""
leftCount = 0
rightCount = 0
midStart = 0
midCount = 0

# Get word or phrase
text = input("Enter a word or phrase: ")

# Get values
leftCount = int(input("\nLeft characters: "))
rightCount = int(input("Right characters: "))
midStart = int(input("Mid start character: "))
midCount = int(input("Mid count characters: "))

# Left substring
subString = left(text, leftCount)
print("\nLeft: " + subString)

# Right substring
subString = right(text, rightCount)
print("Right: " + subString)

# Mid substring
subString = mid(text, midStart, midCount)
print("Mid: " + subString)
