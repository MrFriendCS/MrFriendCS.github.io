# Title: Parallel Arrays
# Author: Mr Friend
# Date: 18 Jun 2024

#
# Sub-programs
#

def left(inputs):
    """Creates an array of strings with the first three characters of each supplied string.  Returns an array."""
    
    # Local variables
    outputs = [""] * len(inputs)
    
    # Loop for each string in array
    for index in range(len(inputs)):
        
        # Create and store substring
        outputs[index] = inputs[index][ :3]
    
    # Return array of strings
    return outputs
    
    
#
# Main program
#

# Global variables

# Countries
capitals = ["London", "Paris", "Berlin", "Oslo", "Madrid", "Rome"]
countries = ["UK", "France", "Germany", "Norway", "Spain", "Italy"]
populations = [66.8, 67.4, 83.2, 5.4, 46.8, 60.5]


# Pupils
forenames = ["Aimee", "Stewart", "Aonghas", "James", "Kieran", "Callum", "Darren"]
surnames = ["Campbell", "Ford", "MacDonald", "Smyth", "Young", "Robertson", "Walker"]
ages = [17, 14, 16, 17, 13, 14, 12]
