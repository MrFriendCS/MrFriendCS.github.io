# Title: AH SDD Canteen
# Author: Mr Friend
# Date: 29 May 2026


# Locker class
from order import Order
from menu_item import Menu_Item


def readData() -> list:
    '''Read CSV data into an array of Locker objects.'''

    # Local variables
    contents = ''
    temp = []
    data = []
    arrayOfObjects = []
    isLocked = False

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
        lockerNo = int(data[0])
        pupilName = data[1]
        lock = int(data[2])
        
        # Check lock status
        if lock == 1:
            isLocked = True
        else:
            isLocked = False
        
        # Append new locker object to array
        arrayOfObjects.append(Locker(lockerNo, pupilName, isLocked))
        
    return arrayOfObjects



#
# Main program
#

item1 = Menu_Item('Sausage roll', 1.25)
item2 = Menu_Item('Ketchup sachet', 0.25)

order1 = Order()
order1.add_item(item1)
order1.add_item(item2)

order1.display_order()

print(f'£{order1.calculate_cost():.2f}')
