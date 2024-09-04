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
        
        print("Test: Lower case, simple shift")
        assert caesar.encode("abc", 3) == "def"
        print("Passed")
        
        
        print("\nTest: Lower case, wrap alphabet")
        assert caesar.encode("xyz", 3) == "abc"
        print("Passed")
        
        print("\nTest: Lower case with symbols")
        assert caesar.encode("!a b-c,", 3) == "def"
        print("Passed")

        
        print("\nTest: Upper case, simple shift")
        assert caesar.encode("ABC", 3) == "def"
        print("Passed")


        print("\nTest: Upper case, wrap alphabet")
        assert caesar.encode("XYZ", 3) == "abc"
        print("Passed")


        print("\nTest: Upper case with symbols")
        assert caesar.encode("!A B-C,", 3) == "def"
        print("Passed")
        
        print("\nTest: Lower case, shift > 26")
        assert caesar.encode("abc", 55) == "def"
        print("Passed")
        
        print("\nTest: Upper case, shift > 26")
        assert caesar.encode("ABC", 55) == "def"
        print("Passed")
                
        print("\nAll tests passed!")
        print("=================")
        
    except:
        print("FAILED")
        print("\nTesting ended")
        print("=============")

#
# Main program
#

print("Test Caesar Cipher Tests")
print("------------------------")

print("\n1. Encode test")
print("2. Decode test")

if input("\nEnter 1 or 2: ") == "1":
    # Encode test
    testEncode()
else:
    print("\nNo decode tests available, yet")
