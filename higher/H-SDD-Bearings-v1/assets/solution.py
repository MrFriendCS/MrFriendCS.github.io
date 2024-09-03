# Title: H SDD Barra Ball Bearings
# Author: Mr Friend
# Date: 6 Nov 2020

# Declare global variables
maxSize = 0.0
minSize = 0.0
sizeData = []
tooBig = 0
tooSmall = 0
batchResult = False

# Functions

def getMaxSize():
    # Get maximum allowed size of ball bearings

    # Declare local variable
    upperLimit = 0

    # Get value from user
    upperLimit = float(input("Enter the maximum size: "))

    # Check value and get a valid value from user
    while upperLimit < 0:
        upperLimit = float(input("Enter a valid maximum size: "))

    return upperLimit    

def getMinSize():
    # Get minimum size of ball bearings

    # Declare local variable
    lowerLimit = 0

    # Get value from user
    lowerLimit = float(input("Enter the minimum size: "))

    # Check value and get a valid value from user
    while lowerLimit < 0:
        lowerLimit = float(input("Enter a valid minimum size: "))

    return lowerLimit

def getSizeData():
    # Get the ball bearing test data from a csv file

    # Declare local variable
    bearingSize = []


    # Open file in read mode
    file = open("bearingBatch1.csv", "r")

    # Read the first line
    line = file.readline().strip()

    while line:
        
        bearingSize.append(float(line))

        # Read the next line
        line = file.readline().strip()

    # Close the file
    file.close()

    return bearingSize

def countTooBig(upperLimit, results):
    # Count how many ball bearings are too big

    # Declare local variable
    countBig = 0

    for index in range(len(results)):
        if results[index] > upperLimit:
            countBig = countBig + 1
    
    return countBig

def countTooSmall(lowerLimit, results):
    # Count how many ball bearings are too small

    # Declare local variable
    countSmall = 0

    for index in range(len(results)):
        if results[index] < lowerLimit:
            countSmall = countSmall + 1
    
    return countSmall

def getResult(countBig, countSmall):
    # Calculate if the batch passess
    # Batches are always of 1,000 ball bearings

    # Declare local variable
    result = False

    if (countBig < 50) and (countSmall < 50) and (countBig + countSmall < 70):
        result = True

    return result

def displayResult(result):
    # Display the result of the tests

    if result == True:
        print("The batch passes.")
    else:
        print("The batch failed - melt them down!")


# Main program

maxSize = getMaxSize()
minSize = getMinSize()

sizeData = getSizeData()

tooBig = countTooBig(maxSize, sizeData)
tooSmall = countTooSmall(minSize, sizeData)

batchResult = getResult(tooBig, tooSmall)
displayResult(batchResult)
