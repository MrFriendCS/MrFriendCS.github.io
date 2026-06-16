# Title: H-SDD-Standard Algorithms
# Author: Mr Friend
# Date: 16 Jun 2026

#
# Sub-programs
#

def searchString(values: list[str], target: str) -> bool:
    """Linear search.  Returns True if target value is in list of values,
       otherwise returns False.
       """
    
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


def findMinReal(values: list[float]) -> float:
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


def findMaxInt(values: list[int]) -> int:
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


def countString(values: list[str], target: str) -> int:
    """Counts the number of target values in the array of values."""
    
    # Local variables
    countFound = 0
    
    # Loop for each value in array
    for index in range(len(values)):
        
        # Check current value and target
        if values[index] == target:
            
            # Increment count
            countFound = countFound + 1
    
    # Return result
    return countFound
