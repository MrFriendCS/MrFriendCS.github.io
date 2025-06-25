# Title: Testing Functions in summmer3.py
# Author: Mr Friend
# Date: 25 Jun 2025

# Get functions to be tested
from summer3 import *

#
# Sub-programs
#

def testContains():
    """Test the functionality of the contains() function."""
    
    # Initialise variable
    failCount = 0
    inputs1 = ["hello", "HELLO", "hello", "HELLO",
               "hello", "HELLO", "hello", "HELLO",
               "h3!!0", "H3!!0", "h3!!0", "H3!!0"]
    inputs2 = ["h", "e", "L", "L",
               "a", "b", "A", "B",
               "3", "!", "0", "9"]
    outputs = [True, True, True, True,
               False, False, False, False,
               True, True, True, False]
    
    # Display function being tested
    print("\nTesting: contains() function")

    # Loop through tests
    for index in range(len(inputs1)):
        
        try:
            
            assert contains(inputs1[index], inputs2[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " + str(index+1) + ": contains(\""
                  + str(inputs1[index]) + "\", \"" + inputs2[index] + "\") = "
                  + str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs1)) + " tests passed.")
        

def testLetterTypes():
    """Test the functionality of the letterTypes() function."""
    
    # Initialise variable
    failCount = 0
    inputs = ["Hello", "HELLO", "hello", "HeLlO!",
              "", "A 1 * z", "\,./", "1 z A *"]
    outputs = [(1, 4), (5,0), (0,5), (3, 2),
               (0, 0), (1, 1), (0, 0), (1, 1)]
    
    # Display function being tested
    print("\nTesting: letterTypes() function")

    # Loop through tests
    for index in range(len(inputs)):
        
        try:
            
            assert letterTypes(inputs[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " + str(index+1) + ": letterTypes(\""
                  + str(inputs[index]) + "\") = " + str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs)) + " tests passed.")


#
# Main program
#

# Tests
testContains()
testLetterTypes()

