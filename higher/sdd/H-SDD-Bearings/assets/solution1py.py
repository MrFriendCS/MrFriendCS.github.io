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


def countTooBig(values):
    """Count and return how many ball bearings are too big."""

    # Initialise local variables
    count = 0
    maxSize = 3.01

    # Loop for each value
    for index in range(len(values)):
        
        # Copare value
        if values[index] > maxSize:
            count = count + 1
    
    return count


def countTooSmall(values):
    """Count and return how many ball bearings are too big."""

    # Initialise local variables
    count = 0
    minSize = 2.99

    # Loop for each value
    for index in range(len(values)):
        
        # Copare value
        if values[index] < minSize:
            count = count + 1
    
    return count


def writeResult(big, small):
    """Calculate the result and write to file."""
    
    # Initialise local variables
    result = "FAIL"
    bigPer = 0.0
    smallPer = 0.0
    totalPer = 0.0
    
    # Calculate percentages
    bigPer = (big / 1000) * 100
    smallPer = (small / 1000) * 100
    totalPer = bigPer + smallPer
        
    # Calculate result
    if bigPer < 3 and smallPer < 2 and totalPer < 3:
        
        # Set to pass
        result = "PASS"

    # Open file in write mode
    file = open("batchResult.txt", "w")
    
    # Write header
    file.write("Batch Result\n")
    file.write("------------\n\n")
    
    # Write counts
    file.write("Too big:   " + str(bigPer) + "%\n")
    file.write("Too small: " + str(smallPer) + "%\n")
    file.write("Total:     " + str(totalPer) + "%\n\n")
    
    # Write result
    file.write(result + "\n")
    
    # Write footer
    file.write("====" + "\n")
    
    # Close file
    file.close()
    

def main():
    """Main program"""

    # Initialise variables
    data = [0.0] * 1000
    tooBig = 0
    tooSmall = 0

    # 1.  Read bearings sizes from file
    sizeData = getSizeData()

    # 2.  Calculate how many bearings are too big
    tooBig = countTooBig(sizeData)
    
    # 3.  Calculate how many bearings are too small
    tooSmall = countTooSmall(sizeData)

    # 4.  Calculate the result and write to file
    writeResult(tooBig, tooSmall)
    
# Call main()
#main()
