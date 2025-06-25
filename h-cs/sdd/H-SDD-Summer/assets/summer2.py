# Title: H-SDD-Summer Part 2
# Author: Mr Friend
# Date: 25 Jun 2025

#
# Sub-programs
#


def reverse(text):
    """Returns the characters in reverse order."""
    
    # Initialise local variable
    output = ""
    
    # Loop for each characters
    for letter in text:
        
        # Add character to begining
        output = letter + output
        
    # Return reveresed string
    return output


def makeUsername(name):
    """Create and return a username."""
    
    # Get extra code
    import random
    
    # Initialise local variables
    substring = ""
    ascii = 0
    number = 0
    letter = ""
    username = "es"
    
    # Check if name is valid
    if len(name) > 2:
        
        # Get substring
        if len(name) >= 4:
            
            # Use first 4 letters
            substring = name[ :4]
        
        else:
            
            # Use all letters
            substring = name
            
        # Loop for each letter in substring
        for index in range(len(substring)):
            
            # Get ASCII value of current letter
            ascii = ord(substring[index])
            
            # Lower case?
            if ascii < 97:
                
                # Add lowercase letter to username
                username = username + chr(ascii + 32)
            
            else:
                
                # Add letter to username
                username = username + chr(ascii)
        
        # Add random number
        username = username + str(random.randint(1, 9))
        
        # Add random letter
        username = username + chr(random.randint(97, 122))
    
    else:
        
        # Set username to error value
        username = "invalid"
    
    # Return circumference
    return username
