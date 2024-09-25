# Title: H-SDD-Bearing - Tests
# Author: Mr Friend
# Date: 25 Sep 2024

"""Tests the functions in bearings.py"""

import bearings1


def testGetSizeData():
    """Tests the getSizeData() function"""
    
    # Local variable
    test = 1
    
    print("\ngetSizeData() Tests")
    print("-------------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": ['A','B','C'], 'A' --> ", end="")
        assert bearings1.findItem(["A","B","C"], "A") == 0
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": ['X','Y','Z'], 'Z' --> ", end="")
        assert bearings1.findItem(["X","Y","Z"], "Z") == 2
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": ['A','B','C'], 'D' --> ", end="")
        assert bearings1.findItem(["A","B","C"], "D") == -1
        print("Passed")
        
        print("\nPASSED: getSizeData()")
        print("=====================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: getSizeData()")
        print("=====================\n")
        
        return 0


def testFindMin():
    """Tests the findMin() function"""
    
    # Local variable
    test = 1
    
    print("\nfindMin() Tests")
    print("---------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": [1, 2, 3] --> ", end="")
        assert bearings1.findMin([1,2,3]) == 1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": [3, 1, 2] --> ", end="")
        assert bearings1.findMin([3,1,2]) == 1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": [2, 3, 1] --> ", end="")
        assert bearings1.findMin([2,3,1]) == 1
        print("Passed")
                     
        print("\nPASSED: findMin()")
        print("=================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: findMin()")
        print("=================\n")
        
        return 0
  

def testFindMax():
    """Tests the findMax() function"""
    
    # Local variable
    test = 1
    
    print("\nfindMax Tests")
    print("-------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": [1, 2, 3] --> ", end="")
        assert bearings1.findMax([1,2,3]) == 3
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": [3, 1, 2] --> ", end="")
        assert bearings1.findMax([3,1,2]) == 3
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": [2, 3, 1] --> ", end="")
        assert bearings1.findMax([2,3,1]) == 3
        print("Passed")
                             
        print("\nPASSED: findMax()")
        print("=================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: findMax()")
        print("=================\n")
        
        return 0
    
    
def testCountSmall():
    """Tests the countSmall() function"""
    
    # Local variable
    test = 1
    
    print("\ncountSmall() Tests")
    print("----------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": [3.0, 3.0, 3.0] --> ", end="")
        assert bearings1.countSmall([3.0, 3.0, 3.0]) == 0
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": [2.99, 3.0, 3.0] --> ", end="")
        assert bearings1.countSmall([2.99, 3.0, 3.0]) == 1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": [2.99, 2.99, 3.0] --> ", end="")
        assert bearings1.countSmall([2.99, 2.99, 3.0]) == 2
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": [2.99, 2.99, 2.99] --> ", end="")
        assert bearings1.countSmall([2.99, 2.99, 2.99]) == 3
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": [2.91, 2.91, 2.91] --> ", end="")
        assert bearings1.countSmall([2.991, 2.991, 2.991]) == 0
        print("Passed")
                     
        print("\nPASSED: countSmall()")
        print("====================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: countSmall()")
        print("====================\n")
        
        return 0


def testCountBig():
    """Tests the countBig() function"""
    
    # Local variable
    test = 1
    
    print("\ncountItem() Tests")
    print("-----------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": [3.0, 3.0, 3.0] --> ", end="")
        assert bearings1.countBig([3.0, 3.0, 3.0]) == 0
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": [3.01, 3.0, 3.0] --> ", end="")
        assert bearings1.countBig([3.01, 3.0, 3.0]) == 1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": [3.01, 3.01, 3.0] --> ", end="")
        assert bearings1.countBig([3.01, 3.01, 3.0]) == 2
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": [3.01, 3.01, 3.01] --> ", end="")
        assert bearings1.countBig([3.01, 3.01, 3.01]) == 3
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": [3.009, 3.009, 3.009] --> ", end="")
        assert bearings1.countBig([3.009, 3.009, 3.009]) == 0
        print("Passed")
                     
        print("\nPASSED: countBig()")
        print("==================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: countBig()")
        print("==================\n")
        
        return 0


def testCalcResults():
    """Tests the calcResults() function"""
    
    # Local variable
    test = 1
    
    print("\ncalcResults() Tests")
    print("-------------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 0, 0 --> ", end="")
        assert bearings1.calcResults(0, 0) == (0.0, 0.0, True)
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 20, 0 --> ", end="")
        assert bearings1.calcResults(20, 0) == (2.0, 0.0, False)
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 0, 20 --> ", end="")
        assert bearings1.calcResults(0, 20) == (0.0, 2.0, False)
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 15, 15 --> ", end="")
        assert bearings1.calcResults(15, 15) == (1.5, 1.5, False)
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 15, 14 --> ", end="")
        result = bearings1.calcResults(15, 14)
        assert result[0] == 1.5
        assert round(result[1], 1) == 1.4
        assert result[2] == True
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 14, 15 --> ", end="")
        result = bearings1.calcResults(14, 15)
        assert round(result[0], 1) == 1.4
        assert result[1] == 1.5
        assert result[2] == True
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 19, 0 --> ", end="")
        assert bearings1.calcResults(19, 0) == (1.9, 0.0, True)
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 0, 19 --> ", end="")
        assert bearings1.calcResults(0, 19) == (0.0, 1.9, True)
        print("Passed")
                     
        print("\nPASSED: calcResults()")
        print("=====================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: calcResults()")
        print("=====================\n")
        
        return 0
    

def testWriteData1():
    """Tests the writeData() function"""
    
    # Local variable
    test = 1
    
    print("\nwriteData() Tests")
    print("-----------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 1.0, 2.0, 3.0, 4.0, True --> ", end="")
        bearings1.writeData(1.0, 2.0, 3.0, 4.0, True)
        print("Written")
                     
        print("\nCompleted: writeData()")
        print("======================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: writeData()")
        print("===================\n")
        
        return 0


def testWriteData2():
    """Tests the writeData() function"""
    
    # Local variable
    test = 1
    
    print("\nwriteData() Tests")
    print("-----------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 0.1, 0.2, 0.3, 0.4, False --> ", end="")
        bearings1.writeData(0.1, 0.2, 0.3, 0.4, False)
        print("Written")
                     
        print("\nCompleted: writeData()")
        print("======================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: writeData()")
        print("===================\n")
        
        return 0


def testAll():
    """Tests all functions"""
    
    # Local variable
    passed = 0
    
    print("\nRun All Tests")
    print("-------------\n")
    
    try:
        
        passed += testGetSizeData()
        passed += testFindMin()
        passed += testFindMax()
        passed += testCountBig()
        passed += testCountBig()
        passed += testCalcResults()
        passed += writeData()
        
        if passed == 7:
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
    print("\nBearings Tests")
    print("--------------\n")

    print("1. getSizeData()")
    print("2. findMin()")
    print("3. findMax()")
    print("4. countSmall()")
    print("5. countBig()")
    print("6. calcResults()")
    print("7. writeData() - Test 1")
    print("8. writeData() - Test 2")
    
    print("\na. All tests")
    print("x. Exit")

    # Get text value from user
    test = input("\nTest: ")

    if test == "1":
        testGetSizeData()
        
    elif test == "2":
        testFindMin()
        
    elif test == "3":
        testFindMax()
        
    elif test == "4":
        testCountSmall()
        
    elif test == "5":
        testCountBig()
        
    elif test == "6":
        testCalcResults()
        
    elif test == "7":
        testWriteData1()
        
    elif test == "8":
        testWriteData2()
             
    elif test == "a":
        # Run all tests
        testAll()
        
    elif test == "x":
        # Exit tests
        run = False
