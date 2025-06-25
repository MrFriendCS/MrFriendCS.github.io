# Title: H-SDD-Summer Part 3
# Author: Mr Friend
# Date: 25 Jun 2025

#
# Sub-programs
#


def contains(text, target):
    """Returns True if character found in text."""
    
    # Initialise local variables
    found = False
    index = 0
    ascii = 0
    letter = ""
    
    # Ensure target is uppercase
    
    # Get ASCII value
    ascii = ord(target)
    
    # check target ASCII value
    if ascii > 97 and ascii < 122:
        
        # convert target to uppercase
        target = chr(ascii - 32)
    
    # Loop until target found or reached end of string
    while not found and index < len(text):
        
        # Get current character
        letter = text[index]
        
        # Ensure current letter is uppercase
    
        # Get ASCII value
        ascii = ord(letter)
        
        # check letter ASCII value
        if ascii > 97 and ascii < 122:
            
            # convert letter to uppercase
            letter = chr(ascii - 32)
        
        # Check if current letter is matches the target
        if letter == target:
            
            # Update flag
            found = True
        
        else:
            
            # Increment index
            index = index + 1
            
    # Return result
    return found  


def letterTypes(text):
    """Returns the number of uppercase and lowercase characters."""
    
    # Initialise local variables
    ascii = 0
    uppercase = 0
    lowercase = 0
    
    # Loop for each characters
    for letter in text:
        
        # Get ASCII value of current character
        ascii = ord(letter)
        
        if ascii >= 65 and ascii <= 90:
            
            # Increment uppercase
            uppercase = uppercase + 1
            
        elif ascii >= 97 and ascii <= 122:
            
            # Increment uppercase
            lowercase = lowercase + 1
    
    # Return counts
    return uppercase, lowercase
       