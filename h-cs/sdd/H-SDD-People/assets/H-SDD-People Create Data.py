# Title: H-SDD-People Create Data
# Author: Mr Friend
# Date: 3 Oct 2024

import sys

school = "C:\\Users\\afriend1r\\AppData\\Local\\Programs\\Thonny"

start1 = "C:\\Users\\afriend1r"
start2 = "D:"

end = "\\OneDrive - Glow Scotland\\SQA - CS - N5\\DDD\\Database Files\\Modules"

# Check if directory exists
if school in sys.path:
    # School laptop
    sys.path.append(start1 + end)
    
else:
    # Personel laptop
    sys.path.append(start2 + end)


import DDDhelper

from dataclasses import dataclass

@dataclass
class tempRecord:
    
    forename: str = ""
    surname: str = ""
    age: str = ""


tempArray = [tempRecord() for i in range(100)]

# Create data
for index in range(len(tempArray)):

    tempArray[index].forename = DDDhelper.getForename()
    tempArray[index].surname = DDDhelper.getSurname()
    tempArray[index].age = DDDhelper.getNumber()


# Write customer data to file
fileOut = open("people.csv", "w")

for index in range(len(tempArray)):
    
    fileOut.write(tempArray[index].forename + ",")
    fileOut.write(tempArray[index].surname + ",")
    fileOut.write(str(tempArray[index].age) + "\n")

fileOut.close()
