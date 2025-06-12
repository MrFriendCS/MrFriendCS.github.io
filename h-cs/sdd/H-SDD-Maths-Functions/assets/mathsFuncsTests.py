# Title: Testing Functions in mathsFunc.py
# Author: Mr Friend
# Date: 11 Jun 2025

# Get functions to be tested
from mathsFuncs import *

#
# Sub-programs
#

def testAdd():
    """Test the funcationality of the add function."""
    
    # Initialise variable
    failCount = 0
    
    # Display message
    print("\nTesting: add function")

    # Test 1
    try:
        
        assert add(2, 3) == 5
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 2 + 3 = 5")
    
    # Test 2
    try:
        
        assert add(-2, -3) == -5
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: -2 + (-3) = -5")

    # Display final message
    if failCount == 0:
        
        print("\tAll tests passed.")


def testMultiply():
    """Test the funcationality of the multiply function."""
    
    # Initialise variable
    failCount = 0
    
    # Display message
    print("\nTesting: multiply function")

    # Test 1
    try:
        
        assert multiply(2, 3) == 6
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 2 * 3 = 6")
    
    # Test 2
    try:
        
        assert multiply(-2, -3) == 6
        
    except:
        
        failCount = failCount + 1
    
    # Test 3
    try:
        
        assert multiply(-2, 3) == -6
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: -2 + (-3) = -5")

    # Display final message
    if failCount == 0:
        
        print("\tAll tests passed.")


def testSubtract():
    """Test the funcationality of the subtract function."""
    
    # Initialise variable
    failCount = 0
    
    # Display message
    print("\nTesting: subtract function")

    try:
        
        assert subtract(5, 2) == 3
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 5 - 2 = 3")

    # Display final message
    if failCount == 0:
        
        print("\tAll tests passed.")
        

def testDivide():
    """Test the funcationality of the divide function."""
    
    # Initialise variable
    failCount = 0
    
    # Display message
    print("\nTesting: divide function")

    try:
        
        assert divide(6, 3) == 2.0
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 6 / 3 = 2.0")

    # Display final message
    if failCount == 0:
        
        print("\tAll tests passed.")


#
# Main program
#

# Run tests
testAdd()
testMultiply()
testSubtract()
testDivide()
