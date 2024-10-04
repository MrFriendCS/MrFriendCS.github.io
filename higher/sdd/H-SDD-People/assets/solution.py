# Title: H-SDD-People Solution
# Author: Mr Friend
# Date: 3 Oct 2024

# Import code
from dataclasses import dataclass


# Define record
@dataclass
class Person:
    """A record to represent a person."""
    first: str = ""
    last: str = ""
    age: int = 0


def getData():
    """Reads data into array of records."""
    
    # Create array of records
    people = [Person() for i in range(100)]

    # Make connection to file
    file = open("people.csv", "r")
    
    for index in range(len(people)):
        
        # Read a row of data
        line = file.readline()
        
        # Split row at commas
        data = line.split(",")
        
        # Assign data to current record
        people[index].first = data[0].strip()
        people[index].last = data[1].strip()
        people[index].age = int(data[2].strip())
        
    return people


def countMacs(people):
    """Count surnames that start with 'Mac' or 'Mc'."""
    
    # Initialise variables
    count = 0
    surname = ""
    
    # Loop for each record
    for index in range(len(people)):
        
        # Get surname
        surname = people[index].last
        
        # Count 'Mac' and 'Mc'
        if surname[:3] == "Mac" or surname[:2] == 2:
            
            # Increment count
            count = count + 1
            
    return count


def findOldest(people):
    """Find the age of the oldest person."""
    
    # Initialise local variables
    oldest = people[0].age
    
    # Loop for remaining people
    for index in range(1, len(people)):
        
        # Check if older
        if people[index].age > oldest:
            
            # Update oldest
            oldest = people[index].age
            
    return oldest


def saveResults(people, macs, oldest):
    """Write the results to file."""
    
    # Create file
    file = open("summary1871.txt", "w")
    
    file.write("Results\n")
    file.write("-------\n\n")
    
    file.write("There were " + str(macs) + " people ")
    file.write("with either 'Mac' or 'Mc' surnames.\n\n")
    
    file.write("The oldest was " + str(oldest) + ".\n\n")
    
    file.write("Oldest people:\n\n")
    
    # Loop to find oldest people
    for index in range(len(people)):
        
        # Check
        if people[index].age == oldest:
            
            # Save name
            file.write("\t" + people[index].first + " ")
            file.write(people[index].last + "\n")
    
    file.write("\n=======\n")
    
    # Close connection to file
    file.close()
    

def main():
    """Main program."""
    
    people = getData()
    
    macs = countMacs(people)
    
    oldest = findOldest(people)
    
    saveResults(people, macs, oldest)


# Call main()
main()

