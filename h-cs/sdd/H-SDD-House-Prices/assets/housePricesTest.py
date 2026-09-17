# Title: H SDD - House Prices - Tests
# Author: Mr Friend
# Date: 17 Sep 2026

"""Tests the functions in housePrices.py"""

import housePrices


def testReadData() -> int:
    """Tests the readData() function"""
    
    # Local variable
    test: int = 1
    
    print("\nreadData() Tests")
    print("----------------\n")
    
    try:
        
        # Array of postcodes
        
        print("Test " + str(test) +
              ": Read data, postcodes array --> ", end="")
        assert len(housePrices.readData()[0]) == 1000
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": First value --> ", end="")
        assert type(housePrices.readData()[0][0]) == type("str")
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Last value --> ", end="")
        assert type(housePrices.readData()[0][-1]) == type("str")
        print("Passed")
        
        # Array of prices
        
        print("Test " + str(test) +
              ": Read data, prices array --> ", end="")
        assert len(housePrices.readData()[1]) == 1000
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": First value --> ", end="")
        assert type(housePrices.readData()[1][0]) == type(123)
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Last value --> ", end="")
        assert type(housePrices.readData()[1][-1]) == type(123)
        print("Passed")
        
        print("\nPASSED: readData()")
        print("==================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: readData()")
        print("==================\n")
        
        return 0


def testCountHS0() -> int:
    """Tests the countHS0() function"""
    
    # Local variables
    test: int = 1
    inputs: list[list[str]]
    outputs: list[int]
    
    # Values
    inputs = [['HS1 1AB', 'HS2 2CD', 'HS3 3EF'],
              ['HS0 1AB', 'HS2 2CD', 'HS3 3EF'],
              ['HS0 1AB', 'HS2 2CD', 'HS0 3EF'],
              ['HS0 1AB', 'HS0 2CD', 'HS0 3EF']]
    outputs = [0, 1, 2, 3]
    
    print("\ncountHS0() Tests")
    print("------------===-\n")
    
    try:
        
        for index in range(len(inputs)):
            
            print(f'Test {str(test)}: countHS0({inputs[index]}) --> ', end="")
            
            assert housePrices.countHS0(inputs[index]) == outputs[index]
            
            print("Passed")
            
            test += 1
               
        print("\nPASSED: countHS0()")
        print("==================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: countHS0()")
        print("==================\n")
        
        return 0
  

def testFixHS0() -> int:
    """Tests the fixHS0() function"""
    
    # Local variables
    test: int = 1
    inputs: list[list[str]]
    outputs: list[list[str]]
    
    # Values
    inputs = [['HS1 1AB', 'HS2 2CD', 'HS3 3EF'],
              ['HS0 1AB', 'HS2 2CD', 'HS3 3EF'],
              ['HS0 1AB', 'HS2 2CD', 'HS0 3EF'],
              ['HS0 1AB', 'HS0 2CD', 'HS0 3EF']]
    outputs = [['HS1 1AB', 'HS2 2CD', 'HS3 3EF'],
               ['HS1 1AB', 'HS2 2CD', 'HS3 3EF'],
               ['HS1 1AB', 'HS2 2CD', 'HS1 3EF'],
               ['HS1 1AB', 'HS1 2CD', 'HS1 3EF']]
    
    print("\nfixHS0() Tests")
    print("--------------\n")
    
    try:
        
        for index in range(len(inputs)):
            
            print(f'Test {str(test)}: fixHS0({inputs[index]}) --> ', end="")
            
            assert housePrices.fixHS0(inputs[index]) == outputs[index]
            
            print("Passed")
            
            test += 1
               
        print("\nPASSED: fixHS0()")
        print("================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: fixHS0()")
        print("================\n")
        
        return 0
    
    
def testNewPrices() -> int:
    """Tests the newPrices() function"""
    
    # Local variables
    test: int = 1
    inputs1: list[list[str]]
    inputs2: list[list[int]]
    outputs: list[list[int]]
    
    # Values
    inputs1 = [['HS1 9AB', 'HS2 8CD', 'HS3 7EF'],
               ['HS4 6GH', 'HS5 5IJ', 'HS6 4KL'],
               ['HS7 3MN', 'HS8 2OP', 'HS9 1QR']]
    inputs2 = [[1000, 1000, 1000],
               [1000, 1000, 1000],
               [1000, 1000, 1000]]
    outputs = [[980, 980, 980],
               [980, 980, 1020],
               [1020, 1020, 1050]]
    
    print("\nnewPrices() Tests")
    print("-----------------\n")
    
    try:
        
        for index in range(len(inputs1)):
            
            print(f'Test {str(test)}: newPrices({inputs1[index]}, ', \
                  f'{inputs2[index]}) --> ', end="")
            
            assert housePrices.newPrices(inputs1[index], inputs2[index]) == outputs[index]
            
            print("Passed")
            
            test += 1
               
        print("\nPASSED: newPrices()")
        print("===================\n")
        
        return 1
    
    except:
        print("Failed")
        print("\nFAILED: newPrices()")
        print("===================\n")
        
        return 0


def testFindLowest() -> int:
    """Tests the findLowest() function"""
    
    # Local variables
    test: int = 1
    inputs: list[list[int]]
    outputs: list[int]
    
    # Values
    inputs = [[0, 1, 2],
              [1, 2, 0],
              [1, 0, 2]]
    outputs = [0, 0, 0]
    
    print("\nfindLowest() Tests")
    print("------------------\n")
    
    try:
        
        for index in range(len(inputs)):
            
            print(f'Test {str(test)}: findLowest({inputs[index]}) --> ', end="")
            
            assert housePrices.findLowest(inputs[index]) == outputs[index]
            
            print("Passed")
            
            test += 1
               
        print("\nPASSED: ()")
        print("====================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: findLowest()")
        print("====================\n")
        
        return 0
    

def testFindHighest() -> int:
    """Tests the findHighest() function"""
    
    # Local variables
    test: int = 1
    inputs: list[list[int]]
    outputs: list[int]
    
    # Values
    inputs = [[2, 1, 1],
              [0, 1, 2],
              [0, 2, 1]]
    outputs = [2, 2, 2]
    
    print("\nfindHighest() Tests")
    print("-------------------\n")
    
    try:
        
        for index in range(len(inputs)):
            
            print(f'Test {str(test)}: findHighest({inputs[index]}) --> ', end="")
            
            assert housePrices.findHighest(inputs[index]) == outputs[index]
            
            print("Passed")
            
            test += 1
               
        print("\nPASSED: ()")
        print("====================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: findHighest()")
        print("=====================\n")
        
        return 0


def testCountValues() -> int:
    """Tests the countValues() function"""
    
    # Local variables
    test: int = 1
    inputs1: list[list[int]]
    inputs2: list[int]
    outputs: list[int]
    
    # Values
    inputs1 = [[0, 0, 0],
               [1, 0, 0],
               [1, 0, 1],
               [1, 1, 1]]
    inputs2 = [1, 1, 1, 1]
    outputs = [0, 1, 2, 3]
    
    print("\ncountValues() Tests")
    print("-------------------\n")
    
    try:
        
        for index in range(len(inputs1)):
            
            print(f'Test {str(test)}: countValues({inputs1[index]}, ', \
                  f'{inputs2[index]}) --> ', end="")
            
            assert housePrices.countValues(inputs1[index], inputs2[index]) == outputs[index]
            
            print("Passed")
            
            test += 1
               
        print("\nPASSED: ()")
        print("====================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: countValues()")
        print("=====================\n")
        
        return 0
    

def testWriteSummary() -> int:
    """Tests the writeSummary() function"""
    
    print("\nwriteSummary() Tests")
    print("--------------------\n")
    
    try:
        
        print("Test: writeSummary(" +
              "1, 2, 3, 4, 5, ['HS1 2AB', 'HS9 5XD'], [1, 1000]" +
              ") --> ", end="")
        housePrices.writeSummary(1, 2, 3, 4, 5, ['HS1 2AB', 'HS9 5XD'], [1, 1000])
        print("Written")
                     
        print("\nCompleted: writeSummary()")
        print("=========================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: writeSummary()")
        print("===================\n")
        
        return 0


def testWriteData() -> int:
    """Tests the writeData() function"""
    
    print("\nwriteData() Tests")
    print("-----------------\n")
    
    try:
        
        print("Test: writeData(" +
              "['HS1 2AB', 'HS9 5XD'], [1, 1000], [2, 2000]" +
              ") --> ", end="")
        housePrices.writeData(['HS1 2AB', 'HS9 5XD'], [1, 1000], [2, 2000])
        print("Written")
                     
        print("\nCompleted: writeData()")
        print("======================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: writeData()")
        print("===================\n")
        
        return 0


def testAll() -> None:
    """Tests all functions"""
    
    # Local variable
    passed: int = 0
    
    print("\nRun All Tests")
    print("-------------\n")
    
    try:
        
        passed += testReadData()
        passed += testCountHS0()
        passed += testFixHS0()
        passed += testNewPrices()
        passed += testFindLowest()
        passed += testFindHighest()
        passed += testCountValues()
        passed += testWriteSummary()
        passed += testWriteData()
        
        if passed == 9:
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
test: str = ""
run: bool = True

while run:
    print("\nhousePrices Tests")
    print("--------------\n")

    print("1. readData()")
    print("2. countHS0()")
    print("3. fixHS0()")
    print("4. newPrices()")
    print("5. findLowest()")
    print("6. findHighest()")
    print("7. countValues()")
    print("8. writeSummary()")
    print("9. writeData()")
    
    print("\na. All tests")
    print("x. Exit")

    # Get text value from user
    test = input("\nTest: ")

    if test == "1":
        testReadData()
        
    elif test == "2":
        testCountHS0()
        
    elif test == "3":
        testFixHS0()
        
    elif test == "4":
        testNewPrices()
        
    elif test == "5":
        testFindLowest()
        
    elif test == "6":
        testFindHighest()
        
    elif test == "7":
        testCountValues()
        
    elif test == "8":
        testWriteSummary()
        
    elif test == "9":
        testWriteData()
             
    elif test == "a":
        # Run all tests
        testAll()
        
    elif test == "x":
        # Exit tests
        run = False
