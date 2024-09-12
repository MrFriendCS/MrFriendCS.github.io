# Title: H SDD Substrings
# Author: Mr Friend
# Date: 12 Sep 2024

def left(text, count):
    """Creates a substring, counting from the left."""
    
    # Local variable
    subString = ""
    
    if count < len(text) and count > 0:
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
    
    if count < len(text) and count > 0:
        # Extract substring
        subString = text[-count: ]
    else:
        subString = text

    # Return substring
    return subString


def mid(text, start, count):
    """Creates a substring, counting from the right."""
    
    # Local variable
    subString = ""
    
    if count < len(text) and count > 0:
        # Extract substring
        subString = text[start-1:start+count-1]
    else:
        subString = text

    # Return substring
    return subString

