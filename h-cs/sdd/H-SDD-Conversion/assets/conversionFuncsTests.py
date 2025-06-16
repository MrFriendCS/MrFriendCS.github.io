# Title: Testing Functions in conversionFuncs.py
# Author: Mr Friend
# Date: 16 Jun 2025

# Get functions to be tested
from conversionFuncs import *

#
# Sub-programs
#

def testSecToMinSec():
    """Test the funcationality of the secToMinSec() function."""
    
    # Initialise variable
    failCount = 0
    inputs = [81, 81.9, 0, -1]
    outputs = [(1, 21), (1, 21), (0, 0), (-1, -1)]
    
    # Display message
    print("\nTesting: secToMinSec() function")

    # Test 1
    for index in range(len(inputs)):
        
        try:
            
            assert secToMinSec(inputs[index]) == outputs[index]
            
        except:
            
            failCount = failCount + 1
            
            print("\tFailed: " + str(inputs[index]) + " = "
                  + str(outputs[index]))
    
    # Display final message
    if failCount == 0:
        
        print("\tAll tests passed.")
        

def testMinToHourMin():
    """Test the funcationality of the minToHourMin() function."""
    
    # Initialise variable
    failCount = 0
    inputs = [81, 81.9, 0, -1]
    outputs = [(1, 21), (1, 21), (0, 0), (-1, -1)]
    
    # Display message
    print("\nTesting: minToHourMin() function")

    # Tests
    
    for index in range(len(inputs)):
        
        try:
            
            assert minToHourMin(inputs[index]) == outputs[index]
            
        except:
            
            failCount = failCount + 1
            
            print("\tFailed: " + str(inputs[index]) + " = "
                  + str(outputs[index]))

    # Display final message
    if failCount == 0:
        
        print("\tAll tests passed.")


def testHourToDayHour():
    """Test the funcationality of the hourToDayHour() function."""
    
    # Initialise variable
    failCount = 0
    inputs = [81, 81.9, 0, -1]
    outputs = [(3, 9), (3, 9), (0, 0), (-1, -1)]
    
    # Display message
    print("\nTesting: hourToDayHour() function")

    # Tests
    for index in range(len(inputs)):
        
        try:
            
            assert hourToDayHour(inputs[index]) == outputs[index]
            
        except:
            
            failCount = failCount + 1
            
            print("\tFailed: " + str(inputs[index]) + " = "
                  + str(outputs[index]))

    # Display final message
    if failCount == 0:
        
        print("\tAll tests passed.")


def testMMtoCMmm():
    """Test the funcationality of the mmToCMmm() function."""
    
    # Initialise variable
    failCount = 0
    inputs = [81, 81.9, 0, -1]
    outputs = [(8, 1), (8, 1), (0, 0), (-1, -1)]
    
    # Display message
    print("\nTesting: mmToCMmm() function")

    # Tests
    for index in range(len(inputs)):
        
        try:
            
            assert mmToCMmm(inputs[index]) == outputs[index]
            
        except:
            
            failCount = failCount + 1
            
            print("\tFailed: " + str(inputs[index]) + " = "
                  + str(outputs[index]))

    # Display final message
    if failCount == 0:
        
        print("\tAll tests passed.")


def testCMtoMcm():
    """Test the funcationality of the cmToMcm() function."""
    
    # Initialise variable
    failCount = 0
    inputs = [81, 181.9, 0, -1]
    outputs = [(0, 81), (1, 81), (0, 0), (-1, -1)]
    
    # Display message
    print("\nTesting: cmToMcm() function")

    # Tests
    for index in range(len(inputs)):
        
        try:
            
            assert cmToMcm(inputs[index]) == outputs[index]
            
        except:
            
            failCount = failCount + 1
            
            print("\tFailed: " + str(inputs[index]) + " = "
                  + str(outputs[index]))
        
    # Display final message
    if failCount == 0:
        
        print("\tAll tests passed.")
        

def testMtoKMm():
    """Test the funcationality of the mToKMm() function."""
    
    # Initialise variable
    failCount = 0
    inputs = [81, 1081.9, 0, -1]
    outputs = [(0, 81), (1, 81), (0, 0), (-1, -1)]
    
    # Display message
    print("\nTesting: mToKMm() function")

    # Tests
    for index in range(len(inputs)):
        
        try:
            
            assert mToKMm(inputs[index]) == outputs[index]
            
        except:
            
            failCount = failCount + 1
            
            print("\tFailed: " + str(inputs[index]) + " = "
                  + str(outputs[index]))

    # Display final message
    if failCount == 0:
        
        print("\tAll tests passed.")
        

def testInchesToFeetInches():
    """Test the funcationality of the inchesToFeetInches() function."""
    
    # Initialise variable
    failCount = 0
    inputs = [81, 81.9, 0, -1]
    outputs = [(6, 9), (6, 9), (0, 0), (-1, -1)]
    
    # Display message
    print("\nTesting: inchesToFeetInches() function")

    # Tests
    for index in range(len(inputs)):
        
        try:
            
            assert inchesToFeetInches(inputs[index]) == outputs[index]
            
        except:
            
            failCount = failCount + 1
            
            print("\tFailed: " + str(inputs[index]) + " = "
                  + str(outputs[index]))

    # Display final message
    if failCount == 0:
        
        print("\tAll tests passed.")


def testFeetToYardsFeet():
    """Test the funcationality of the feetToYardsFeet() function."""
    
    # Initialise variable
    failCount = 0
    inputs = [82, 82.9, 0, -1]
    outputs = [(27, 1), (27, 1), (0, 0), (-1, -1)]
    
    # Display message
    print("\nTesting: feetToYardsFeet() function")

    # Tests
    for index in range(len(inputs)):
        
        try:
            
            assert feetToYardsFeet(inputs[index]) == outputs[index]
            
        except:
            
            failCount = failCount + 1
            
            print("\tFailed: " + str(inputs[index]) + " = "
                  + str(outputs[index]))

    # Display final message
    if failCount == 0:
        
        print("\tAll tests passed.")


#
# Main program
#

# Run tests
testSecToMinSec()
testMinToHourMin()
testHourToDayHour()
testMMtoCMmm()
testCMtoMcm()
testMtoKMm()
testInchesToFeetInches()
testFeetToYardsFeet()
