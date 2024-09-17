# Title: H-SDD-Write-Data - Part 1 Tests
# Author: Mr Friend
# Date: 17 Sep 2024

"""Tests the functions in writeData1.py"""

import writeData1


def testRandomData():
    """Tests the randomData() function"""
    
    # Local variable
    test = 1
    uppers = []
    numbers = []
    lowers = []
    
    print("\nrandomData() Tests")
    print("------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": Uppercase --> ", end="")
        assert type(writeData1.randomData(3)[0][0]) == type("A")
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Number --> ", end="")
        assert type(writeData1.randomData(3)[1][1]) == type(0)
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Lowercase --> ", end="")
        assert type(writeData1.randomData(3)[2][2]) == type("a")
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": All uppercase --> ", end="")
        
        uppers = writeData1.randomData(260)[0]
        for counter in range(26):
            assert chr(65 + counter) in uppers
            
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": All numbers --> ", end="")
        
        numbers = writeData1.randomData(260)[1]
        for counter in range(10):
            counter in numbers
            
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": All lowercase --> ", end="")
        
        lowers = writeData1.randomData(260)[2]
        for counter in range(26):
            assert chr(97 + counter) in lowers
            
        print("Passed")
                     
        print("\nPASSED: randomData()")
        print("====================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: randomData()")
        print("====================\n")
        
        return 0


def testWriteData():
    """Tests the writeData() function"""
    
    import os
    
    # Local variable
    test = 1
    
    print("\nwriteData() Tests")
    print("-----------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": Write Data --> ", end="")
        
        writeData1.writeData(["A","B","C"],[1,2,3],["a","b","c"])
        assert os.path.getsize("randomData.csv") == 21
        
        print("Passed")
                     
        print("\nPASSED: writeData()")
        print("===================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: right()")
        print("===============\n")
        
        return 0


def testAll():
    """Tests all functions"""
    
    # Local variable
    passed = 0
    
    print("\nRun All Tests")
    print("--------------\n")
    
    try:
        
        passed += testRandomData()
        passed += testWriteData()
        
        if passed == 2:
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
    print("\nWrite Data Part 1 Tests")
    print("-----------------------\n")

    print("1. randomData() tests")
    print("2. writeData() tests")
    print("\na. All tests")
    print("x. Exit")

    # Get text value from user
    test = input("\nTest: ")

    if test == "1":
        # 
        testRandomData()
        
    elif test == "2":
        # 
        testWriteData()
             
    elif test == "a":
        # Run all tests
        testAll()
        
    elif test == "x":
        # Exit tests
        run = False
