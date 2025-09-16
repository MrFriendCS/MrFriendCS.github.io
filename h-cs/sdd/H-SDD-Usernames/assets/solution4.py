# Title: H SDD - Usernames Part 4
# Author: Mr Friend
# Date: 16 Sep 2025


# Get extra code
from dataclasses import dataclass


@dataclass
class Student:
    """A record to represent a student."""
    
    firstName: str = ""
    lastName: str = ""
    insuranceNo: str = ""


def readData():
    """Read data from csv file.  Returns an array of records."""
    
    # Initialise local variables
    line = ""
    data = [""] * 3
    students = [Student() for index in range(100)]
    
    # Open connection to file
    file = open("students.csv", "r")
    
    # Loop for each student
    for index in range(len(students)):
        
        # Read a line
        line = file.readline()
        
        # Split line
        data = line.split(",")
        
        # Assign data to record
        students[index].firstName = data[0].strip()
        students[index].lastName = data[1].strip()
        students[index].insuranceNo = data[2].strip()
        
    # Close connection to file
    file.close()
        
    # Return array of records
    return students


def createUsernames(students):
    """Create usernames for students.  Return an array."""
    
    # Initialise local variables
    usernames = [""] * len(students)
    part1 = ""
    part2 = ""
    part3 = ""
    username = ""
    
    # Loop for each student
    for index in range(len(students)):
        
        # Extract username parts
        part1 = left(students[index].firstName, 3)
        part2 = right(students[index].lastName, 3)
        part3 = mid(students[index].insuranceNo, 4, 3)
              
        # Put username parts together
        username = part1 + part2 + part3
        
        # Ensure lowercase
        username = lower(username)
        
        # Assign to array
        usernames[index] = username
    
    # Return array
    return usernames
    

def left(text, characters):
    """Left substring function."""
    
    # Initialise local variable
    left = ""
    
    # Create substring
    left = text[ :characters]
    
    # Return substring
    return left


def right(text, characters):
    """Right substring function."""
    
    # Initialise local variable
    right = ""
    
    # Create substring
    right = text[-characters: ]
    
    # Return substring
    return right


def mid(text, start, characters):
    """Mid substring function."""
    
    # Initialise local variable
    mid = ""
    
    # Create substring
    mid = text[start-1:start-1+characters]
    
    # Return substring
    return mid


def lower(text):
    """Changes all uppercase letters to lower case.  Returns a string."""
    
    # Initialise local variables
    word = ""
    ascii = 0
    
    # Loop for each letter
    for letter in text:
        
        # Get ASCII value
        ascii = ord(letter)
        
        # Check if uppercase
        if ascii >= 65 and ascii <= 90:
            
            # Convert to lowercase
            ascii = ascii + 32
            
            # Add letter
            word = word + chr(ascii)
            
        else:
            
            # Add letter
            word = word + letter
        
    # Return word
    return word


def writeData(usernames):
    """Write the usernames to text file."""
    
    # Make connection to text file
    file = open("usernames.txt", "w")
        
    # Loop for each username
    for username in usernames:
        
        file.write(username + "\n")
        
    # Close connection to file
    file.close()


#
# Main program
#

def main():
    
    # Intialise global variables
    students = [Student() for index in range(100)]
    usernames = [""] * len(students)
    
    # 1. Read the student data from a csv file
    students = readData()
    print(students[-1])
    
    # 2. Create the usernames
    usernames = createUsernames(students)
    
    # 3. Write the usernames to a text file
    writeData(usernames)
    
    

# Call main program
main()