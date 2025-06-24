# Title: H-SDD-Standard Algorithms
# Author: Mr Friend
# Date: 24 Jun 2025

#
# Sub-programs
#

def search(values, target):
    """Linear search.  Returns True if target value is in list of values, otherwise returns False."""
    
    # Local variables
    found = False
    index = 0
    
    # Loop until target found, or last value checked
    while not found and index < len(values):
        
        # Check current value and target
        if values[index] == target:
            
            # Change flag
            found = True
            
        else:
            
            # Increment index
            index = index + 1
    
    # Return result
    return found


def findMin(values):
    """Returns the smallest value from an array of values."""
    
    # Local variable
    minimum = values[0]
    
    # Loop from second element for each value in array
    for index in range(1, len(values)):
        
        # Check current value is less than current minimum
        if values[index] < minimum:
            
            # Update minimum
            minimum = values[index]
    
    # Return smallest
    return minimum


def findMax(values):
    """Returns the largest value from an array of values."""
    
    # Local variable
    maximum = values[0]
    
    # Loop from second element for each value in array
    for index in range(1, len(values)):
        
        # Check current value is more than current maximum
        if values[index] > maximum:
            
            # Update maximum
            maximum = values[index]
    
    # Return smallest
    return maximum


def count(values, target):
    """Counts the number of target values in the array of values.  Returns an integer."""
    
    # Local variables
    count = 0
    
    # Loop for each value in array
    for index in range(len(values)):
        
        # Check current value and target
        if values[index] == target:
            
            # Increment count
            count = count + 1
    
    # Return result
    return count
