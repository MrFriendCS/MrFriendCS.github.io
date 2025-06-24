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