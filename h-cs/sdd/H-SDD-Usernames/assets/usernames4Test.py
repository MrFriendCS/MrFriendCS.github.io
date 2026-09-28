# Title: H SDD - Usernames Part 4 - Tests
# Author: Mr Friend
# Date: 27 Sep 2026

"""Tests the functions in usernames4.py"""

from usernames4 import *


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
        assert len(readData()) == 100
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": First value --> ", end="")
        assert type(readData()[0].firstName) == type("str")
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Last value --> ", end="")
        assert type(readData()[-1].firstName) == type("str")
        print("Passed")
       
        print("\nPASSED: readData()")
        print("==================\n")
        
        return 1
        
    except:
        
        print("\nFAILED: readData()")
        print("==================\n")
        
        return 0


def testleft() -> int:
    """Tests the left() function"""
    
    # Local variables
    test: int = 1
    inputs1: list[str]
    inputs2: list[int]
    outputs: list[str]
    
    # Values
    inputs1 = ['Hello', 'Hello', 'Hello']
    inputs2 = [1, 2, 4]
    outputs = ['H', 'He', 'Hell']
    
    print("\nleft() Tests")
    print("------------\n")
    
    try:
        
        for index in range(len(inputs1)):
            
            print(f'Test {test}: left("{inputs1[index]}", {inputs2[index]}) --> ', end="")
            
            assert left(inputs1[index], inputs2[index]) == outputs[index]
            
            print("Passed")
            
            test += 1
               
        print("\nPASSED: left()")
        print("==============\n")
        
        return 1
        
    except:
        
        print("Failed")
        print("\nFAILED: left()")
        print("==============\n")
        
        return 0
  

def testRight() -> int:
    """Tests the right() function"""
    
    # Local variables
    test: int = 1
    inputs1: list[str]
    inputs2: list[int]
    outputs: list[str]
    
    # Values
    inputs1 = ['Hello', 'Hello', 'Hello']
    inputs2 = [1, 2, 4]
    outputs = ['o', 'lo', 'ello']
    
    print("\nleft() Tests")
    print("------------\n")
    
    try:
        
        for index in range(len(inputs1)):
            
            print(f'Test {test}: right("{inputs1[index]}", {inputs2[index]}) --> ', end="")
            
            assert right(inputs1[index], inputs2[index]) == outputs[index]
            
            print("Passed")
            
            test += 1
               
        print("\nPASSED: right()")
        print("===============\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: right()")
        print("===============\n")
        
        return 0
    
    
def testMid() -> int:
    """Tests the mid() function"""
    
    # Local variables
    test: int = 1
    inputs1: list[str]
    inputs2: list[int]
    inputs3: list[int]
    outputs: list[str]
    
    # Values
    inputs1 = ['Hello world!', 'Hello world!', 'Hello world!']
    inputs2 = [2, 4, 7]
    inputs3 = [4, 5, 3]
    outputs = ['ello', 'lo wo', 'wor']
    
    print("\nmid() Tests")
    print("-----------\n")
    
    try:
        
        for index in range(len(inputs1)):
            
            print(f'Test {test}: mid("{inputs1[index]}", {inputs2[index]}, {inputs3[index]}) --> ', end="")
            
            assert mid(inputs1[index], inputs2[index], inputs3[index]) == outputs[index]
            
            print("Passed")
            
            test += 1
               
        print("\nPASSED: mid()")
        print("=============\n")
        
        return 1
    
    except:
        print("Failed")
        print("\nFAILED: mid()")
        print("=============\n")
        
        return 0


def testLower() -> int:
    """Tests the lower() function"""
    
    # Local variables
    test: int = 1
    inputs: list[str]
    outputs: list[str]
    
    # Values
    inputs = ['CAT', 'cat', '1CAT2', '.cat,']
    outputs = ['cat', 'cat', '1cat2', '.cat,']
    
    print("\nlower() Tests")
    print("-------------\n")
    
    try:
        
        for index in range(len(inputs)):
            
            print(f'Test {test}: lower("{inputs[index]}") --> ', end="")
            
            assert lower(inputs[index]) == outputs[index]
            
            print("Passed")
            
            test += 1
               
        print("\nPASSED: lower()")
        print("===============\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: lower()")
        print("===============\n")
        
        return 0
    

def testCreateUsernames() -> int:
    """Tests the createUsernames() function"""
    
    # Local variables
    test: int = 1
    first: list[str]
    last: list[str]
    ni: list[str]
    outputs: list[str]
    student: Student
    
    # Values
    first = ["Barbra", "Jeth" , "Earl"]
    last = ["Newhouse", "Grewcock", "Vasiljevic"]
    ni = ["ZQ018158G", "LU962093W", "XQ961836I"]
    outputs = ["baruse181", "jetock620", "earvic618"]
    
    print("\ncreateUsernames() Tests")
    print("-----------------------\n")
    
    try:
        
        for index in range(len(first)):
            
            student = Student(first[index], last[index], ni[index])
            
            print(f'Test {test}: createUsernames([{student}]) --> ', end="")
            
            assert createUsernames([student]) == [outputs[index]]
            
            print("Passed")
            
            test += 1
               
        print("\nPASSED: createUsernames()")
        print("=========================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: createUsernames()")
        print("=====================\n")
        
        return 0


def testWriteData() -> int:
    """Tests the writeData() function"""
    
    # Local variables
    test: int = 1
    inputs: list[str]
    
    # Values
    inputs = ["baruse181", "jetock620", "earvic618"]
    
    print("\nwriteData() Tests")
    print("-----------------\n")
    
    try:
        
        print(f"Test {test}: writeData(" +
              '["baruse181", "jetock620", "earvic618"]' +
              ") --> ", end="")
        
        writeData(inputs)
        
        print("Written")
        
        test += 1
        
        # Connect to file
        print(f"Test {test}: connect to file --> ", end="")
        
        file = open("usernames.txt", "r", encoding="utf-8")
        
        print("Passed")
        
        test += 1
        
        # Loop for each line
        for index in range(len(inputs)):
            
            print(f"Test {test}: readline() --> ", end="")
            
            assert file.readline().strip() == inputs[index]
            
            print("Passed")
            
            test += 1
            
                     
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
        passed += testleft()
        passed += testRight()
        passed += testMid()
        passed += testLower()
        passed += testCreateUsernames()
        passed += testWriteData()
        
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
test: str = ""
run: bool = True

while run:
    print("\nusernames4 Tests")
    print("--------------\n")

    print("1. readData()")
    print("2. left()")
    print("3. right()")
    print("4. mid()")
    print("5. lower()")
    print("6. createUsernames()")
    print("7. writeData()")
    
    print("\na. All tests")
    print("x. Exit")

    # Get text value from user
    test = input("\nTest: ")

    if test == "1":
        testReadData()
        
    elif test == "2":
        testleft()
        
    elif test == "3":
        testRight()
        
    elif test == "4":
        testMid()
        
    elif test == "5":
        testLower()
        
    elif test == "6":
        testCreateUsernames()
        
    elif test == "7":
        testWriteData()
             
    elif test == "a":
        # Run all tests
        testAll()
        
    elif test == "x":
        # Exit tests
        run = False
