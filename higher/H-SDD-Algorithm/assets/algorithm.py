# Title: H-SDD-Algorithm
# Author: Mr Friend
# Date: 20 Sep 2024

def findItem(items, target):
    """Linear search.  Returns index position or -1"""
    
    # Initialise local variables
    found = False
    index = 0
    
    # Loop until found or end of list
    while not found and index < len(items):
        
        # Compare
        if items[index] == target:
            # Update flag
            found = True
            
        else:
            # Increment index
            index = index + 1

    if not found:
        index = -1
    
    return index


def countItem(items, target):
    """Count occurrences.  Returns count."""
    
    # Initialise local variables
    count = 0
    
    # Loop until end of list
    for index in range(len(items)):
        
        # Compare
        if items[index] == target:
            # Increment count
            count = count + 1
   
    return count


def findMax(items):
    """Find maximum.  Returns maximum value."""
    
    # Initialise local variables
    max = items[0]
    
    # Loop until end of list
    for index in range(1, len(items)):
        
        # Compare
        if items[index] > max:
            # Update max
            max = items[index]
   
    return max


def findMin(items):
    """Find minimum.  Returns minimum value."""
    
    # Initialise local variables
    min = items[0]
    
    # Loop until end of list
    for index in range(1, len(items)):
        
        # Compare
        if items[index] < min:
            # Update min
            min = items[index]
   
    return min
