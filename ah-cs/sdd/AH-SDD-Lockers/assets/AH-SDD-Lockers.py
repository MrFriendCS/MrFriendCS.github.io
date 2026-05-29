# Title: AH SDD Locker
# Author: Mr Friend
# Date: 29 May 2026


# Locker class
from locker import Locker


def read_data() -> list:
    """Read CSV data into an array of Locker objects."""

    # Local variables
    contents = ''
    temp = []
    data = []
    array_of_objects = []
    islocked = False

    # Connect to a file
    file = open('Lockers.csv', 'r', encoding='utf-8')

    # Read contents, remove end \n
    contents = file.read().strip()
    
    # Close the connection to the file
    file.close()

    # Split at newlines
    temp = contents.split('\n')

    # Loop for each object - Ignore first row
    for index in range(1, len(temp)):
        
        # Split data
        data = temp[index].split(',')
        
        # Extract values
        locker_no = int(data[0])
        pupil_name = data[1]
        lock = int(data[2])
        
        # Check lock status
        if lock == 1:
            islocked = True
        else:
            islocked = False
        
        # Append new locker object to array
        array_of_objects.append(Locker(locker_no, pupil_name, islocked))
        
    return array_of_objects


def find_locked(array_of_objects) -> list:
    """Procedure to find locked lockers, and return their numbers."""
    
    # Local variable
    lockers = []
    
    # Loop for each locker
    for locker in array_of_objects:
        
        current_locker = locker.details()
        
        if current_locker[2] == True:
            
            lockers = lockers + [current_locker[0]]
    
    return lockers


def find_locker_no(array_of_objects, pupil_name:str='') -> list:
    """Function find a pupil's locker number(s). """ \
        """Returns the locker number(s), or an empty array."""
    
    # Local variable
    lockers = []
    
    # Loop for each locker
    for locker in array_of_objects:
        
        # Get current locker details
        details = locker.details()
        
        # Compare pupil name
        if details[1] == pupil_name:
            
            # Assign lock number to array
            lockers = lockers + [details[1]]
    
    # Return locker number(s)
    return lockers


def assign_locker(array_of_objects, locker_no=-1,
                  pupil_name='') -> bool:
    """Assigns a locker to a pupil. """ \
        """Returns True if successful, else returns False."""
    
    # Local variables
    assigned = False
    index = 0
    
    # Loop for each locker until found
    while assigned == False and index < len(array_of_objects)-1:
        
        # Get current locker details
        current_locker = array_of_objects[index].details()
        
        # Compare locker number
        if current_locker[0] == locker_no:
            
            # Assign locker to pupil
            array_of_objects[index].assign(pupil_name)
            
            # Update assigned
            assigned = True
        
        # Increment index
        index += 1
    
    # Return result
    return assigned


#
# Main program
#

# Read data from file
objects = read_data()


find_locked(objects)

print(find_locker_no(objects, 'Jodie Whittaker'))

print(assign_locker(objects, 14,'Ncuti Gatwa'))

print(find_locker_no(objects, 'Ncuti Gatwa'))

print(find_locked(objects))
