# Title: Caesar Cipher Tests
# Author: Mr Friend
# Date: 4 Sep 2024

"""Tests the functions in caesar.py"""

import caesar


def testEncode():
    """Tests the encode() function"""
    
    # Local variable
    test = 1
    
    print("\nEncode Tests")
    print("------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": Lower case, small shift: ", end="")
        assert caesar.encode("abcd", 1) == "bcde"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Lower case, small wrap: ", end="")
        assert caesar.encode("wxyz", 1) == "xyza"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Lower case, big shift: ", end="")
        assert caesar.encode("abcd", 25) == "zabc"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Lower case, big wrap: ", end="")
        assert caesar.encode("wxyz", 25) == "vwxy"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Lower case, symbols: ", end="")
        assert caesar.encode("!a b-c,", 3) == "def"
        print("Passed")
        
        test += 11
        print("Test " + str(test) +
              ": Upper case, small shift: ", end="")
        assert caesar.encode("ABCD", 1) == "bcde"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Upper case, small wrap: ", end="")
        assert caesar.encode("WXYZ", 1) == "xyza"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Upper case, big shift: ", end="")
        assert caesar.encode("ABCD", 25) == "zabc"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Upper case, big wrap: ", end="")
        assert caesar.encode("WXYZ", 25) == "vwxy"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Upper case, symbols: ", end="")
        assert caesar.encode("!A B-C,", 3) == "def"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Lower case, shift > 26: ", end="")
        assert caesar.encode("abcd", 55) == "defg"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Upper case, shift > 26: ", end="")
        assert caesar.encode("ABCD", 55) == "defg"
        print("Passed")
                
        print("\nAll encode tests passed!")
        print("========================\n")
        
    except:
        print("FAILED")
        print("\nEncode testing ended")
        print("=================1===\n")


def testDecode():
    """Tests the decode() function"""
    
    # Local variable
    test = 1
    
    print("\nDecode Tests")
    print("------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": Lower case, small shift: ", end="")
        assert caesar.decode("bcde", 1) == "abcd"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Lower case, small wrap: ", end="")
        assert caesar.decode("xyza", 1) == "wxyz"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Lower case, big shift: ", end="")
        assert caesar.decode("zabc", 25) == "abcd"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Lower case, big wrap: ", end="")
        assert caesar.decode("vwxy", 25) == "wxyz"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Lower case, symbols: ", end="")
        assert caesar.decode("!D E-F,", 3) == "!A B-C,"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Upper case, small shift: ", end="")
        assert caesar.decode("BCDE", 1) == "ABCD"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Upper case, small wrap: ", end="")
        assert caesar.decode("XYZA", 1) == "WXYZ"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Upper case, big shift: ", end="")
        assert caesar.decode("ZABC", 25) == "ABCD"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Upper case, big wrap: ", end="")
        assert caesar.decode("VWXY", 25) == "WXYZ"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Upper case, symbols: ", end="")
        assert caesar.decode("!D E-F,", 3) == "!A B-C,"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Lower case, shift > 26: ", end="")
        assert caesar.decode("defg", 55) == "abcd"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Upper case, shift > 26: ", end="")
        assert caesar.decode("DEFG", 55) == "ABCD"
        print("Passed")
                
        print("\nAll decode tests passed!")
        print("========================\n")
        
    except:
        print("FAILED")
        print("\nDecode testing ended")
        print("====================\n")


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

