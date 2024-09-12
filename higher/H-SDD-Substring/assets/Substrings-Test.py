# Title: H-SDD-Substring Tests
# Author: Mr Friend
# Date: 12 Sep 2024

"""Tests the functions in substring.py"""

import substring


def testLeft():
    """Tests the left() function"""
    
    # Local variable
    test = 1
    
    print("\nleft() Tests")
    print("------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 'Hello', 4 --> ", end="")
        assert substring.left("Hello", 4) == "Hell"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 'Hello', 14 --> ", end="")
        assert substring.left("Hello", 14) == "Hello"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": '', 4 --> ", end="")
        assert substring.left("", 4) == ""
        print("Passed")
                     
        print("\nAll left() tests passed!")
        print("========================\n")
        
        return 1
        
    except:
        print("FAILED")
        print("\nleft() testing ended")
        print("====================\n")
        
        return 0


def testRight():
    """Tests the right() function"""
    
    # Local variable
    test = 1
    
    print("\nright() Tests")
    print("-------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 'Hello', 4 --> ", end="")
        assert substring.right("Hello", 4) == "ello"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 'Hello', 14 --> ", end="")
        assert substring.right("Hello", 14) == "Hello"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": '', 4 --> ", end="")
        assert substring.right("", 4) == ""
        print("Passed")
                     
        print("\nAll right() tests passed!")
        print("=========================\n")
        
        return 1
        
    except:
        print("FAILED")
        print("\nright() testing ended")
        print("=====================\n")
        
        return 0


def testMid():
    """Tests the mid() function"""
    
    # Local variable
    test = 1
    
    print("\nmid() Tests")
    print("-----------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 'Hello world!', 4, 5 --> ", end="")
        assert substring.mid("Hello world!", 4, 5) == "lo wo"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 'Hello world!', 2, 6 --> ", end="")
        assert substring.mid("Hello world!", 2, 6) == "ello w"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 'Hello world!', 2, 5 --> ", end="")
        assert substring.mid("Hello world!", 4, 5) == "lo wo"
        print("Passed")
                
        print("\nAll mid() tests passed!")
        print("========================\n")
        
        return 1
        
    except:
        print("FAILED")
        print("\nmid() testing ended")
        print("====================\n")
        
        return 0


def testLower():
    """Tests the lower() function"""
    
    # Local variable
    test = 1
    
    print("\nlower() Tests")
    print("-------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 'Hello!' --> ", end="")
        assert substring.lower("Hello!") == "hello!"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 'Hello!' --> ", end="")
        assert substring.lower("Hello!") == "hello!"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 'Hello!' --> ", end="")
        assert substring.lower("Hello!") == "hello!"
        print("Passed")
                
        print("\nAll lower() tests passed!")
        print("=========================\n")
        
        return 1
        
    except:
        print("FAILED")
        print("\nlower() testing ended")
        print("====================\n")
        
        return 0


def testUpper():
    """Tests the upper() function"""
    
    # Local variable
    test = 1
    
    print("\nFupper() Tests")
    print("--------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 'Hello!' --> ", end="")
        assert substring.upper("Hello!") == "HELLO!"
        print("Passed")
                
        print("\nAll fi2cm() tests passed!")
        print("=========================\n")
        
        return 1
        
    except:
        print("FAILED")
        print("\nfi2cm() testing ended")
        print("=====================\n")
        
        return 0
        

def testCM2FI():
    """Tests the cm2fi() function"""
    
    # Local variable
    test = 1
    
    print("\nCentimetres to Feet and Inches Tests")
    print("------------------------------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 200 --> ", end="")
        assert convert.cm2fi(200) == (6, 7)
        print("Passed")
                
        print("\nAll cm2fi() tests passed!")
        print("=========================\n")
        
        return 1
        
    except:
        print("FAILED")
        print("\ncm2fi() testing ended")
        print("=====================\n")
        
        return 0


def testSL2KG():
    """Tests the sl2kg() function"""
    
    # Local variable
    test = 1
    
    print("\nStones and Pounds to Kilograms Tests")
    print("------------------------------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 10, 7 --> ", end="")
        assert convert.sl2kg(10, 7) == 66.7
        print("Passed")
                
        print("\nAll sl2kg() tests passed!")
        print("=========================\n")
        
        return 1
        
    except:
        print("FAILED")
        print("\nsl2kg() testing ended")
        print("=====================\n")
        
        return 0
        

def testKG2SL():
    """Tests the kg2sl() function"""
    
    # Local variable
    test = 1
    
    print("\nKilograms to Stones and Pounds Tests")
    print("------------------------------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 10.0 --> ", end="")
        assert convert.kg2sl(10.0) == (1, 8)
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 150.0 --> ", end="")
        assert convert.kg2sl(150.0) == (23, 9)
        print("Passed")
                
        print("\nAll kg2sl() tests passed!")
        print("=========================\n")
        
        return 1
        
    except:
        print("FAILED")
        print("\nkg2sl() testing ended")
        print("=====================\n")
        
        return 0


def testAll():
    """Tests all functions"""
    
    # Local variable
    passed = 0
    
    print("\nRun All Tests")
    print("--------------\n")
    
    try:
        
        passed += testF2C()
        passed += testC2F()
        passed += testM2KM()
        passed += testKM2M()
        passed += testFI2CM()
        passed += testCM2FI()
        passed += testSL2KG()
        passed += testKG2SL()
        
        if passed == 8:
            print("\nTesting of all functions passed!")
            print("================================\n")
        else:
            1/0  # Throws an exception
        
    except:
            print("\nTesting of all functions FAILED!")
            print("================================\n")
        

#
# Main program
#

# Initialise global variables
test = ""
run = True

while run:
    print("\nConvert Tests")
    print("-------------")

    print("\n1. left() tests")
    print("2. right() tests")
    print("3. mid() tests")
    print("4. lower() tests")
    print("5. upper() tests")
    print("6. reverse() tests")
    print("7. swap() tests")
    print("8. reverse() tests")
    print("9. remove() tests")
    print("\na. All tests")
    print("x. Exit")

    # Get text value from user
    test = input("\nTest: ")

    if test == "1":
        # 
        testLeft()
        
    elif test == "2":
        # 
        testRight()
        
    elif test == "3":
        # 
        testMid()
        
    elif test == "4":
        # 
        testLower()
        
    elif test == "5":
        # 
        testUpper()
        
    elif test == "6":
        # 
        testReverse()
        
    elif test == "7":
        # 
        testSwap()
        
    elif test == "8":
        # 
        testRemove()
        
    elif test == "a":
        # Run all tests
        testAll()
        
    elif test == "x":
        # Exit tests
        run = False

