# Title: Caesar Cipher Tests
# Author: Mr Friend
# Date: 4 Sep 2024

"""Tests the functions in caesar.py"""

import caesar


def testEncode():
    """Tests the encode() function"""
    
    print("\nEncode Tests")
    print("------------\n")
    
    try:
        
        print("Test: Lower case, simple shift: ", end="")
        assert caesar.encode("abc", 3) == "def"
        print("Passed")
        
        
        print("Test: Lower case, wrap alphabet: ", end="")
        assert caesar.encode("xyz", 3) == "abc"
        print("Passed")
        
        print("Test: Lower case with symbols: ", end="")
        assert caesar.encode("!a b-c,", 3) == "def"
        print("Passed")

        
        print("Test: Upper case, simple shift: ", end="")
        assert caesar.encode("ABC", 3) == "def"
        print("Passed")


        print("Test: Upper case, wrap alphabet: ", end="")
        assert caesar.encode("XYZ", 3) == "abc"
        print("Passed")


        print("Test: Upper case with symbols: ", end="")
        assert caesar.encode("!A B-C,", 3) == "def"
        print("Passed")
        
        print("Test: Lower case, shift > 26: ", end="")
        assert caesar.encode("abc", 55) == "def"
        print("Passed")
        
        print("Test: Upper case, shift > 26: ", end="")
        assert caesar.encode("ABC", 55) == "def"
        print("Passed")
                
        print("\nAll tests passed!")
        print("=================\n")
        
    except:
        print("FAILED")
        print("\nTesting ended")
        print("=============\n")


def testDecode():
    """Tests the decode() function"""
    
    print("\nDecode Tests")
    print("------------\n")
    
    try:
        
        print("Test: Lower case, simple shift: ", end="")
        assert caesar.decode("def", 3) == "abc"
        print("Passed")
        
        
        print("Test: Lower case, wrap alphabet: ", end="")
        assert caesar.decode("abc", 3) == "xyz"
        print("Passed")
        
        print("Test: Lower case with symbols: ", end="")
        assert caesar.decode("!D E-F,", 3) == "!A B-C,"
        print("Passed")

        
        print("Test: Upper case, simple shift: ", end="")
        assert caesar.decode("DEF", 3) == "ABC"
        print("Passed")


        print("Test: Upper case, wrap alphabet: ", end="")
        assert caesar.decode("ABC", 3) == "XYZ"
        print("Passed")


        print("Test: Upper case with symbols: ", end="")
        assert caesar.decode("!D E-F,", 3) == "!A B-C,"
        print("Passed")
        
        print("Test: Lower case, shift > 26: ", end="")
        assert caesar.decode("def", 55) == "abc"
        print("Passed")
        
        print("Test: Upper case, shift > 26: ", end="")
        assert caesar.decode("DEF", 55) == "ABC"
        print("Passed")
                
        print("\nAll tests passed!")
        print("=================\n")
        
    except:
        print("FAILED")
        print("\nTesting ended")
        print("=============\n")


#
# Main program
#

# Initialise global variables
test = ""
run = True

while run:
    print("\nCaesar Cipher Tests")
    print("-------------------")

    print("\n1. Encode tests")
    print("2. Decode tests")
    print("x. Exit")

    # Get text value from user
    test = input("\nTest: ")

    if test == "1":
        # Encode test
        testEncode()
    elif test == "2":
        # Decode test
        testDecode()
    elif test == "x":
        # Exit tests
        run = False
