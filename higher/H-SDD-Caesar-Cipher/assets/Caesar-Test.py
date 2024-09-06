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
              ": Lower case, simple shift: ", end="")
        assert caesar.encode("abcd", 2) == "cdef"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Lower case, wrap alphabet: ", end="")
        assert caesar.encode("wxyz", 2) == "yzab"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Lower case, big shift: ", end="")
        assert caesar.encode("abcd", 24) == "yzab"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Lower case, wrap alphabet, big shift: ", end="")
        assert caesar.encode("wxyz", 24) == "uvwx"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Lower case with symbols: ", end="")
        assert caesar.encode("!a b-c,", 3) == "def"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Upper case, simple shift: ", end="")
        assert caesar.encode("ABCD", 2) == "cdef"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Upper case, wrap alphabet: ", end="")
        assert caesar.encode("WXYZ", 2) == "yzab"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Upper case, big shift: ", end="")
        assert caesar.encode("ABCD", 24) == "yzab"
        print("Passed")
        
        test += 1 
        print("Test " + str(test) +
              ": Upper case, wrap alphabet, big shift: ", end="")
        assert caesar.encode("WXYZ", 24) == "uvwx"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Upper case with symbols: ", end="")
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
                
        print("\nAll tests passed!")
        print("=================\n")
        
    except:
        print("FAILED")
        print("\nTesting ended")
        print("=============\n")


def testDecode():
    """Tests the decode() function"""
    
    # Local variable
    test = 1
    
    print("\nDecode Tests")
    print("------------\n")
    
    try:
        
        print("Test " + str(test) +
              ": Lower case, simple shift: ", end="")
        assert caesar.decode("cdef", 2) == "abcd"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Lower case, wrap alphabet: ", end="")
        assert caesar.decode("abcd", 2) == "yzab"
        print("Passed")
        
        print("Test " + str(test) +
              ": Lower case, big shift: ", end="")
        assert caesar.decode("yzab", 24) == "abcd"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Lower case, wrap alphabet, big shift: ", end="")
        assert caesar.decode("uvwx", 24) == "wxyz"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Lower case with symbols: ", end="")
        assert caesar.decode("!D E-F,", 3) == "!A B-C,"
        print("Passed")

        test += 1
        print("Test " + str(test) +
              ": Upper case, simple shift: ", end="")
        assert caesar.decode("CDEF", 2) == "ABCD"
        print("Passed")

        test += 1
        print("Test " + str(test) +
              ": Upper case, wrap alphabet: ", end="")
        assert caesar.decode("ABCD", 2) == "YZAB"
        print("Passed")

        test += 1
        print("Test " + str(test) +
              ": Upper case, big shift: ", end="")
        assert caesar.decode("WXYZ", 24) == "YZAB"
        print("Passed")

        test += 1
        print("Test " + str(test) +
              ": Upper case, wrap alphabet, big: ", end="")
        assert caesar.decode("ABCD", 24) == "CDEF"
        print("Passed")
        
        test += 1
        print("Test " + str(test) +
              ": Upper case with symbols: ", end="")
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
