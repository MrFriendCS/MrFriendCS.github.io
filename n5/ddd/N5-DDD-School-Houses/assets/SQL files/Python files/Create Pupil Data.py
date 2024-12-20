# Title: Create School House Pupil Table Data
# Author: Mr Friend
# Date: 20 Dec 2024

"""
Create the data and export as CSV.
Seperate list of pupils used to overwrite random records.
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


def getLocalPupils():
    """Read in forenames and surnames of pupils."""
    
    # Initialise local variables
    pupils = []
    
    if school:
        location = start1 + folder2
    else:
        location = start2 + folder2
        
    file = open(location + "naughtyList.csv", "r")
    
    line = file.readline()  # ignore header
    line = file.readline()
    
    while line != "":
        
        data = line.split(",")
        
        forename = data[0].strip()
        surname =  data[1].strip()
        
        pupils = pupils + [[forename, surname]]
        
        line = file.readline()
    
    return pupils


def createPupilData(count, localPupils):
    """Create the data for the pupil table."""
    
    
    @dataclass
    class Pupil:
        """Record to represent a pupil."""
        id: int = 0
        surname: str = ""
        forename: str = ""
        house: int = 0
        year: str = ""
        age: int = 0
        
        
    
    # Initialise local variables
    pupils = [Pupil() for index in range(count)]
    forename = ""
    surname = ""
    
    # Loop for each child
    for index in range(count):
        pupils[index].id = index + 1
        
        forename = DDDhelper.getForename()
        surname = DDDhelper.getSurname()
        
        while [forename, surname] in localPupils:
            forename = DDDhelper.getForename()
            surname = DDDhelper.getSurname()
            
        pupils[index].forename = forename
        pupils[index].surname = surname
        pupils[index].house = DDDhelper.getNumber(1, 4)
        pupils[index].year = DDDhelper.getSchoolYear()
        pupils[index].age = 11 + int(pupils[index].year[-1])
    
    
    # pupilID 93 used in a task - wrong age
    pupils[92].forename = "Sally"
    pupils[92].surname = "Holby"
    pupils[92].year = "S4"
    pupils[92].age = 11
    
    # pupilID 205 used in a task - wrong name and year
    pupils[204].forename = "Colin"
    pupils[204].surname = "Fifth"
    pupils[204].year = "S5"
    pupils[204].age = 13
    
    # pupilID 278 used in a task - a Muggle!
    pupils[277].forename = "John"
    pupils[277].surname = "Bull"
    pupils[277].year = "S1"
    pupils[277].age = 11
        
     
    return pupils


def addPupils(pupils, localPupils):
    """Find naughty children and update all their gifts."""
     
    # Initialise local variables
    pupilIDs = []
    pupilNumbers = [index for index in range(0, len(pupils))]
    
    
    # Pick index positions of naughty children
    pupilIDs = random.sample(pupilNumbers, k=len(localPupils))
    
    # pupilID 93 and 205 used in a task
    while 92 in pupilIDs or 204 in pupilIDs or 277 in pupilIDs:
        pupilIDs = random.sample(pupilNumbers, k=len(localPupils))
    
    # Replace 'nice' children with 'naughty' children
    for index in range(len(pupilIDs)):
        
        pupils[pupilIDs[index]].forename = localPupils[index][0]
        pupils[pupilIDs[index]].surname = localPupils[index][1]
        pupils[pupilIDs[index]].house = 4
            
                      
    return pupils


def writeChildCSV(pupils):
    """Create CSV file for data."""
    
    file = open("../CSV files/Pupil.csv", "w")
    
    # Headers
    file.write("id,lastName,firstName,house,year,age\n")

    # Loop for each child
    for pupil in pupils:
        
        file.write(str(pupil.id) + ",")
        file.write(    pupil.surname + ",")
        file.write(    pupil.forename + ",")
        file.write(str(pupil.house) + ",")
        file.write(    pupil.year + ",")
        file.write(str(pupil.age))
        file.write("\n")
        
    file.close()
        

def main():
    """Main program."""

    # Initialise variables
    noOfPupils = 300
    localPupils = []
    addLocal = False
    
    
    if input("Include local pupils (y/n)? ") == "y":
        addLocal = True
    
    # 1 - Get names of pupils (maybe)
    if addLocal:
       localPupils = getLocalPupils()

    # 2 - Create child table data
    pupils = createPupilData(noOfPupils, localPupils)
    
    # 3 - Add 'naughty' children (maybe)
    if addLocal: 
        pupils = addPupils(pupils, localPupils)
    
    # 4 - Write child table
    writeChildCSV(pupils)


# Call main()
main()


