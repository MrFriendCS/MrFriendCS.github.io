# Title: Create Santa Data
# Author: Mr Friend
# Date: 15 Dec 2025

"""
Create the data and export as CSV.
Seperate list of naughty children used to overwrite random records.
Naughty children are removed from the gift list, as they don't deserve them!
"""

# Import Extra Code
import sys
from dataclasses import dataclass
import random


# Find DDDhelper file
shool = "C:\\Users\\afriend1r\\AppData\\Local\\Programs\\Thonny"

start1 = "C:\\Users\\afriend1r\\OneDrive - Glow Scotland\\"
start2 = "C:\\Users\\alfri\\OneDrive - Glow Scotland\\"

folder1 = "GitHub\\MrFriendCS.github.io\\"
folder2 = "GitHub\\"


# Check if directory exists
if shool in sys.path:
    # School laptop
    sys.path.append(start1 + folder1)
    school = True
    
else:
    # Personal laptop
    sys.path.append(start2 + folder1)
    school = False


# Get extra code
import DDDhelper


def getNaughtyList():
    """Read in forenames and surnames of naughty children."""
    
    # Initialise local variables
    naughtyList = []
    
    if school:
        location = start1 + folder2
    else:
        location = start2 + folder2
        
    file = open(location + "pupilList.csv", "r")
    
    line = file.readline()  # ignore header
    line = file.readline()
    
    while line != "":
        
        data = line.split(",")
        
        forename = data[0].strip()
        surname =  data[1].strip()
        
        naughtyList = naughtyList + [[forename, surname]]
        
        line = file.readline()
    
    return naughtyList


def createChildData(count, naughtyList):
    """Create the data for the child table,
    apart from nice as all children are nice."""
    
    
    @dataclass
    class Child:
        """Record to represent a child."""
        childID: int = 0
        first: str = ""
        last: str = ""
        nice: bool = True
        
    
    # Initialise local variables
    children = [Child() for index in range(count)]
    forename = ""
    surname = ""
    
    # Loop for each child
    for index in range(count):
        children[index].childID = index + 1
        
        forename = DDDhelper.getForename()
        surname = DDDhelper.getSurname()
        
        while [forename, surname] in naughtyList:
            forename = DDDhelper.getForename()
            surname = DDDhelper.getSurname()
            
        children[index].first = forename
        children[index].last = surname
     
    return children


def createGiftData(noOfKids):
    """Create the data for the gift entity.  Two gifts each."""
    
    
    @dataclass
    class Gift:
        """A record to represent a gift."""
        giftID: int = 0
        childID: int = 0
        toyID: int = 0
        
    # Initialise local variables
    gifts = [Gift() for index in range(noOfKids * 2)]
        
    # Set initial giftID value    
    giftID = 1
        
    # First half of gifts
    offset = 0
    
    # Loop twice - two gifts each child
    for loop in range(2):
        
        childIDs = [index for index in range(1, noOfKids+1)]
        
        # Loop for each child
        for index in range(offset, offset+noOfKids):
            
            # Pick a random child
            childID = random.choice(childIDs)
            
            # Remove childID from list
            childIDs.remove(childID)
            
            # Pick a random gift
            toyID = random.randint(1, 19)
            
            # Populate record
            gifts[index].giftID = giftID
            gifts[index].childID = childID
            gifts[index].toyID = toyID
            
            # Increment giftID
            giftID = giftID + 1
        
        # Second half of gifts
        offset = noOfKids
        
    
    # Remove children and give their gifts to other children
    removeIDs = [[47, 73], [119, 158]]
    extraIDs = [56, 81]
    
    # Loop twice
    for loop in range(len(extraIDs)):
    
        # Loop for each gift
        for index in range(len(gifts)):
            
            if gifts[index].childID in removeIDs[loop]:
                gifts[index].childID = extraIDs[loop]
        

    return gifts


def naughtyKids(children, gifts, naughtyList):
    """Find naughty children and update all their gifts."""
     
    # Initialise local variables
    naughtyIDs = []
    naughtyNumbers = [index for index in range(0, len(children))]
    
    
    # Pick index positions of naughty children
    naughtyIDs = random.sample(naughtyNumbers, k=len(naughtyList))
    
    # childID 172 used in a task
    while 171 in naughtyIDs:
        naughtyIDs = random.sample(naughtyNumbers, k=len(naughtyList))
    
    # Replace 'nice' children with 'naughty' children
    for index in range(len(naughtyIDs)):
        
        children[naughtyIDs[index]].first = naughtyList[index][0]
        children[naughtyIDs[index]].last = naughtyList[index][1]
        children[naughtyIDs[index]].nice = False
        
   
    # Convert naughtyIDs to childIDs
    for index in range(len(naughtyIDs)):
        naughtyIDs[index] = naughtyIDs[index] + 1
    
    
    # Loop for each gift - Set to coal
    for index in range(len(gifts)):
        
        if gifts[index].childID in naughtyIDs:
            gifts[index].toyID = 0
            
                      
    return children, gifts


def writeChildCSV(children):
    """Create CSV file for data."""
    
    file = open("../CSV files/Child.csv", "w")
    
    # Headers
    file.write("childID,firstName,lastName,nice\n")

    # Loop for each child
    for child in children:
        
        file.write(str(child.childID) + ",")
        file.write(    child.first + ",")
        file.write(    child.last + ",")
        file.write(str(child.nice).upper() +"\n")
        
    file.close()
        

def writeGiftCSV(gifts):
    """Create CSV file for data."""
    
    file = open("../CSV files/Gift.csv", "w")
    
    # Headers
    file.write("giftID,childID,toyID\n")
    
    # Loop for each gift
    for gift in gifts:
        file.write(str(gift.giftID) + ",")
        file.write(str(gift.childID) + ",")
        file.write(str(gift.toyID) + "\n")
        
    file.close()


def main():
    """Main program."""

    # Initialise variables
    noOfKids = 200
    naughtyList = []
    naughty = False
    
    
    if input("Include naughty children (y/n)? ") == "y":
        naughty = True
    
    # 0 - Get names of naughty children (maybe)
    if naughty:
        
        naughtyList = getNaughtyList()

    
    # 1 - Create child table data
    children = createChildData(noOfKids, naughtyList)
    
    # 2 - Create gift table data
    gifts = createGiftData(noOfKids)
    
    # 3 - Add 'naughty' children (maybe)
    if naughty:
        
        children, gifts = naughtyKids(children, gifts, naughtyList)
    
    # 4 - Write child table
    writeChildCSV(children)
    
    # 5 - Write gift table
    writeGiftCSV(gifts)


# Call main()
main()


