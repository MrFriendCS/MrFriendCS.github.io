# Title: Caesar Cipher Tests
# Author: Mr Friend
# Date: 17 Jun 2025

"""Tests the functions in caesar.py"""

from caesar import *

def testEncode():
    """Test the functionality of the encode() function."""
    
    # Initialise local variables
    failCount = 0
    inputs = ["abcd", "wxyz", "abcd", "wxyz", "!a b-c,", "ABCD",
              "WXYZ", "ABCD", "WXYZ", "!A B-C,", "abcd", "ABCD"]
    shifts = [1, 1, 25, 25, 3, 1,
              1, 25, 25, 3, 55, 55]
    outputs = ["bcde", "xyza", "zabc", "vwxy", "def", "bcde",
               "xyza", "zabc", "vwxy", "def", "defg", "defg"]
    
    # Display function being tested
    print("\nTesting: encode() function")
    
    # Loop through tests
    for index in range(len(inputs)):
    
        try:
            
            assert encode(inputs[index], shifts[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " + str(index+1) + ": encode(\""
                  + inputs[index] + "\", " + str(shifts[index])
                  + ") = '" + outputs[index] + "'")
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs)) + " tests passed.")


def testDecode():
    """Test the functionality of the decode() function."""
    
    # Initialise local variables
    failCount = 0
    inputs = ["bcde", "xyza", "zabc", "vwxy", "!D E-F,", "BCDE",
              "XYZA", "ZABC", "VWXY", "!D E-F,", "defg", "DEFG", "def DEF"]
    shifts = [1, 1, 25, 25, 3, 1,
              1, 25, 25, 3, 55, 55, 3]
    outputs = ["abcd", "wxyz", "abcd", "wxyz", "!A B-C,", "ABCD",
               "WXYZ", "ABCD", "WXYZ", "!A B-C,", "abcd", "ABCD", "abc ABC"]
    
    # Display function being tested
    print("\nTesting: decode() function")
    
    # Loop through tests
    for index in range(len(inputs)):
    
        try:
            
            assert decode(inputs[index], shifts[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " + str(index+1) + ": decode(\""
                  + inputs[index] + "\", " + str(shifts[index])
                  + ") = '" + outputs[index] + "'")
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs)) + " tests passed.")


#
# Main program
#

# Initialise global variables
test = ""
run = True

while run:
    print("\nCaesar Cipher Tests")
    print("-------------------")

    print("\n1  Encode tests")
    print("2  Decode tests")
    print("x  Exit")

    # Get text value from user
    test = input("\nTest: ")

    if test == "1":
        # Encode test
        testEncode()
    elif test == "2":
        # Decode test
        testDecode()
    elif test == "x":
        # Exit tests
        run = False
