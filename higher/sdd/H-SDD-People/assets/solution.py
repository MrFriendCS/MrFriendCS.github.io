# Title: H-SDD-People Solution
# Author: Mr Friend
# Date: 3 Oct 2024

# Import code
from dataclasses import dataclass


# Define record
@dataclass
class Person:
    first: str = ""
    last: str = ""
    age: int = 0
    
def getData():
    """Reads data into array of records."""
    
    # Create array of records
    people = (Person() for i in range(100))
    
    # Make connection to file
    file.open("people.csv", "r")
    
    for index in range(len(people)):
        
        # Read a row of data
        line = file.readline()
        
        # Split row at commas
        data = line.split(",")
        
        # Assign data to current record
        people[index].first = data[0].strip()
        people[index].last = data[1].strip()
        people[index].age = data[1].strip()
        
    