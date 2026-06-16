# Title: Testing Functions in standard.py
# Author: Mr Friend
# Date: 16 Jun 2026

# Get functions to be tested
from standard import *

#
# Sub-programs
#

def testSearchString() -> None:
    """Test the functionality of the searchString() function."""
    
    # Initialise local variables
    failCount = 0
    errorText = ""
    
    values1 = ["A", "B", "C", "D", "E", "F", "G"]
    values2 = ["Campbell", "Ford", "MacDonald", "Smyth", "Young"]
    
    inputs1 = [values1, values1, values2, values2]
    inputs2 = ["A", "G", "Ford", "Robertson"]
    outputs = [True, True, True, False]
    
    # Display function being tested
    print("\nTesting: searchString() function")

    # Loop through tests
    for index in range(len(inputs1)):
        
        try:
            
            assert searchString(inputs1[index], inputs2[index]) \
                   == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Error text dependent on type
            if isinstance(inputs2[index], str):
                
                # String
                errorText = ", \"" + str(inputs2[index]) + "\") = "
            
            else:
                
                # Non-string
                errorText = ", " + str(inputs2[index]) + ") = "
            
            # Display failure message
            print("\tFailed Test " + str(index+1)
                  + ": searchString(" + str(inputs1[index])
                  + errorText + str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs1)) + " tests passed.")


def testFindMinReal() -> None:
    """Test the functionality of the findMinReal() function."""
    
    # Initialise local variables
    failCount = 0
    
    values1 = [6.8, 67.4, 83.2, 55.4, 46.8, 60.5]
    values2 = [6.8, 67.4, 83.2, 55.4, 46.8, 6.5]
    values3 = [6.8, 67.4, 3.2, 55.4, 46.8, 6.5]
    
    inputs = [values1, values2, values3]
    outputs = [6.8, 6.5, 3.2]
    
    # Display function being tested
    print("\nTesting: findMinReal() function")

    # Loop through tests
    for index in range(len(inputs)):
        
        try:
            
            assert findMinReal(inputs[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Error text dependent on type
            if isinstance(outputs[index], str):
                
                # String
                errorText = ") = \'" + str(outputs[index]) + "\'"
            
            else:
                
                # Non-string
                errorText = ") = " + str(outputs[index])
            
            # Display failure message
            print("\tFailed Test " + str(index+1)
                  + ": findMinReal(" + str(inputs[index])
                  + errorText)
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs)) + " tests passed.")


def testFindMaxInt() -> None:
    """Test the functionality of the findMaxInt() function."""
    
    # Initialise local variables
    failCount = 0
    
    values1 = [17, 14, 16, 17, 13, 14, 12]
    values2 = [17, 14, 16, 17, 13, 14, 22]
    values3 = [17, 14, 16, 77, 13, 14, 22]
    
    inputs = [values1, values2, values3]
    outputs = [17, 22, 77]
    
    # Display function being tested
    print("\nTesting: findMaxInt() function")

    # Loop through tests
    for index in range(len(inputs)):
        
        try:
            
            assert findMaxInt(inputs[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Error text dependent on type
            if isinstance(outputs[index], str):
                
                # String
                errorText = ") = \'" + str(outputs[index]) + "\'"
            
            else:
                
                # Non-string
                errorText = ") = " + str(outputs[index])
            
            # Display failure message
            print("\tFailed Test " + str(index+1)
                  + ": findMaxInt(" + str(inputs[index])
                  + errorText)
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs)) + " tests passed.")


def testCountString() -> None:
    """Test the functionality of the countString() function."""
    
    # Initialise local variables
    failCount = 0
    
    values1 = ["A", "B", "C", "A", "D", "E", "A"]
    values2 = ["Campbell", "Ford", "MacDonald", "Smyth", "Young"]
    
    inputs1 = [values1, values1, values2]
    inputs2 = ["A", "B", "Robertson"]
    outputs = [3, 1, 0]
    
    # Display function being tested
    print("\nTesting: countString() function")

    # Loop through tests
    for index in range(len(inputs1)):
        
        try:
            
            assert countString(inputs1[index], inputs2[index]) \
                   == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Error text dependent on type
            if isinstance(inputs2[index], str):
                
                # String
                errorText = ", \"" + str(inputs2[index]) + "\") = "
            
            else:
                
                # Non-string
                errorText = ", " + str(inputs2[index]) + ") = "
            
            # Display failure message
            print("\tFailed Test " + str(index+1)
                  + ": countString(" + str(inputs1[index])
                  + errorText + str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs1)) + " tests passed.")


#
# Main program
#

# Tests
testSearchString()
testFindMinReal()
testFindMaxInt()
testCountString()
