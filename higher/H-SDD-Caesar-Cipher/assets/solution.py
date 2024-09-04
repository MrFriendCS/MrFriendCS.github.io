# Title: H SDD Caesar Cipher
# Author: Mr Friend
# Date: 4 Sep 2024


def encode(plainText, key):
    """Shift cipher.  Creates cipher text."""
    # Initialise local variables
    ascii = 0
    cipherText = ""
    
    # Loop for each letter in message
    for index in range(len(plainText)):
        
        # Get ASCII value
        ascii = ord(plainText[index])
        
        # Is ASCII value 65 to 90?
        if ascii >= 65 and ascii <= 90:
            
            ascii = ascii + 32
            
        # Is ASCII value 95 to 122?
        if ascii >= 95 and ascii <= 122:
            
            # Add key value to ASCII value
            ascii = ascii + key
            
            # Is ascii > 122?
            if ascii > 122:
                
                ascii = ascii - 26
            
            # Add ASCII character to cipher text
            cipherText = cipherText + chr(ascii)
    
    return cipherText


#
# Main program
#

print(encode("Hello!", 1))

print(encode("abc XYZ",3))
