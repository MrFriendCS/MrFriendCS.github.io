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
    print("--------------------\n")
    
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
              ": 0.1 --> ", end="")
        assert round(calculation.areaOfSquare(0.1), 2) == 0.01
        print("Passed")
                     
        print("\nPASSED: areaOfSquare()")
        print("======================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: areaOfSquare()")
        print("======================\n")
        
        return 0


def testAreaOfRectangle():
    """Tests the areaOfRectangle() function"""
    
    # Local variable
    test = 1
    
    print("\nareaOfRectangle() Tests")
    print("-----------------------\n")
    
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
              ": 0.1, 0.1 --> ", end="")
        assert round(calculation.areaOfRectangle(0.1, 0.1), 2) == 0.01
        print("Passed")
                     
        print("\nPASSED: areaOfRectangle()")
        print("=========================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: areaOfRectangle()")
        print("=========================\n")
        
        return 0
    

def testAreaOfTriangle():
    """Tests the areaOfTriangle() function"""
    
    # Local variable
    test = 1
    
    print("\nareaOfTriangle() Tests")
    print("----------------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 1, 1 --> ", end="")
        assert calculation.areaOfTriangle(1, 1) == 0.5
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 0, 1 --> ", end="")
        assert calculation.areaOfTriangle(0, 1) == -1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 1, 0 --> ", end="")
        assert calculation.areaOfTriangle(1, 0) == -1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 2, 5 --> ", end="")
        assert calculation.areaOfTriangle(2, 5) == 5
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 5, 2 --> ", end="")
        assert calculation.areaOfTriangle(5, 2) == 5
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 0.1, 0.1 --> ", end="")
        assert round(calculation.areaOfTriangle(0.1, 0.1), 3) == 0.005
        print("Passed")
                     
        print("\nPASSED: areaOfTriangle()")
        print("========================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: areaOfTriangle()")
        print("========================\n")
        
        return 0
    

def testAreaOfCircle():
    """Tests the areaOfCircle() function"""
    
    # Local variable
    test = 1
    
    print("\nareaOfCircle() Tests")
    print("--------------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 1, 'radius' --> ", end="")
        assert calculation.areaOfCircle(1, "radius") == 3.14
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 2, 'diameter' --> ", end="")
        assert calculation.areaOfCircle(2, "diameter") == 3.14
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 0, 'radius' --> ", end="")
        assert calculation.areaOfCircle(0, "radius") == -1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 0, 'diameter' --> ", end="")
        assert calculation.areaOfCircle(0, "diameter") == -1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 1, 'Hello' --> ", end="")
        assert calculation.areaOfCircle(1, "Hello") == -1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 0.1, 'radius' --> ", end="")
        assert round(calculation.areaOfCircle(0.1, "radius"), 4) == 0.0314
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 10, 'RADIUS' --> ", end="")
        assert calculation.areaOfCircle(10, "RADIUS") == 314
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 20, 'DIAMETER' --> ", end="")
        assert calculation.areaOfCircle(20, "DIAMETER") == 314
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 5, 'RaDiUs' --> ", end="")
        assert calculation.areaOfCircle(5, "RaDiUs") == 78.5
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 10, 'dIaMeTeR' --> ", end="")
        assert calculation.areaOfCircle(10, "dIaMeTeR") == 78.5
        print("Passed")
                     
        print("\nPASSED: areaOfCircle()")
        print("======================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: areaOfCircle()")
        print("======================\n")
        
        return 0
    

def testVolOfCube():
    """Tests the volOfCube() function"""
    
    # Local variable
    test = 1
    
    print("\nvolOfCube() Tests")
    print("-----------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 1 --> ", end="")
        assert calculation.volOfCube(1) == 1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 0 --> ", end="")
        assert calculation.volOfCube(0) == -1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 5 --> ", end="")
        assert calculation.volOfCube(5) == 125
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 0.1 --> ", end="")
        assert round(calculation.volOfCube(0.1), 3) == 0.001
        print("Passed")
                     
        print("\nPASSED: volOfCube()")
        print("===================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: volOfCube()")
        print("===================\n")
        
        return 0


def testVolOfCuboid():
    """Tests the volOfCuboid() function"""
    
    # Local variable
    test = 1
    
    print("\nvolOfCuboid() Tests")
    print("-------------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 1, 1, 1 --> ", end="")
        assert calculation.volOfCuboid(1, 1, 1) == 1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 0, 1, 1 --> ", end="")
        assert calculation.volOfCuboid(0, 1, 1) == -1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 1, 0, 1 --> ", end="")
        assert calculation.volOfCuboid(1, 0, 1) == -1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 1, 1, 0 --> ", end="")
        assert calculation.volOfCuboid(1, 1, 0) == -1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 2, 5, 10 --> ", end="")
        assert calculation.volOfCuboid(2, 5, 10) == 100
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 10, 5, 2 --> ", end="")
        assert calculation.volOfCuboid(10, 5, 2) == 100
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 0.1, 0.1, 0.1 --> ", end="")
        assert round(calculation.volOfCuboid(0.1, 0.1, 0.1), 3) == 0.001
        print("Passed")
                     
        print("\nPASSED: volOfCuboid()")
        print("=====================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: volOfCuboid()")
        print("=====================\n")
        
        return 0


def testVolOfCylinder():
    """Tests the volOfCylinder() function"""
    
    # Local variable
    test = 1
    
    print("\nvolOfCylinder() Tests")
    print("---------------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 1, 'radius', 1 --> ", end="")
        assert calculation.volOfCylinder(1, "radius", 1) == 3.14
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 2, 'diameter', 1 --> ", end="")
        assert calculation.volOfCylinder(2, "diameter", 1) == 3.14
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 0, 'radius, 1' --> ", end="")
        assert calculation.volOfCylinder(0, "radius", 1) == -1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 0, 'diameter', 1 --> ", end="")
        assert calculation.volOfCylinder(0, "diameter", 1) == -1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 1, 'radius, 0' --> ", end="")
        assert calculation.volOfCylinder(0, "radius", 1) == -1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 1, 'diameter', 0 --> ", end="")
        assert calculation.volOfCylinder(0, "diameter", 1) == -1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 1, 'Hello', 1 --> ", end="")
        assert calculation.volOfCylinder(1, "Hello", 1) == -1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 0.1, 'radius', 1 --> ", end="")
        assert round(calculation.volOfCylinder(0.1, "radius", 1), 4) == 0.0314
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 1, 'radius', 0.1 --> ", end="")
        assert round(calculation.volOfCylinder(1, "radius", 0.1), 3) == 0.314
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 10, 'RADIUS', 1 --> ", end="")
        assert calculation.volOfCylinder(10, "RADIUS", 1) == 314
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 20, 'DIAMETER', 1 --> ", end="")
        assert calculation.volOfCylinder(20, "DIAMETER", 1) == 314
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 1, 'RaDiUs', 5 --> ", end="")
        assert round(calculation.volOfCylinder(1, "RaDiUs", 5), 1) == 15.7
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 2, 'dIaMeTeR', 10 --> ", end="")
        assert round(calculation.volOfCylinder(2, "dIaMeTeR", 10), 1) == 31.4
        print("Passed")
                     
        print("\nPASSED: volOfCylinder()")
        print("=======================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: volOfCylinder()")
        print("=======================\n")
        
        return 0
    

def testVolOfSphere():
    """Tests the volOfSphere() function"""
    
    # Local variable
    test = 1
    
    print("\nvolOfSphere() Tests")
    print("-------------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 1, 'radius' --> ", end="")
        assert round(calculation.volOfSphere(1, "radius"), 4) == 4.1867
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 2, 'diameter' --> ", end="")
        assert round(calculation.volOfSphere(2, "diameter"), 4) == 4.1867
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 0, 'radius' --> ", end="")
        assert calculation.volOfSphere(0, "radius") == -1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 0, 'diameter' --> ", end="")
        assert calculation.volOfSphere(0, "diameter") == -1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 1, 'Hello' --> ", end="")
        assert calculation.volOfSphere(1, "Hello") == -1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 0.1, 'radius' --> ", end="")
        assert round(calculation.volOfSphere(0.1, "radius"), 7) == 0.0041867
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 10, 'RADIUS' --> ", end="")
        assert round(calculation.volOfSphere(10, "RADIUS"), 3) == 4186.667
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 20, 'DIAMETER' --> ", end="")
        assert round(calculation.volOfSphere(20, "DIAMETER"), 3) == 4186.667
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 1, 'RaDiUs' --> ", end="")
        assert round(calculation.volOfSphere(2, "RaDiUs"), 4) == 33.4933
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 2, 'dIaMeTeR' --> ", end="")
        assert round(calculation.volOfSphere(48, "dIaMeTeR"), 4) == 33.4933
        print("Passed")
                     
        print("\nPASSED: volOfSphere()")
        print("=====================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: volOfSphere()")
        print("=====================\n")
        
        return 0


def testAll():
    """Tests all functions"""
    
    # Local variable
    passed = 0
    
    print("\nRun All Tests")
    print("-------------\n")
    
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
    print("-----------------\n")

    print("1. areaOfSquare()")
    print("2. areaOfRectangle()")
    print("3. areaOfTriangle()")
    print("4. areaOfCircle()")
    print("5. volOfCube()")
    print("6. volOfCuboid()")
    print("7. volOfCylinder()")
    print("8. volOfSphere()")
    
    print("\na. All tests")
    print("x. Exit")

    # Get text value from user
    test = input("\nTest: ")

    if test == "1":
        testAreaOfSquare()
        
    elif test == "2":
        testAreaOfRectangle()
        
    elif test == "3":
        testAreaOfTriangle()
        
    elif test == "4":
        testAreaOfCircle()
        
    elif test == "5":
        testVolOfCube()
        
    elif test == "6":
        testVolOfCuboid()
        
    elif test == "7":
        testVolOfCylinder()
        
    elif test == "8":
        testVolOfSphere()
             
    elif test == "a":
        # Run all tests
        testAll()
        
    elif test == "x":
        # Exit tests
        run = False
