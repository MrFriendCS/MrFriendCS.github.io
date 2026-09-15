# Title: H SDD Bearings v1
# Author: Mr Friend
# Date: 15 Sep 2026

#
# Subprograms
#

def getSizeData() -> list[float]:
    """Read ball bearing test data from a csv file.  Return array."""

    # Declare local variables
    bearingSizes: list[float] = [0.0 for _ in range(1000)]
    line: str = ""
    
    # Open file in read mode
    file = open("bearingsData.csv", "r", encoding="UTF-8")

    # Loop for each value
    for index in range(len(bearingSizes)):
                       
        # Read a line of data
        line = file.readline()

        bearingSizes[index] = float(line.strip())

    # Close the file
    file.close()

    return bearingSizes


def findMin(items: list[float]) -> float:
    """Finds and returns minimum value in an array."""
    
    # Initialise local variable
    minSize: float = 0.0
    
    # Set min to first value in array
    minSize = items[0]
    
    # Loop from second element
    for index in range(1, len(items)):
        
        # Compare current value with min
        if items[index] < minSize:
            
            # Update min
            minSize = items[index]
            
    # Return minimum value
    return minSize


def findMax(items: list[float]) -> float:
    """Finds and returns maximum value in an array."""
    
    # Initialise local variable
    maxSize: float = 0.0
    
    # Set max to first value in array
    maxSize = items[0]
    
    # Loop from second element
    for index in range(1, len(items)):
        
        # Compare current value with min
        if items[index] > maxSize:
            
            # Update min
            maxSize = items[index]
            
    # Return maximum value
    return maxSize


def countSmall(items: list[float]) -> int:
    """Count and return how many ball bearings are too big."""

    # Initialise local variables
    count: int = 0
    minSize: float = 2.99

    # Loop for each value
    for index in range(len(items)):
        
        # Copare value
        if items[index] < minSize:
            count = count + 1
    
    return count


def countBig(items: list[float]) -> int:
    """Count and return how many ball bearings are too big."""

    # Initialise local variables
    count: int = 0
    maxSize: float = 3.01

    # Loop for each value
    for index in range(len(items)):
        
        # Copare value
        if items[index] > maxSize:
            count = count + 1
    
    return count


def calcPercent(count: int) -> float:
    """Calculate percentage of small/big bearings to 2 dp."""
    
    # Initialise local variable
    percent: float = 0.0
    
    # Calculate percentage
    percent = (count / 1000) * 100
    
    # Round to 2 dp
    percent = round(percent, 2)
    
    return percent


def calcBatchResult (smallPercent: float, bigPercent: float) -> bool:
    """Calculate result of batch.  Returns Boolean."""
    
    # Initialise local variable
    totalPercent: float = 0.0
    result: bool = False
    
    # Calculate total percent
    totalPercent = smallPercent + bigPercent
    
    # Determine result
    if smallPercent < 2 and bigPercent < 2 and totalPercent < 3:
        
        # Update result
        result = True
    
    return result


def writeData(min: float, max: float, smallPercent: float,
              bigPercent: float, result: bool) -> None:
    """Write data to file."""
    
    # Initialise local variables
    totalPercent: float = 0.0
    
    # Calculate total percentage
    totalPercent = smallPercent + bigPercent
        
    # Open file in write mode
    file = open("batchResult.txt", "w", encoding="UTF-8")
    
    # Write header
    file.write("Batch Result\n")
    file.write("------------\n\n")
    
    # Write counts
    file.write("Min:   " + str(min) + " cm\n")
    file.write("Max:   " + str(max) + " cm\n\n")
    
    
    # Write counts
    file.write("Too small: " + str(smallPercent) + "%\n")
    file.write("Too big:   " + str(bigPercent) + "%\n")
    file.write("Total:     " + str(totalPercent) + "%\n\n")
    
    # Write result
    if result:
        file.write("PASS" + "\n")
    else:
        file.write("FAIL" + "\n")
    
    # Write footer
    file.write("====" + "\n")
    
    # Close file
    file.close()
    

def main() -> None:
    """Main program"""

    # Initialise variables
    sizeData: list[float] = [0.0 for _ in range(1000)]
    minSize: float = 0.0
    maxSize: float = 0.0
    small: int = 0
    big: int = 0
    smallPercent: float = 0.0
    bigPercent: float = 0.0
    result: bool = False

    # 1.  Read bearings sizes from file
    sizeData = getSizeData()
    
    # 2.  Determine size of smallest bearing                                      
    minSize = findMin(sizeData)
    
    # 3.  Determine size of largest bearing                                      
    maxSize = findMax(sizeData)

    # 4.  Calculate how many bearings are too small
    small = countSmall(sizeData)

    # 5.  Calculate how many bearings are too big
    big = countBig(sizeData)

    # 6.  Calculate percentage of small bearings, 2 dp
    smallPercent = calcPercent(small)

    # 7.  Calculate percentage of big bearings, 2 dp
    bigPercent = calcPercent(big)
    
    # 8.  Calculate batch result
    result = calcBatchResult(smallPercent, bigPercent)

    # 9.  Write data to file
    writeData(minSize, maxSize, smallPercent, bigPercent, result)
    
# Call main()
#main()
