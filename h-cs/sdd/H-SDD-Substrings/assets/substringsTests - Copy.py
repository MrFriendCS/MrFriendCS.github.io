# Title: H-SDD-Substrings-Tests
# Author: Mr Friend
# Date:  16 Jun 2025

"""Tests the functions in substring.py"""

from substrings import *


def testLeft():
    """Test the funcationality of the left() function."""
    
    # Initialise variables
    failCount = 0
    inputs = ["Hello", "12345", "£1.26p", "Hello", "Hello", "Hello"]
    chars = [4, 3, 5, 0, -1, 6]
    outputs = ["Hell", "123", "£1.26", "Hello", "Hello", "Hello"]
    
    # Display message
    print("\nTesting: left() function")
    
    # Tests
    for index in range(len(inputs)):
    
        try:
            
            assert left(inputs[index], chars[index]) == outputs[index]
            
        except:
            
            failCount = failCount + 1
            
            print("\tFailed: \"" + inputs[index] + "\", "
                  + str(chars[index]) + " = \"" + outputs[index] + "\"")
    
    # Display final message
    if failCount == 0:
        
        print("\tAll tests passed.")


def testRight():
    """Test the funcationality of the right() function."""
       
    # Initialise variables
    failCount = 0
    inputs = ["Hello", "12345", "£1.26p", "Hello", "Hello", "Hello"]
    chars = [4, 3, 5, 0, -1, 6]
    outputs = ["ello", "345", "1.26p", "Hello", "Hello", "Hello"]
    
    # Display message
    print("\nTesting: right() function")
    
    # Tests
    for index in range(len(inputs)):
    
        try:
            
            assert right(inputs[index], chars[index]) == outputs[index]
            
        except:
            
            failCount = failCount + 1
            
            print("\tFailed: \"" + inputs[index] + "\", "
                  + str(chars[index]) + " = \"" + outputs[index] + "\"")
      
    # Display final message
    if failCount == 0:
        
        print("\tAll tests passed.")


def testMid():
    """Test the funcationality of the mid() function."""
    
    # Initialise variables"Hello!", 2, 3) == "ell"
    failCount = 0
    inputs = ["Hello", "12345", "£1.26p", "Hello", "Hello", "Hello"]
    starts = [2, 3, 2, 4, -1, 3]
    chars = [3, 2, 3, 0, 3, 5]
    outputs = ["ell", "34", "1.2", "Hello", "Hello", "Hello"]
    
    # Display message
    print("\nTesting: mid() function")
    
    # Tests
    for index in range(len(inputs)):
    
        try:
            
            assert mid(inputs[index], starts[index], chars[index]) == outputs[index]
            
        except:
            
            failCount = failCount + 1
            
            print("\tFailed: \"" + inputs[index] + "\", "
                  + str(starts[index]) + ", " + str(chars[index])
                  + " = \"" + outputs[index] + "\"")
    
    # Display final message
    if failCount == 0:
        
        print("\tAll tests passed.")
    

#
# Main program
#

testLeft()
testRight()
testMid()
        
