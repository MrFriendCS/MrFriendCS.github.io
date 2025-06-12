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




#
# Main program
#

# Run tests
testSecToMinSec()

