# Title: Create N5 Santa Data
# Author: Mr Friend
# Date: 18 Dec 2024

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
start2 = "D:\\OneDrive - Glow Scotland\\"

folder1 = "GitHub\\MrFriendCS.github.io\\"
folder2 = "SQA - CS - N5\\DDD\\Database Files\\"  # Definately N5 folder


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
    forenames = []
    surnames = []
    
    if school:
        location = start1 + folder2
    else:
        location = start2 + folder2
        
    file = open(location + "naughtyList.csv", "r")
    
    line = file.readline()  # ignore header
    line = file.readline()
    
    while line != "":
        
        data = line.split(",")
        
        forenames = forenames + [data[0].strip()]
        surnames = surnames + [data[1].strip()]
        
        line = file.readline()
    
    return forenames, surnames


def createChildData(count, naughtyFirst, naughtyLast):
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
    
    # Loop for each child
    for index in range(count):
        children[index].childID = index + 1
        children[index].first = DDDhelper.getForename()
        children[index].last = DDDhelper.getSurname()
        
        while (children[index].first in naughtyFirst and
               children[index].last in naughtyLast):
            children[index].first = DDDhelper.getForename()
            children[index].last = DDDhelper.getSurname()
     
    return children


def createGiftData(noOfKids):
    """Create the data for the gift entity.  Two gifts each."""
    
    
    @dataclass
    class Gift:
        """A record to represent a gift."""
        giftID: int = 0
        childID: int = 0
        gift: str = ""
        cost: float = 0.0
        
    # Initialise local variables
    listOfGifts = []
    listOfCosts = []
    gifts = [Gift() for index in range(noOfKids * 2)]
    
        
    # Get Gift data
    
    fileIn = open("../CSV files/GiftList.csv", "r")
    
    line = fileIn.readline()  # Ignore heading row
    line = fileIn.readline()


    while line != "":
    
        data = line.split(",")
        
        listOfGifts = listOfGifts + [data[0].strip()]
        listOfCosts = listOfCosts + [data[1].strip()]
        
        line = fileIn.readline()
        
    fileIn.close()
    
    
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
            giftIndex = random.randint(0, len(listOfGifts)-1)
            
            # Populate record
            gifts[index].giftID = giftID
            gifts[index].childID = childID
            gifts[index].gift = listOfGifts[giftIndex]
            gifts[index].cost = listOfCosts[giftIndex]
            
            # Increment giftID
            giftID = giftID + 1
        
        # Second half of gifts
        offset = noOfKids


    return gifts


def naughtyKids(children, gifts, naughtyFirst, naughtyLast):
    """Find naughty children and update all their gifts."""
     
    # List of numbers 
    naughtyIDs = []
    
    # Pick index positions of naughty children
    #naughtyIDs = random.sample(naughtyNumbers, k=len(naughtyFirst))

    # Loop for each naughty child
    for index in range(len(children)):
        
        if children[index].first in naughtyFirst:
            children[index].nice = False
            naughtyIDs = naughtyIDs + [index+1]
    
    print(naughtyIDs)

    """
    pointer = 0
    
    # Loop for each naughty child
    for index in range(len(children)):
        
        if children[index].childID in naughtyIDs:
            children[index].first = naughtyFirst[pointer]
            children[index].last = naughtyLast[pointer]
            children[index].nice = False
            
            pointer = pointer + 1
    """
    
    
    
    # Loop for each gift - Set to coal
    for index in range(len(gifts)):
        
        if gifts[index].childID in naughtyIDs:
            gifts[index].gift = "Lump of coal"
            gifts[index].cost = 0.50
            
                      
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
    file.write("giftID,childID,gift,cost\n")
    
    # Loop for each gift
    for gift in gifts:
        file.write(str(gift.giftID) + ",")
        file.write(str(gift.childID) + ",")
        file.write(    gift.gift + ",")
        file.write(str(gift.cost) + "\n")
        
    file.close()


def main():
    """Main program."""

    # Initialise variables
    noOfKids = 200
    
    # 0 - Get names of naughty children
    naughtyFirst, naughtyLast = getNaughtyList()

    
    # 1 - Create child table data
    children = createChildData(noOfKids, naughtyFirst, naughtyLast)
    
    # 2 - Create gift table data
    gifts = createGiftData(noOfKids)
    
    # 3 - Add 'naughty' children (maybe)
    if input("Include naughty children (y/n)? ") == "y":
        
        children, gifts = naughtyKids(children, gifts, naughtyFirst, naughtyLast)
    
    # 4 - Write child table
    writeChildCSV(children)
    
    # 5 - Write gift table
    writeGiftCSV(gifts)


# Call main()
main()
