# Title: H-SDD-Calculation - Tests
# Author: Mr Friend
# Date: 19 Sep 2024

"""Tests the functions in calculation.py"""

import calculation


def testAreaOfSquare():
    """Tests the areaOfSqaure() function"""
    
    # Local variable
    test = 1
    
    print("\nareaOfSqaure() Tests")
    print("------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 1 --> ", end="")
        assert calculation.areaOfSquare(1) == 1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 0 --> ", end="")
        assert calculation.areaOfSquare(0) == -1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 5 --> ", end="")
        assert calculation.areaOfSquare(5) == 25
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 0.5 --> ", end="")
        assert calculation.areaOfSquare(0.5) == 0.25
        print("Passed")
                     
        print("\nPASSED: areaOfSquare()")
        print("====================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: areaOfSquare()")
        print("====================\n")
        
        return 0


def testAreaOfRectangle():
    """Tests the areaOfRectangle() function"""
    
    import os
    
    # Local variable
    test = 1
    
    print("\nareaOfRectangle() Tests")
    print("-----------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 1, 1 --> ", end="")
        assert calculation.areaOfRectangle(1, 1) == 1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 0, 1 --> ", end="")
        assert calculation.areaOfRectangle(0, 1) == -1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 1, 0 --> ", end="")
        assert calculation.areaOfRectangle(1, 0) == -1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 2, 5 --> ", end="")
        assert calculation.areaOfRectangle(2, 5) == 10
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 5, 2 --> ", end="")
        assert calculation.areaOfRectangle(5, 2) == 10
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 0.5, 0.5 --> ", end="")
        assert calculation.areaOfRectangle(0.5, 0.5) == 0.25
        print("Passed")
                     
        print("\nPASSED: areaOfRectangle()")
        print("====================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: areaOfRectangle()")
        print("===============\n")
        
        return 0


def testAll():
    """Tests all functions"""
    
    # Local variable
    passed = 0
    
    print("\nRun All Tests")
    print("--------------\n")
    
    try:
        
        passed += testAreaOfSquare()
        passed += testAreaOfRectangle()
        passed += testAreaOfTriangle()
        passed += testAreaOfCircle()
        passed += testVolOfCube()
        passed += testVolOfCuboid()
        passed += testVolOfCylinder()
        passed += testVolOfSphere()
        
        if passed == 8:
            print("\nTesting of all functions: PASSED!")
            print("=================================\n")
        else:
            1/0  # Throws an exception
        
    except:
            print("\nTesting of all functions: FAILED!")
            print("=================================\n")
        

#
# Main program
#

# Initialise global variables
test = ""
run = True

while run:
    print("\nCalculation Tests")
    print("-----------------------\n")

    print("1. areaOfSquare() tests")
    print("2. areaOfRectangle() tests")
    print("3. areaOfTriangle() tests")
    print("4. areaOfCircle() tests")
    print("5. volOfCube() tests")
    print("6. volOfCuboid() tests")
    print("7. volOfCylinder() tests")
    print("8. volOfSphere() tests")
    
    print("\na. All tests")
    print("x. Exit")

    # Get text value from user
    test = input("\nTest: ")

    if test == "1":
        # 
        testAreaOfSquare()
        
    elif test == "2":
        # 
        testAreaOfRectangle()
        
    elif test == "3":
        # 
        testAreaOfTriangle()
        
    elif test == "4":
        # 
        testAreaOfCircle()
        
    elif test == "5":
        # 
        testVolOfCube()
        
    elif test == "6":
        # 
        testVolOfCuboid()
        
    elif test == "7":
        # 
        testVolOfCylinder()
        
    elif test == "8":
        # 
        testVolOfSphere()
             
    elif test == "a":
        # Run all tests
        testAll()
        
    elif test == "x":
        # Exit tests
        run = False
