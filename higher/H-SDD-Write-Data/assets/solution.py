# Title: H SDD Writing
# Author: Mr Friend
# Date: 17 Sep 2024

#
# Subprograms
#

def randomData(length):
    """Creates three parallel arrays containing random values."""
    
    # Import module
    import random
    
    # Initialise local variables
    upperArray = [""] * length
    numberArray = [""] * length
    lowerArray = [""] * length
    
    # Populate arrays with data
    for index in range(length):
        
        # Uppercase character
        upperArray[index] = chr(random.randint(65, 90))
        
        # Single digit: 0-9
        numberArray[index] = random.randint(0, 9)
        
        # Lowercase character
        lowerArray[index] = chr(random.randint(97, 122))
        
    return upperArray, numberArray, lowerArray
        
    
def writeData(upperArray, numberArray, lowerArray):
    """Writes three parallel arrays to csv file."""
    
    # Connect to file - write mode
    file = open("randomData.csv", "w")
    
    # Loop for each value
    for index in range(len(upperArray)):
        
        file.write(upperArray[index] + ",")
        file.write(str(numberArray[index]) + ",")
        file.write(lowerArray[index] + "\n")
        
    # Close connection to file
    file.close()
    
    
def main():
    """Main program"""
     
    # Initialise variable
    length = 0
    
    # Get length of arrays from user
    length = int(input("How many values? "))
    
    # Initialise arrays
    uppers = [""] * length
    numbers = [0] * length
    lowers = [""] * length
    
    # Get random data
    uppers, numbers, lowers = randomData(length)
    
    # Write data to file
    writeData(uppers, numbers, lowers)
    

# Call main program
main()