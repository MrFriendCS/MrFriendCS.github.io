# Title: H-SDD-Substrings-Tests
# Author: Mr Friend
# Date:  12 Jun 2025

"""Tests the functions in substring.py"""

from substrings import *


def testLeft():
    """Test the funcationality of the left() function."""
    
    # Initialise variable
    failCount = 0
    
    # Display message
    print("\nTesting: left() function")
    
    # Test 1
    try:
        
        assert left("Hello!", 4) == "Hell"
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: \"Hello\", 4 = \"Hell\"")
    
    # Test 2
    try:
        
        assert left("12345", 3) == "123"
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: \"12345\", 3 = \"123\"")

    # Test 3
    try:
        
        assert left("£1.26p", 5) == "£1.26"
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: \"£1.26p\", 5) == \"£1.26\"")

    # Test 4
    try:
        
        assert left("Hello!", 0) == "Hello!"
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: \"Hello!\", 0) == \"Hello!\"")

    # Test 5
    try:
        
        assert left("Hello!", -1) == "Hello!"
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: \"Hello!\", 0) == \"Hello!\"")

    # Test 6
    try:
        
        assert left("Hello!", 7) == "Hello!"
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: \"Hello!\", 7) == \"Hello!\"")
    
    # Display final message
    if failCount == 0:
        
        print("\tAll tests passed.")


def testRight():
    """Test the funcationality of the right() function."""
    
    # Initialise variable
    failCount = 0
    
    # Display message
    print("\nTesting: right() function")
    
    # Test 1
    try:
        
        assert right("Hello!", 4) == "llo!"
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: \"Hello!\", 4 = \"llo!\"")
    
    # Test 2
    try:
        
        assert right("12345", 3) == "345"
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: \"12345\", 3 = \"345\"")

    # Test 3
    try:
        
        assert right("£1.26p", 5) == "1.26p"
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: \"£1.26p\", 5) == \"1.26p\"")

    # Test 4
    try:
        
        assert right("Hello!", 0) == "Hello!"
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: \"Hello!\", 0) == \"Hello!\"")

    # Test 5
    try:
        
        assert right("Hello!", -1) == "Hello!"
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: \"Hello!\", 0) == \"Hello!\"")

    # Test 6
    try:
        
        assert right("Hello!", 7) == "Hello!"
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: \"Hello!\", 7) == \"Hello!\"")
    
    # Display final message
    if failCount == 0:
        
        print("\tAll tests passed.")


def testMid():
    """Test the funcationality of the mid() function."""
    
    # Initialise variable
    failCount = 0
    
    # Display message
    print("\nTesting: mid() function")
    
    # Test 1
    try:
        
        assert mid("Hello!", 2, 3) == "ell"
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: \"Hello\", 2, 3 = \"ello\"")
    
    # Test 2
    try:
        
        assert mid("12345", 3, 2) == "34"
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: \"12345\", 3, 2 = \"34\"")

    # Test 3
    try:
        
        assert mid("£1.26p", 2, 3) == "1.2"
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: \"£1.26p\", 2, 3) == \"1.2\"")

    # Test 4
    try:
        
        assert mid("Hello!", 4, 0) == "Hello!"
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: \"Hello!\", 4, 0) == \"Hello!\"")

    # Test 5
    try:
        
        assert mid("Hello!", -1, 3) == "Hello!"
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: \"Hello!\", -1, 3) == \"Hello!\"")

    # Test 6
    try:
        
        assert mid("Hello!", 3, 5) == "Hello!"
        
    except:
        
        failCount = failCount + 1
        
        print("\tFailed: \"Hello!\", 3, 5) == \"Hello!\"")
    
    # Display final message
    if failCount == 0:
        
        print("\tAll tests passed.")
    

#
# Main program
#

testLeft()
testRight()
testMid()
        
