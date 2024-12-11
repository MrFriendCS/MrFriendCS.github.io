# Title: N5-DDD-Prison
# Author: Mr Friend
# Date: 6 Oct 2024

"""
Create the data and export as CSV file.
Seperate list of convicts used to overwrite random records.
"""

# Import Extra Code
import sys
from dataclasses import dataclass


# Find DDDhelper file
shool = "C:\\Users\\afriend1r\\AppData\\Local\\Programs\\Thonny"

start1 = "C:\\Users\\afriend1r"
start2 = "D:"

end = "\\OneDrive - Glow Scotland\\GitHub\\MrFriendCS.github.io"

# Check if directory exists
if shool in sys.path:
    # School laptop
    sys.path.append(start1 + end)
    
else:
    # Personel laptop
    sys.path.append(start2 + end)

# Get extra code
import DDDhelper


def getIDs(count):
    """ Creates a list of IDs."""
    
    # Initialise local variables
    id = 0
    min = 1000000
    max = 5000000
    tempList = [0] * count
    
    # Loop for each
    for index in range(count):
        
        # Pick random ID
        id = DDDhelper.getNumber(min, max)
        
        while id in tempList:
            
            # Pick a new random ID
            id = DDDhelper.getNumber(min, max)
            
        tempList[index] = id
        
    # Return list
    return tempList


def getSurnames(count):
    """Create list of surnames."""
    
    # Initialise local variable    
    tempList = [""] * count
    
    # Loop for each surname
    for index in range(count):
        tempList[index] = DDDhelper.getSurname()
        
    # Return list
    return tempList


def getForenames(count):
    """Create list of forenames."""
    
    # Initialise local variable
    tempList = [""] * count
    
    # Loop for each forename
    for index in range(count):
        tempList[index] = DDDhelper.getForename()
        
    # Return list
    return tempList


def getHairColours(count):
    """Create list of hair colours."""
    
    # Initialise local variable    
    tempList = [""] * count
    
    # Loop for each 
    for index in range(count):
        tempList[index] = DDDhelper.getHair()
        
    # Return list
    return tempList


def getEyeColours(count):
    """Create list of eye colours."""
    
    # Initialise local variables    
    tempList = [""] * count
    
    # Loop for each 
    for index in range(count):
        tempList[index] = DDDhelper.getEye()
        
    # Return list
    return tempList


def getHeights(count):
    """Create list of heights."""
    
    # Initilise local variables
    min = 130
    max = 250
    heights = [0.0] * count
    
    # Loop for each
    for index in range(count):
        heights[index] = DDDhelper.getNumber(min, max) / 100
    
    # Return list
    return heights
    

def getConvictions(count):
    """Create list of convictions."""
    
    # Initialise local variable
    tempList = [""] * count
    
    # Loop for each 
    for index in range(count):
        tempList[index] = DDDhelper.getConviction()
        
    # Return list
    return tempList


def getOpens(count):
    """Creates a Boolean list (0, 1)."""
    
    # Initialise local variable
    tempList = [True] * count
    
    # Loop for each
    for index in range(count):
        
        # Pick value
        tempList[index] = DDDhelper.getTrue(70)
            
    return tempList


def getDOBs(count):
    """Create list of dates."""
    
    # Initialise local variables
    tempList = [""] * count
    
    # Loop for each
    for index in range(count):
        
        tempList[index] = DDDhelper.getDate(1960, 2004)
        
    return tempList


def getPupils():
    """Read pupil names from pupilList.csv"""
    
    # Initialise local variables
    forenames = []
    surnames = []
    
    # Open file
    file = open("pupilList.csv", "r")
    
    # Read first line
    line = file.readline()
    
    # Loop for each line
    while line != "":
        
        names = line.split(",")
        
        forenames += [names[0].strip()]
        surnames += [names[1].strip()]
        
        # Read next line
        line = file.readline()
    
    # Close file
    file.close()
            
    return forenames, surnames


def updateNames(forenames, surnames, pupilFirsts, pupilLasts):
    """Update names to ensure each pupil is a 'prisoner'."""
    
    # Get extra code
    import random
    
    # Create list of index values
    numbers = [i for i in range(len(forenames)-1)]
    
    # Pick index positions
    positions = random.sample(numbers, k=len(pupilFirsts))
    
    # Loop for each
    for index in range(len(pupilFirsts)):
        
        forenames[positions[index]] = pupilFirsts[index]
        surnames[positions[index]] = pupilLasts[index]
  
    # Return updated lists
    return forenames, surnames


def writeCSV(a, b, c, d, e, f, g, h, i):
    """Create prisoner CSV file."""
    
    file = open("../CSV files/Prisoner.csv", "w")
    
    
    # Loop for each prisoner
    for index in range(len(a)):
        file.write(str(a[index]) + ",")
        file.write(    b[index] + ",")
        file.write(    c[index] + ",")
        file.write(    d[index] + ",")
        file.write(    e[index] + ",")
        file.write(str(f[index]) + ",")
        file.write(    g[index] + ",")
        file.write(str(h[index]) + ",")
        file.write(    i[index] + "\n")
        
    file.close()


def main():
    """Main program."""

    # Initialise variables
    noOfPrisoners = 200 

    # 1 - Get IDs
    ids = getIDs(noOfPrisoners)

    # 2 - Get surnames
    surnames = getSurnames(noOfPrisoners)

    # 3 - Get forename
    forenames = getForenames(noOfPrisoners)
    
    # 4 - Get hair colours
    hairs = getHairColours(noOfPrisoners)
    
    # 5 - Get eye colurs
    eyes = getEyeColours(noOfPrisoners)
    
    # 6 - Get eye colurs
    heights = getHeights(noOfPrisoners)
    
    # 7 - Get convictions
    convictions = getConvictions(noOfPrisoners)
    
    # 8 - Get open prisons
    opens = getOpens(noOfPrisoners)
    
    # 9 - Get DOBs
    dobs = getDOBs(noOfPrisoners)

    # 10 - Get pupil names
    #pupilFirsts, pupilLasts = getPupils()
    
    # 11 = Update names
    #forenames, surnames = updateNames(forenames, surnames, pupilFirsts, pupilLasts)

    # 12 - Write prisoner table
    writeCSV(ids, surnames, forenames, hairs, eyes,
                       heights, convictions, opens, dobs)


# Call main()
main()
