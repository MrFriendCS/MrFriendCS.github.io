# Title: H SDD Caesar Cipher
# Author: Mr Friend
# Date: 5 Sep 2024


def encode(plainText, shift):
    """Shift cipher.  Creates cipher text."""
    
    # Initialise local variables
    ascii = 0
    cipherText = ""
    
    # Ensure key is 0 to 26
    shift = shift % 26
    
    # Loop for each letter in message
    for index in range(len(plainText)):
        
        # Get ASCII value
        ascii = ord(plainText[index])
        
        # Is ASCII value 65 to 90?
        if ascii >= 65 and ascii <= 90:
            
            ascii = ascii + 32
            
        # Is ASCII value 97 to 122?
        if ascii >= 97 and ascii <= 122:
            
            # Add key value to ASCII value
            ascii = ascii + shift
            
            # Is ascii > 122?
            if ascii > 122:
                
                ascii = ascii - 26
            
            # Add ASCII character to cipher text
            cipherText = cipherText + chr(ascii)
    
    return cipherText


def decode(cipherText, shift):
    """Shift cipher.  Creates plain text."""
    
    # Initialise local variables
    ascii = 0
    lowerCase = False
    plainText = ""
    
    # Ensure key is 0 to 26
    shift = shift % 26
    
    # Loop for each letter in message
    for index in range(len(cipherText)):
        
        # Reset variable
        lowerCase = False
        
        # Get ASCII value
        ascii = ord(cipherText[index])
        
        # Is ASCII value 97-122?
        if ascii >= 97 and ascii <= 122:
            # Set lower case
            lowerCase = True
        
        # Is ASCII value 65-90 or 97-122?
        if (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122):
        
            # Subtract shift value from ASCII value
            ascii = ascii - shift
        
            # Is ASCII value < 65?
            if ascii < 65:
                # Add 26 to ASCII value
                ascii = ascii + 26
            # Is ASCII value < 97?
            elif lowerCase and ascii < 97:
                # Add 26 to ASCII value
                ascii = ascii + 26
        
        # Add ASCII character to plain text
        plainText = plainText + chr(ascii)
    
    # Return plain text
    return plainText
