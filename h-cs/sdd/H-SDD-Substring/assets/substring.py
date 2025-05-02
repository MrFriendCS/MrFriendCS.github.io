# Title: H-SDD-Substrings
# Author: Mr Friend
# Date: 12 Sep 2024

def left(text, count):
    """Creates a substring, counting from the left."""
    
    # Local variable
    subString = ""
    
    if count > 0 and count < len(text):
        # Extract substring
        subString = text[ :count]
    else:
        subString = text

    # Return substring
    return subString


def right(text, count):
    """Creates a substring, counting from the right."""
    
    # Local variable
    subString = ""
    
    if count > 0 and count < len(text):
        # Extract substring
        subString = text[-count: ]
    else:
        subString = text

    # Return substring
    return subString


def mid(text, start, count):
    """Creates a substring, starting at a position, counting from the left."""
    
    # Local variable
    subString = ""
    
    if start > 0 and count > 0 and start+count <= len(text):
        # Extract substring
        subString = text[start-1:start+count-1]
    else:
        subString = text

    # Return substring
    return subString


def lower(text):
    """Creates a lowercase string."""
    
    # Local variables
    ascii = 0
    newText = ""
    
    # Loop for each character
    for index in range(len(text)):
        
        # Get ASCII value of character
        ascii = ord(text[index])
        
        # Check if uppercase
        if ascii >= 65 and ascii <= 90:
            # Convert to lowercase
            ascii = ascii + 32
        
        # Add character to text
        newText = newText + chr(ascii)
    
    # Return lowercase version
    return newText


def upper(text):
    """Creates an uppercase string."""
    
    # Local variables
    ascii = 0
    newText = ""
    
    # Loop for each character
    for index in range(len(text)):
        
        # Get ASCII value of character
        ascii = ord(text[index])
        
        # Check if lowercase
        if ascii >= 97 and ascii <= 122:
            # Convert to uppercase
            ascii = ascii - 32
        
        # Add character to text
        newText = newText + chr(ascii)
    
    # Return uppercase version
    return newText


def reverse(text):
    """Creates a reveresed string."""
    
    # Local variables
    newText = ""
    
    # Loop for each character
    for index in range(len(text)):
        
        # Add character to text
        newText = text[index] + newText
    
    # Return reversed version
    return newText


def swap(text):
    """Swaps uppercase characters for lowercase once, and vice-versa."""
    
    # Local variables
    ascii = 0
    newText = ""
    
    # Loop for each character
    for index in range(len(text)):
        
        # Get ASCII value of character
        ascii = ord(text[index])
        
        # Check if uppercase
        if ascii >= 65 and ascii <= 90:
            # Convert to lowercase
            ascii = ascii + 32
            
        # Check if lowercase
        elif ascii >=97 and ascii <=122:
            # Convert to uppercase
            ascii = ascii - 32

        # Add character to text
        newText = newText + chr(ascii)
    
    # Return modified version
    return newText


def remove(text):
    """Removes none uppercase and none lowercase characters."""
    
    # Local variables
    ascii = 0
    newText = ""
    
    # Loop for each character
    for index in range(len(text)):
        
        # Get ASCII value of character
        ascii = ord(text[index])
        
        # Check if uppercase
        if ascii >= 65 and ascii <= 90:
            
            # Add character to text
            newText = newText + chr(ascii)
            
        # Check if lowercase
        elif ascii >=97 and ascii <=122:
            
            # Add character to text
            newText = newText + chr(ascii)
    
    # Return modified version
    return newText
