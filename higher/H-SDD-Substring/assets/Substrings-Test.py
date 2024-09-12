# Title: H-SDD-Substring-Tests
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
              ": 'Hello!', 4 --> ", end="")
        assert substring.left("Hello!", 4) == "Hell"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": '12345', 3 --> ", end="")
        assert substring.left("12345", 3) == "123"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": '£1.26p', 5 --> ", end="")
        assert substring.left("£1.26p", 5) == "£1.26"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 'Hello!', -1 --> ", end="")
        assert substring.left("Hello!", -1) == "Hello!"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": '', 4 --> ", end="")
        assert substring.left("", 4) == ""
        print("Passed")
                     
        print("\nPASSED: left()")
        print("==============\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: left()")
        print("==============\n")
        
        return 0


def testRight():
    """Tests the right() function"""
    
    # Local variable
    test = 1
    
    print("\nright() Tests")
    print("-------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 'Hello!', 5 --> ", end="")
        assert substring.right("Hello!", 5) == "ello!"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": '12345', 3 --> ", end="")
        assert substring.right("12345", 3) == "345"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": '£1.26p', 3 --> ", end="")
        assert substring.right("£1.26p", 3) == "26p"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 'Hello!', -1 --> ", end="")
        assert substring.right("Hello!", -1) == "Hello!"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": '', 4 --> ", end="")
        assert substring.right("", 4) == ""
        print("Passed")
                     
        print("\nPASSED: right()")
        print("===============\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: right()")
        print("===============\n")
        
        return 0


def testMid():
    """Tests the mid() function"""
    
    # Local variable
    test = 1
    
    print("\nmid() Tests")
    print("-----------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 'Hello world!', 4, 5 --> ", end="")
        assert substring.mid("Hello world!", 4, 5) == "lo wo"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": '12345', 2, 3 --> ", end="")
        assert substring.mid("12345", 2, 3) == "234"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": '£1.26p', 2, 3 --> ", end="")
        assert substring.mid("£1.26p", 2, 3) == "1.2"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 'Hello!', -1, 2 --> ", end="")
        assert substring.mid("Hello!", -1, 2) == "Hello!"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 'Hello!', 3, -1 --> ", end="")
        assert substring.mid("Hello!", 3, -1) == "Hello!"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": '', 4 --> ", end="")
        assert substring.mid("", 4, 2) == ""
        print("Passed")
                
        print("\nPASSED: mid()")
        print("=============\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: mid()")
        print("=============\n")
        
        return 0


def testLower():
    """Tests the lower() function"""
    
    # Local variable
    test = 1
    
    print("\nlower() Tests")
    print("-------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 'Hello!' --> ", end="")
        assert substring.lower("Hello!") == "hello!"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": '12 34' --> ", end="")
        assert substring.lower("12 34") == "12 34"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": '£1.26p' --> ", end="")
        assert substring.lower("£1.26p") == "£1.26p"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 'AB-cd-wx-YZ' --> ", end="")
        assert substring.lower("AB-cd-wx-YZ") == "ab-cd-wx-yz"
        print("Passed")
                
        print("\nPASSED: lower()")
        print("===============\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: lower()")
        print("===============\n")
        
        return 0


def testUpper():
    """Tests the upper() function"""
    
    # Local variable
    test = 1
    
    print("\nupper() Tests")
    print("-------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 'Hello!' --> ", end="")
        assert substring.upper("Hello!") == "HELLO!"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": '12 34' --> ", end="")
        assert substring.upper("12 34") == "12 34"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": '£1.26p' --> ", end="")
        assert substring.upper("£1.26p") == "£1.26P"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 'ab-CD-WX-yza' --> ", end="")
        assert substring.upper("ab-CD-WX-yz") == "AB-CD-WX-YZ"
        print("Passed")
                
        print("\nPASSED: upper()")
        print("===============\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: upper()")
        print("===============\n")
        
        return 0
        

def testReverse():
    """Tests the reverse() function"""
    
    # Local variable
    test = 1
    
    print("\nreverse() Tests")
    print("---------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 'Hello!' --> ", end="")
        assert substring.reverse("Hello!") == "!olleH"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": '12 34' --> ", end="")
        assert substring.reverse("12 34") == "43 21"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": '£1.26p' --> ", end="")
        assert substring.reverse("£1.26p") == "p62.1£"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 'AB-cd-wx-YZ' --> ", end="")
        assert substring.reverse("AB-cd-wx-YZ") == "ZY-xw-dc-BA"
        print("Passed")
                
        print("\nPASSED: reverse()")
        print("=================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: reverse()")
        print("=================\n")
        
        return 0


def testSwap():
    """Tests the swap() function"""
    
    # Local variable
    test = 1
    
    print("\nswap() Tests")
    print("------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 'Hello!' --> ", end="")
        assert substring.swap("Hello!") == "hELLO!"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": '12 34' --> ", end="")
        assert substring.swap("12 34") == "12 34"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": '£1.26p' --> ", end="")
        assert substring.swap("£1.26p") == "£1.26P"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 'AB-cd-wx-YZ' --> ", end="")
        assert substring.swap("AB-cd-wx-YZ") == "ab-CD-WX-yz"
        print("Passed")
                
        print("\nPASSED: swap()")
        print("==============\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: swap()")
        print("==============\n")
        
        return 0
        

def testRemove():
    """Tests the remove() function"""
    
    # Local variable
    test = 1
    
    print("\nremove() Tests")
    print("--------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": 'Hello!' --> ", end="")
        assert substring.remove("Hello!") == "Hello"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": '12 34' --> ", end="")
        assert substring.remove("12 34") == ""
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": '£1.26p' --> ", end="")
        assert substring.remove("£1.26p") == "p"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": 'AB-cd-wx-YZ' --> ", end="")
        assert substring.remove("AB-cd-wx-YZ") == "ABcdwxYZ"
        print("Passed")
                
        print("\nPASSED: remove()")
        print("================\n")
        
        return 1
        
    except:
        print("Failed")
        print("\nFAILED: remove()")
        print("================\n")
        
        return 0


def testAll():
    """Tests all functions"""
    
    # Local variable
    passed = 0
    
    print("\nRun All Tests")
    print("--------------\n")
    
    try:
        
        passed += testLeft()
        passed += testRight()
        passed += testMid()
        passed += testLower()
        passed += testUpper()
        passed += testReverse()
        passed += testSwap()
        passed += testRemove()
        
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
        # 
        testLeft()
        
    elif test == "2":
        # 
        testRight()
        
    elif test == "3":
        # 
        testMid()
        
    elif test == "4":
        # 
        testLower()
        
    elif test == "5":
        # 
        testUpper()
        
    elif test == "6":
        # 
        testReverse()
        
    elif test == "7":
        # 
        testSwap()
        
    elif test == "8":
        # 
        testRemove()
        
    elif test == "a":
        # Run all tests
        testAll()
        
    elif test == "x":
        # Exit tests
        run = False
