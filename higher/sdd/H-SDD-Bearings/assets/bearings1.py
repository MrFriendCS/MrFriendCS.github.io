# Title: H SDD Bearings v1
# Author: Mr Friend
# Date: 25 Sep 2024

#
# Subprograms
#

def getSizeData():
    """Read ball bearing test data from a csv file.  Return array."""

    # Declare local variable
    bearingSizes = [0.0] * 1000

    # Open file in read mode
    file = open("bearingsData.csv", "r")

    # Loop for each value
    for index in range(len(bearingSizes)):
                       
        # Read a line of data
        line = file.readline()

        bearingSizes[index] = float(line.strip())

    # Close the file
    file.close()

    return bearingSizes


def findMin(items):
    """Finds and returns minimum value in an array."""
    
    # Initialise local variable
    min = 0.0
    
    # Set min to first value in array
    min = items[0]
    
    # Loop from second element
    for index in range(1, len(items)):
        
        # Compare current value with min
        if items[index] < min:
            
            # Update min
            min = items[index]
            
    # Return minimum value
    return min


def findMax(items):
    """Finds and returns maximum value in an array."""
    
    # Initialise local variable
    max = 0.0
    
    # Set max to first value in array
    max = items[0]
    
    # Loop from second element
    for index in range(1, len(items)):
        
        # Compare current value with min
        if items[index] > max:
            
            # Update min
            max = items[index]
            
    # Return maximum value
    return max


def countSmall(items):
    """Count and return how many ball bearings are too big."""

    # Initialise local variables
    count = 0
    minSize = 2.99

    # Loop for each value
    for index in range(len(items)):
        
        # Copare value
        if items[index] <= minSize:
            count = count + 1
    
    return count


def countBig(items):
    """Count and return how many ball bearings are too big."""

    # Initialise local variables
    count = 0
    maxSize = 3.01

    # Loop for each value
    for index in range(len(items)):
        
        # Copare value
        if items[index] >= maxSize:
            count = count + 1
    
    return count


def calcResults (small, big):
    """Calculate result of batch.  Returns Boolean."""
    
    # Initialise local variables
    total = 0
    smallPer = 0.0
    bigPer = 0.0
    result = False
    
    # Calculate total
    total = small + big
    
    # Decide result
    if small < 20 and big < 20 and total < 30:
        
        # Update result
        result = True
    
    # Calculate percentages
    bigPer = (big / 1000) * 100
    smallPer = (small / 1000) * 100
    
    return smallPer, bigPer, result


def writeData(min, max, smallPer, bigPer, result):
    """Write data to file."""
    
    # Initialise local variables
    totalPer = 0.0
    
    # Calculate total percentage
    totalPer = bigPer + smallPer
        
    # Open file in write mode
    file = open("batchResult.txt", "w")
    
    # Write header
    file.write("Batch Result\n")
    file.write("------------\n\n")
    
    # Write counts
    file.write("Min:   " + str(min) + " cm\n")
    file.write("Max:   " + str(max) + " cm\n\n")
    
    
    # Write counts
    file.write("Too small: " + str(smallPer) + "%\n")
    file.write("Too big:   " + str(bigPer) + "%\n")
    file.write("Total:     " + str(totalPer) + "%\n\n")
    
    # Write result
    if result:
        file.write("PASS" + "\n")
    else:
        file.write("FAIL" + "\n")
    
    # Write footer
    file.write("====" + "\n")
    
    # Close file
    file.close()
    

def main():
    """Main program"""

    # Initialise variables
    sizeData = [0.0] * 1000
    min = 0.0
    max = 0.0
    small = 0
    big = 0
    smallPer = 0.0
    bigPer = 0.0
    result = False

    # 1.  Read bearings sizes from file
    sizeData = getSizeData()
    
    # 2.  Determine size of smallest bearing                                      
    min = findMin(sizeData)
    
    # 3.  Determine size of largest bearing                                      
    max = findMax(sizeData)

    # 4.  Calculate how many bearings are too small
    small = countSmall(sizeData)

    # 5.  Calculate how many bearings are too big
    big = countBig(sizeData)
    
    # 6.  Calculate batch result
    smallPer, bigPer, result = calcResults(small, big)

    # 7.  Write data to file
    writeData(min, max, smallPer, bigPer, result)
    
# Call main()
#main()
