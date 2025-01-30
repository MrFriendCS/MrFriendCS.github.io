# Title: H CS 2023 Task 1B
# Author: Mr Friend
# Date: 5 Feb 2023

#
# Functions and Procedures
#

def getData():
    '''
    Read data from file into parallel arrays
    '''

    # Declare local variables and arrays
    line = ""
    tempArray = [""] * 5
    
    length = 26
    attractions = [""] * length
    categories = [""] * length
    visitors = [0] * length
    daysOpen = [0] * length
    heights = [""] * length

    # Open file
    file = open("attractions.csv" ,"r" )

    # Loop for each line
    for index in range(len(attractions)):
        
        # Read line
        line = file.readline()

        # Split the line
        tempArray = line.split(",")

        # Assign values to parallel arrays
        attractions[index] = tempArray[0].strip()
        categories[index] = tempArray[1].strip()
        visitors[index] = int(tempArray[2].strip())
        daysOpen[index] = int(tempArray[3].strip())
        heights[index] = tempArray[4].strip()
        
    # Close file
    file.close()

    # Return data
    return attractions, categories, visitors, daysOpen, heights


def displayPopular(attractions, visitors):
    '''
    Find and display the names of the least visited and most visited attractions
    '''

    # Declare local variables
    minValue = 0
    maxValue = 0

    # Set min and max to first attaraction
    minValue = visitors[0]
    maxValue = visitors[0]

    # Loop for each attarction
    for index in range(1, len(attractions)):

        # Check min
        if visitors[index] < minValue:
            # Update min
            minValue = visitors[index]

        # Check max
        if visitors[index] > maxValue:
            # Update max
            maxValue = visitors[index]
        
    # Display least popular attraction(s)
    print("Least popular attraction(s):\n")

    # Loop for each attraction
    for index in range(len(attractions)):
        if visitors[index] == minValue:
            print(attractions[index])

    # Display most popular attraction(s)
    print("\nMost popular attraction(s):\n")

    # Loop for each attraction
    for index in range(len(attractions)):
        if visitors[index] == maxValue:
            print(attractions[index])


def serviceDue(attractions, categories, daysOpen):
    '''
    Write to file the names of roller coasters that need a service within 7 days
    '''

    # Declare local variables
    days = 0

    # 3.1 Create ‘service.csv’ file
    file = open("service.csv", "w")
    
    # 3.2 Loop for each attraction
    for index in range(len(attractions)):
    
        # 3.3 If current category is ‘Roller Coaster’ then
        if categories[index] == "Roller Coaster":
    
            # 3.4 Set days to current daysOpen modulus 90
            days = daysOpen[index] % 90
    
            # 3.5 If (90 – days) is less than or equal to 7 then
            if (90 - days) <= 7:
    
                # 3.6 Write current attraction to file
                file.write(attractions[index] + "\n")
    
            # 3.7 End if
        # 3.8 End if
    # 3.9 End loop

    # 3.10  Close ‘service.csv’ file
    file.close()

def findHeight(heights):
    '''
    Find attarctions with a height restriction of 1.0m and above
    '''

    # Declare local variable
    count = 0

    # Loop for each attraction
    for index in range(len(heights)):

        # if first character is a '1' then
        if heights[index][0] == "1":

            # Increment count
            count = count + 1

    # Display result
    print("\nThere are " + str(count) + " attractions with a height restriction of 1.0m or above.")
    

#
# Main Program
#

# Declare global variable and arrays
length = 26
attraction = [""] * length
category = [""] * length
visitors = [0] * length
daysOpen = [0] * length
height = [""] * length

# 1. Read data from file in parallel arrays
attraction, category, visitors, daysOpen, height = getData()

# 2. Find and display the names of the least
#      visited and most visited attractions
displayPopular(attraction, visitors)

# 3. Write to file the names of roller coasters
#      that need a service within 7 days
serviceDue(attraction, category, daysOpen)

# 4. Find attarctions with a height restriction
#      of 1.0m and above
findHeight(height)
