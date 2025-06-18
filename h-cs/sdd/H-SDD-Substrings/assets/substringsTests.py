# Title: H-SDD-Substrings-Tests
# Author: Mr Friend
# Date:  16 Jun 2025

"""Tests the functions in substring.py"""

from substrings import *


def testLeft():
    """Test the funcationality of the left() function."""
    
    # Initialise local variables
    failCount = 0
    inputs = ["Hello", "12345", "£1.26p", "Hello", "Hello", "Hello"]
    chars = [4, 3, 5, 0, -1, 6]
    outputs = ["Hell", "123", "£1.26", "Hello", "Hello", "Hello"]
    
    # Display function being tested
    print("\nTesting: left() function")
    
    # Loop through tests
    for index in range(len(inputs)):
    
        try:
            
            assert left(inputs[index], chars[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " + str(index+1) + ": left(\""
                  + inputs[index] + "\", " + str(chars[index])
                  + ") = '" + outputs[index] + "'")
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs)) + " tests passed.")


def testRight():
    """Test the funcationality of the right() function."""
       
    # Initialise local variables
    failCount = 0
    inputs = ["Hello", "12345", "£1.26p", "Hello", "Hello", "Hello"]
    chars = [4, 3, 5, 0, -1, 6]
    outputs = ["ello", "345", "1.26p", "Hello", "Hello", "Hello"]
    
    # Display function being tested
    print("\nTesting: right() function")
    
    # Loop through tests
    for index in range(len(inputs)):
    
        try:
            
            assert right(inputs[index], chars[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed: \"" + inputs[index] + "\", "
                  + str(chars[index]) + " = \"" + outputs[index] + "\"")
      
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs)) + " tests passed.")


def testMid():
    """Test the funcationality of the mid() function."""
    
    # Initialise local variables"Hello!", 2, 3) == "ell"
    failCount = 0
    inputs = ["Hello", "12345", "£1.26p", "Hello", "Hello", "Hello"]
    starts = [2, 3, 2, 4, -1, 3]
    chars = [3, 2, 3, 0, 3, 5]
    outputs = ["ell", "34", "1.2", "Hello", "Hello", "Hello"]
    
    # Display function being tested
    print("\nTesting: mid() function")
    
    # Loop through tests
    for index in range(len(inputs)):
    
        try:
            
            assert mid(inputs[index], starts[index], chars[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed: \"" + inputs[index] + "\", "
                  + str(starts[index]) + ", " + str(chars[index])
                  + " = \"" + outputs[index] + "\"")
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs)) + " tests passed.")
    

#
# Main program
#

testLeft()
testRight()
testMid()
