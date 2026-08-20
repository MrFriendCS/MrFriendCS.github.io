# Title: Parallel Arrays
# Author: Mr Friend
# Date: 18 Jun 2024

#
# Sub-programs
#

def left(inputs: list[str]) -> list[str]:
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
capitals: list[str] = ["London", "Paris", "Berlin", "Oslo", "Madrid", "Rome"]
countries: list[str] = ["UK", "France", "Germany", "Norway", "Spain", "Italy"]
populations: list[float] = [66.8, 67.4, 83.2, 5.4, 46.8, 60.5]


# Pupils
forenames: list[str] = ["Aimee", "Stewart", "Aonghas", "James", "Kieran", "Callum", "Darren"]
surnames: list[str] = ["Campbell", "Ford", "MacDonald", "Smyth", "Young", "Robertson", "Walker"]
ages: list[int] = [17, 14, 16, 17, 13, 14, 12]

print(ages)
