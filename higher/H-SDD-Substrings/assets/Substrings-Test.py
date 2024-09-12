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
    print("------------\n")
    
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


def testM2KM():
    """Tests the m2km() function"""
    
    # Local variable
    test = 1
    
    print("\nMiles to Kilometres Tests")
    print("-------------------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 5.0 --> ", end="")
        assert convert.m2km(5.0) == 8.0
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 500.0 --> ", end="")
        assert convert.m2km(500.0) == 804.7
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 50000.0 --> ", end="")
        assert convert.m2km(50000.0) == 80467.2
        print("Passed")
                
        print("\nAll m2km() tests passed!")
        print("========================\n")
        
        return 1
        
    except:
        print("FAILED")
        print("\nm2km() testing ended")
        print("====================\n")
        
        return 0


def testKM2M():
    """Tests the km2m() function"""
    
    # Local variable
    test = 1
    
    print("\nKilometres to Miles Tests")
    print("-------------------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 8.0 --> ", end="")
        assert convert.km2m(8.0) == 5.0
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 800.0 --> ", end="")
        assert convert.km2m(800.0) == 497.1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 80000.0 --> ", end="")
        assert convert.km2m(80000.0) == 49709.7
        print("Passed")
                
        print("\nAll km2m() tests passed!")
        print("========================\n")
        
        return 1
        
    except:
        print("FAILED")
        print("\nkm2m() testing ended")
        print("====================\n")
        
        return 0


def testFI2CM():
    """Tests the fi2cm() function"""
    
    # Local variable
    test = 1
    
    print("\nFeet and Inches to Centimetres Tests")
    print("------------------------------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 6, 6 --> ", end="")
        assert convert.fi2cm(6, 6) == 198.1
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
        # Celsius to Fahrenheit tests
        testLeft()
        
    elif test == "2":
        # Fahrenheit to Celsius tests
        testC2F()
        
    elif test == "3":
        # Miles to kilometres tests
        testM2KM()
        
    elif test == "4":
        # Kilometres to miles tests
        testKM2M()
        
    elif test == "5":
        # Feet and inches to centimetres tests
        testFI2CM()
        
    elif test == "6":
        # Centimetres to feet and inches tests
        testCM2FI()
        
    elif test == "7":
        # Stones and pounds to kilograms tests
        testSL2KG()
        
    elif test == "8":
        # Kilograms to stones and pounds tests
        testKG2SL()
        
    elif test == "a":
        # Run all tests
        testAll()
        
    elif test == "x":
        # Exit tests
        run = False

