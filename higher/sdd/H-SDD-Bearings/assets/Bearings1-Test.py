# Title: H-SDD-Bearing - Tests
# Author: Mr Friend
# Date: 26 Sep 2024

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
              ": Read data --> ", end="")
        assert len(bearings1.getSizeData()) == 1000
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": First value --> ", end="")
        assert type(bearings1.getSizeData()[0]) == type(1.1)
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Last value --> ", end="")
        assert type(bearings1.getSizeData()[-1]) == type(1.1)
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
              ": [2.99, 2.99, 2.99] --> ", end="")
        assert bearings1.countSmall([2.99, 2.99, 2.99]) == 0
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": [2.989, 2.99, 2.99] --> ", end="")
        assert bearings1.countSmall([2.989, 2.99, 2.99]) == 1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": [2.989, 2.989, 2.99] --> ", end="")
        assert bearings1.countSmall([2.989, 2.989, 2.99]) == 2
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": [2.989, 2.989, 2.989] --> ", end="")
        assert bearings1.countSmall([2.989, 2.989, 2.989]) == 3
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
              ": [3.01, 3.01, 3.01] --> ", end="")
        assert bearings1.countBig([3.01, 3.01, 3.01]) == 0
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": [3.011, 3.01, 3.01] --> ", end="")
        assert bearings1.countBig([3.011, 3.01, 3.01]) == 1
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": [3.011, 3.011, 3.01] --> ", end="")
        assert bearings1.countBig([3.011, 3.011, 3.01]) == 2
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": [3.011, 3.011, 3.011] --> ", end="")
        assert bearings1.countBig([3.011, 3.011, 3.011]) == 3
        print("Passed")
                     
        print("\nPASSED: countBig()")
        print("==================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: countBig()")
        print("==================\n")
        
        return 0
    

def testCalcSmallPercent():
    """Tests the calcSmallPercent() function"""
    
    # Local variable
    test = 1
    
    print("\ncalcSmallPercent() Tests")
    print("------------------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 14 --> ", end="")
        assert bearings1.calcSmallPercent(14) == 1.4
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 15 --> ", end="")
        assert bearings1.calcSmallPercent(15) == 1.5
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 19 --> ", end="")
        assert bearings1.calcSmallPercent(19) == 1.9
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 20 --> ", end="")
        assert bearings1.calcSmallPercent(20) == 2.0
        print("Passed")
                     
        print("\nPASSED: calcSmallPercent()")
        print("==========================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: calcSmallPercent()")
        print("==========================\n")
        
        return 0
    
    
def testCalcBigPercent():
    """Tests the calcBigPercent() function"""
    
    # Local variable
    test = 1
    
    print("\ncalcBigPercent() Tests")
    print("----------------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 14 --> ", end="")
        assert bearings1.calcBigPercent(14) == 1.4
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 15 --> ", end="")
        assert bearings1.calcBigPercent(15) == 1.5
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 19 --> ", end="")
        assert bearings1.calcBigPercent(19) == 1.9
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 20 --> ", end="")
        assert bearings1.calcBigPercent(20) == 2.0
        print("Passed")
                     
        print("\nPASSED: calcBigPercent()")
        print("========================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: calcBigPercent()")
        print("========================\n")
        
        return 0


def testCalcBatchResult():
    """Tests the calcBatchResult() function"""
    
    # Local variable
    test = 1
    
    print("\ncalcBatchResult() Tests")
    print("-----------------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 0, 0 --> ", end="")
        assert bearings1.calcBatchResult(0, 0) == True
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 2, 0 --> ", end="")
        assert bearings1.calcBatchResult(2, 0) == False
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 0, 2 --> ", end="")
        assert bearings1.calcBatchResult(0, 2) == False
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 1.5, 1.5 --> ", end="")
        assert bearings1.calcBatchResult(1.5, 1.5) == False
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 1.5, 1.4 --> ", end="")
        assert bearings1.calcBatchResult(1.5, 1.4) == True
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 1.4, 1.5 --> ", end="")
        assert bearings1.calcBatchResult(1.4, 1.5) == True
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 1.9, 0 --> ", end="")
        assert bearings1.calcBatchResult(1.9, 0) == True
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 0, 1.9 --> ", end="")
        assert bearings1.calcBatchResult(0, 1.9) == True
        print("Passed")
                     
        print("\nPASSED: calcBatchResult()")
        print("=========================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: calcBatchResult()")
        print("=========================\n")
        
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
        passed += testCountSmall()
        passed += testCountBig()
        passed += testCalcSmallPercent()
        passed += testCalcBigPercent()
        passed += testCalcBatchResult()
        passed += testWriteData1()
        passed += testWriteData2()
        
        if passed == 10:
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

    print(" 1. getSizeData()")
    print(" 2. findMin()")
    print(" 3. findMax()")
    print(" 4. countSmall()")
    print(" 5. countBig()")
    print(" 6. calcSmallPercent()")
    print(" 7. calcBigPercent()")
    print(" 8. calcBatchResult()")
    print(" 9. writeData() - Test 1")
    print("10. writeData() - Test 2")
    
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
        testCalcSmallPercent()
        
    elif test == "7":
        testCalcBigPercent()
        
    elif test == "8":
        testCalcBatchResult()
        
    elif test == "9":
        testWriteData1()
        
    elif test == "10":
        testWriteData2()
             
    elif test == "a":
        # Run all tests
        testAll()
        
    elif test == "x":
        # Exit tests
        run = False
