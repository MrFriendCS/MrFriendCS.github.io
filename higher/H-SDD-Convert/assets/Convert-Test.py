# Title: H-SDD-Convert Tests
# Author: Mr Friend
# Date: 8 Sep 2024

"""Tests the functions in convert.py"""

import convert


def testF2C():
    """Tests the f2c() function"""
    
    # Local variable
    test = 1
    
    print("\nFahrenheit to Celsius Tests")
    print("---------------------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 32.0 --> ", end="")
        assert convert.f2c(32.0) == 0
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": -40.0 --> ", end="")
        assert convert.f2c(-40.0) == -40.0
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 100.0 --> ", end="")
        assert convert.f2c(100.0) == 37.8
        print("Passed")
                     
        print("\nAll f2c() tests passed!")
        print("===========+===========\n")
        
    except:
        print("FAILED")
        print("\nf2c() testing ended")
        print("===================\n")


def testC2F():
    """Tests the c2f() function"""
    
    # Local variable
    test = 1
    
    print("\nCelsius to Fahrenheit Tests")
    print("---------------------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 0.0 --> ", end="")
        assert convert.c2f(0.0) == 32.0
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": -40.0 --> ", end="")
        assert convert.c2f(-40.0) == -40.0
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 100.0 --> ", end="")
        assert convert.c2f(100.0) == 212.0
        print("Passed")
                
        print("\nAll c2f() tests passed!")
        print("=======================\n")
        
    except:
        print("FAILED")
        print("\nc2f() testing ended")
        print("====================\n")


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
        
    except:
        print("FAILED")
        print("\nm2km() testing ended")
        print("====================\n")


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
        
    except:
        print("FAILED")
        print("\nkm2m() testing ended")
        print("====================\n")


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
        
    except:
        print("FAILED")
        print("\nfi2cm() testing ended")
        print("=====================\n")
        

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
        
    except:
        print("FAILED")
        print("\ncm2fi() testing ended")
        print("=====================\n")


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
        
    except:
        print("FAILED")
        print("\nsl2kg() testing ended")
        print("=====================\n")
        

def testKG2SL():
    """Tests the kg2sl() function"""
    
    # Local variable
    test = 1
    
    print("\nKilograms to Stones and Pounds Tests")
    print("------------------------------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 66.7 --> ", end="")
        assert convert.kg2sl(66.7) == (10, 7)
        print("Passed")
                
        print("\nAll kg2sl() tests passed!")
        print("=========================\n")
        
    except:
        print("FAILED")
        print("\nkg2sl() testing ended")
        print("=====================\n")


#
# Main program
#

# Initialise global variables
test = ""
run = True

while run:
    print("\nConvert Tests")
    print("-------------")

    print("\n1. f2c tests")
    print("2. c2f tests")
    print("3. m2km tests")
    print("4. km2m tests")
    print("5. fi2cm tests")
    print("6. cm2fi tests")
    print("7. sl2kg tests")
    print("8. kg2sl tests")
    print("x. Exit")

    # Get text value from user
    test = input("\nTest: ")

    if test == "1":
        # Celsius to Fahrenheit tests
        testF2C()
        
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
        
    elif test == "x":
        # Exit tests
        run = False

