# Title: H-SDD-Substrings
# Author: Mr Friend
# Date: 12 Jun 2025

def left(text, count):
    """Creates a substring, counting from the left.  Returns the substring."""
    
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
    """Creates a substring, counting from the right.  Returns the substring."""
    
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
    """Creates a substring, starting at a position, counting from the left.  Returns the substring."""
    
    # Local variable
    subString = ""
    
    if start > 0 and count > 0 and start+count <= len(text):
        # Extract substring
        subString = text[start-1:start+count-1]
    else:
        subString = text

    # Return substring
    return subString
