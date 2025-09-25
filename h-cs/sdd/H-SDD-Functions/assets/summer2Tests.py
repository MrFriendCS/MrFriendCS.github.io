# Title: Testing Functions in summmer2.py
# Author: Mr Friend
# Date: 25 Jun 2025

# Get functions to be tested
from summer2 import *

#
# Sub-programs
#

def testReverse():
    """Test the functionality of the reverse() function."""
    
    # Initialise variable
    failCount = 0
    inputs = ["ABCD", "abcd", "WXYZ", "wxyz",
              "1234", "6789", "\,./", "A b 1 !"]
    outputs = ["DCBA", "dcba", "ZYXW", "zyxw",
               "4321", "9876", "/.,\\", "! 1 b A"]
    
    # Display function being tested
    print("\nTesting: reverse() function")

    # Loop through tests
    for index in range(len(inputs)):
        
        try:
            
            assert reverse(inputs[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " + str(index+1) + ": reverse(\""
                  + str(inputs[index]) + "\") = \'"
                  + str(outputs[index]) + "\'")
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs)) + " tests passed.")


def testMakeUsername():
    """Test the functionality of the makeUsername() function."""
    
    # Initialise variable
    failCount = 0
    
    inputs = ["ABCDE", "abcde", "AbCdE", "aBcDe",
              "ABCD", "abcd", "AbCd", "aBcD",
              "ABC", "abc", "AbC", "aBc",
              "AB", "ab", "Ab", "aB"]
    
    outputs = ["esabcd??", "esabcd??", "esabcd??", "esabcd??",
               "esabcd??", "esabcd??", "esabcd??", "esabcd??",
               "esabc??", "esabc??", "esabc??", "esabc??",
               "invalid", "invalid", "invalid", "invalid"]
    
    returnValue = ""
    number = False
    letter = False
    
    # Display function being tested
    print("\nTesting: makeUsername() function")

    # Loop through tests
    for index in range(len(inputs)):
        
        # Reset flags
        number = False
        letter = False
        
        try:
            
            returnValue = makeUsername(inputs[index])
            
            if len(inputs[index]) < 3:
                
                assert returnValue == outputs[index]
                
            else:
                
                number = int(returnValue[-2]) >= 1 and int(returnValue[-2]) <= 9
                letter = ord(returnValue[-1]) >= 97 and ord(returnValue[-1]) <= 122
                
                if len(inputs[index]) == 3:
                
                    assert returnValue[ :5] == outputs[index][ :5] and number and letter
                
                else:
                    
                    assert returnValue[ :6] == outputs[index][ :6] and number and letter
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " + str(index+1) + ": makeUsername(\""
                  + str(inputs[index]) + "\") = \'"
                  + str(outputs[index]) + "\'")
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs)) + " tests passed.")


#
# Main program
#

# Tests
testReverse()
testMakeUsername()

