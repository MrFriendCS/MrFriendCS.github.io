# Title: H-SDD-Algorithm - Tests
# Author: Mr Friend
# Date: 20 Sep 2024

"""Tests the functions in algorithm.py"""

import algorithm


def testFindItem():
    """Tests the findItem() function"""
    
    # Local variable
    test = 1
    
    print("\nfindItem() Tests")
    print("----------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": ['A','B','C'], 'A' --> ", end="")
        assert algorithm.findItem(["A","B","C"], "A") == 0
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": ['X','Y','Z'], 'Z' --> ", end="")
        assert algorithm.findItem(["X","Y","Z"], "Z") == 2
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": ['A','B','C'], 'D' --> ", end="")
        assert algorithm.findItem(["A","B","C"], "D") == -1
        print("Passed")
        
        print("\nPASSED: findItem()")
        print("==================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: findItem()")
        print("==================\n")
        
        return 0


def testCountItem():
    """Tests the countItem() function"""
    
    # Local variable
    test = 1
    
    print("\ncountItem() Tests")
    print("-----------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": ['A','B','C'], 'A' --> ", end="")
        assert algorithm.countItem(["A","B","C"], "A") == 1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": ['X','Y','Z'], 'Z' --> ", end="")
        assert algorithm.countItem(["X","Y","Z"], "Z") == 1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": ['C','C','C'], 'C' --> ", end="")
        assert algorithm.countItem(["C","C","C"], "C") == 3
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": ['A','A','A'], 'D' --> ", end="")
        assert algorithm.countItem(["A","A","A"], "D") == 0
        print("Passed")
                     
        print("\nPASSED: countItem()")
        print("===================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: countItem()")
        print("===================\n")
        
        return 0
    

def testFindMax():
    """Tests the findMax() function"""
    
    # Local variable
    test = 1
    
    print("\nfindMax Tests")
    print("-------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": ['A','B','C'] --> ", end="")
        assert algorithm.findMax(["A","B","C"]) == "C"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": ['Z','Y','X'] --> ", end="")
        assert algorithm.findMax(["Z","Y","X"]) == "Z"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": [17,61,19] --> ", end="")
        assert algorithm.findMax([17,61,19]) == 61
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": [1.7,6.1,1.9] --> ", end="")
        assert algorithm.findMax([1.7,6.1,1.9]) == 6.1
        print("Passed")
                             
        print("\nPASSED: findMax()")
        print("=================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: findMax()")
        print("=================\n")
        
        return 0
    

def testFindMin():
    """Tests the findMin() function"""
    
    # Local variable
    test = 1
    
    print("\nfindMin() Tests")
    print("---------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": ['A','B','C'] --> ", end="")
        assert algorithm.findMin(["A","B","C"]) == "A"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": ['Z','Y','X'] --> ", end="")
        assert algorithm.findMin(["Z","Y","X"]) == "X"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": [17,61,19] --> ", end="")
        assert algorithm.findMin([17,61,19]) == 17
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": [1.7,6.1,1.9] --> ", end="")
        assert algorithm.findMin([1.7,6.1,1.9]) == 1.7
        print("Passed")
                     
        print("\nPASSED: findMin()")
        print("=================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: findMin()")
        print("=================\n")
        
        return 0


def testAll():
    """Tests all functions"""
    
    # Local variable
    passed = 0
    
    print("\nRun All Tests")
    print("-------------\n")
    
    try:
        
        passed += testFindItem()
        passed += testCountItem()
        passed += testFindMax()
        passed += testFindMin()
        
        if passed == 4:
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
    print("\nAlgorithm Tests")
    print("---------------\n")

    print("1. findItem()")
    print("2. countItem()")
    print("3. findMax()")
    print("4. findMin()")
    
    print("\na. All tests")
    print("x. Exit")

    # Get text value from user
    test = input("\nTest: ")

    if test == "1":
        testFindItem()
        
    elif test == "2":
        testCountItem()
        
    elif test == "3":
        testFindMax()
        
    elif test == "4":
        testFindMin()
             
    elif test == "a":
        # Run all tests
        testAll()
        
    elif test == "x":
        # Exit tests
        run = False
