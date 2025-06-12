# Title: Testing Functions in conversionFuncs.py
# Author: Mr Friend
# Date: 12 Jun 2025

# Get functions to be tested
from conversionFuncs import *

#
# Sub-programs
#

def testSecToMinSec():
    """Test the funcationality of the secToMinSec function."""
    
    # Initialise variable
    failCount = 0
    
    # Display message
    print("\nTesting: secToMinSec function")

    # Test 1
    try:
        
        assert secToMinSec(81) == (1, 21)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 81 = (1, 21)")
    
    # Test 2
    try:
        
        assert secToMinSec(81.9) == (1, 21)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 81.9 = (1, 21)")
        
    # Test 3
    try:
        
        assert secToMinSec(0) == (0, 0)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 0 = (0, 0)")
        
    # Test 4
    try:
        
        assert secToMinSec(-1) == (-1, -1)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: -1 = (-1, -1)")

    # Display final message
    if failCount == 0:
        
        print("\tAll tests passed.")
        

def testMinToHourMin():
    """Test the funcationality of the minToHourMin function."""
    
    # Initialise variable
    failCount = 0
    
    # Display message
    print("\nTesting: minToHourMin function")

    # Test 1
    try:
        
        assert minToHourMin(81) == (1, 21)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 81 = (1, 21)")
    
    # Test 2
    try:
        
        assert minToHourMin(81.9) == (1, 21)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 81.9 = (1, 21)")
        
    # Test 3
    try:
        
        assert minToHourMin(0) == (0, 0)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 0 = (0, 0)")
        
    # Test 4
    try:
        
        assert minToHourMin(-1) == (-1, -1)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: -1 = (-1, -1)")

    # Display final message
    if failCount == 0:
        
        print("\tAll tests passed.")


def testHourToDayHour():
    """Test the funcationality of the hourToDayHour function."""
    
    # Initialise variable
    failCount = 0
    
    # Display message
    print("\nTesting: hourToDayHour function")

    # Test 1
    try:
        
        assert hourToDayHour(81) == (3, 9)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 81 = (3, 9)")
    
    # Test 2
    try:
        
        assert hourToDayHour(81.9) == (3, 9)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 81.9 = (1, 21)")
        
    # Test 3
    try:
        
        assert hourToDayHour(0) == (0, 0)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 0 = (0, 0)")
        
    # Test 4
    try:
        
        assert hourToDayHour(-1) == (-1, -1)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: -1 = (-1, -1)")

    # Display final message
    if failCount == 0:
        
        print("\tAll tests passed.")


def testMMtoCMmm():
    """Test the funcationality of the mmToCMmm function."""
    
    # Initialise variable
    failCount = 0
    
    # Display message
    print("\nTesting: mmToCMmm function")

    # Test 1
    try:
        
        assert mmToCMmm(81) == (8, 1)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 81 = (8, 1)")
    
    # Test 2
    try:
        
        assert mmToCMmm(81.9) == (8, 1)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 81.9 = (1, 21)")
        
    # Test 3
    try:
        
        assert mmToCMmm(0) == (0, 0)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 0 = (0, 0)")
        
    # Test 4
    try:
        
        assert mmToCMmm(-1) == (-1, -1)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: -1 = (-1, -1)")

    # Display final message
    if failCount == 0:
        
        print("\tAll tests passed.")


def testCMtoMcm():
    """Test the funcationality of the cmToMcm function."""
    
    # Initialise variable
    failCount = 0
    
    # Display message
    print("\nTesting: cmToMcm function")

    # Test 1
    try:
        
        assert cmToMcm(81) == (0, 81)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 81 = (0, 81)")
    
    # Test 2
    try:
        
        assert cmToMcm(81.9) == (0, 81)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 81.9 = (0, 81)")
        
    # Test 3
    try:
        
        assert cmToMcm(0) == (0, 0)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 0 = (0, 0)")
        
    # Test 4
    try:
        
        assert cmToMcm(-1) == (-1, -1)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: -1 = (-1, -1)")

    # Display final message
    if failCount == 0:
        
        print("\tAll tests passed.")
        

def testMtoKMm():
    """Test the funcationality of the mToKMm function."""
    
    # Initialise variable
    failCount = 0
    
    # Display message
    print("\nTesting: mToKMm function")

    # Test 1
    try:
        
        assert mToKMm(81) == (0, 81)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 81 = (0, 81)")
    
    # Test 2
    try:
        
        assert mToKMm(81.9) == (0, 81)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 81.9 = (0, 81)")
        
    # Test 3
    try:
        
        assert mToKMm(0) == (0, 0)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 0 = (0, 0)")
        
    # Test 4
    try:
        
        assert mToKMm(-1) == (-1, -1)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: -1 = (-1, -1)")

    # Display final message
    if failCount == 0:
        
        print("\tAll tests passed.")
        

def testInchesToFeetInches():
    """Test the funcationality of the inchesToFeetInches function."""
    
    # Initialise variable
    failCount = 0
    
    # Display message
    print("\nTesting: inchesToFeetInches function")

    # Test 1
    try:
        
        assert inchesToFeetInches(81) == (6, 9)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 81 = (6, 9)")
    
    # Test 2
    try:
        
        assert inchesToFeetInches(81.9) == (6, 9)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 81.9 = (0, 81)")
        
    # Test 3
    try:
        
        assert inchesToFeetInches(0) == (0, 0)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 0 = (0, 0)")
        
    # Test 4
    try:
        
        assert inchesToFeetInches(-1) == (-1, -1)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: -1 = (-1, -1)")

    # Display final message
    if failCount == 0:
        
        print("\tAll tests passed.")


def testFeetToYardsFeet():
    """Test the funcationality of the feetToYardsFeet function."""
    
    # Initialise variable
    failCount = 0
    
    # Display message
    print("\nTesting: feetToYardsFeet function")

    # Test 1
    try:
        
        assert feetToYardsFeet(81) == (27, 0)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 81 = (27, 0)")
    
    # Test 2
    try:
        
        assert feetToYardsFeet(81.9) == (27, 0)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 81.9 = (0, 81)")
        
    # Test 3
    try:
        
        assert feetToYardsFeet(0) == (0, 0)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: 0 = (0, 0)")
        
    # Test 4
    try:
        
        assert feetToYardsFeet(-1) == (-1, -1)
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: -1 = (-1, -1)")

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