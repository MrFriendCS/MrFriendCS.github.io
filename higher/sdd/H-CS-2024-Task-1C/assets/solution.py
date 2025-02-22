# Title: Task 1 Part B
# Author: 
# Date: 3 Feb 2024

# Import code
from dataclasses import dataclass

#
# Sub-programs
#

def getData():
    """Read data and return parallel arrays"""

    # Initialise local variables
    names = [""] * 100
    workers = [0] * 100
    incomes = [0] * 100
    data = [""] * 3
    line = ""
    index = 0

    # Open connection to file
    file = open("companies.csv" ,"r" )

    # Read line from file
    line = file.readline()

    # Loop until all data read, or arrays full
    while line != "" and index < 100:

        # Split line at commas
        tempData = line.split(",")

        # Assign data to parallel arrays
        names[index] = data[0].strip()
        workers[index] = int(data[1].strip())
        incomes[index] = int(data[2].strip())

        # Read next line from file
        line = file.readline()
        
        # Increment index
        index = index + 1

    # Close connection to file
    file.close()

    # Return parallel arrays
    return names, workers, incomes


def findMaxPos(localArray):
    """Returns position of maximum value in an array."""

    # Initialise local variables
    position = 0
    max = 0

    # Set max to first value
    max = localArray[0]

    # Loop for each vaue from second value
    for index in range(1, len(localArray)):

        # New maximum?
        if localArray[index] > max:

            # Update values
            position = index
            max = localArray[index]

    # Return position of maximum value
    return position
    

def findSalaryDiff(names, incomes):
    """Find and display the difference between the chosen
       company’s CEO salary and the highest CEO salary."""

    # Initialise local variables
    company = ""
    maxPos = 0
    difference = 0

    # 2.1  Ask user to enter the name of chosen company
    name = input("Which comapny are you interest in? ")
    
    # 2.2  Set found to false
    found = False
    
    # 2.3  Set found position to -1
    foundPos = -1
    
    # 2.4  Call findMaxPos function to return the position of highest CEO salary
    maxPos = findMaxPos(incomes)
    
    # 2.5  Loop for each company
    for index in range(len(names)):
    
        # 2.6  If current company is the chosen company
        if names[index] == name:
    
            # 2.7  Set found to true
            found = True
    
            # 2.8  Set found position to current index
            foundPos = index
    
        # 2.9  End if
    
    # 2.10 End loop
    
    # 2.11 If chosen company name is in list
    if found == True:
    
        # 2.12 Calculate and store the difference between salaries
        difference = incomes[maxPos] - incomes[foundPos]
        
        # 2.13 Display message containing name of company with highest CEO salary
        print("Highest salary: " + names[maxPos]  + ", £" + str(incomes[maxPos]))
    
        # 2.14 Display the name of the chosen company, and difference in salaries
        print("Interested salary: " + names[foundPos]  + ", £" + str(difference) + " less")

    
    # 2.15 Else
    else:
    
        # 2.16 Display “Company not found”
        print("Company not found")
    
    # 2.17 End if


def findTop(workers):
    """Find and display the companies with top 10% of employees"""

    # Initialise local variables
    maxPos = 0

    # 3.1  Call findMaxPos function to return position of highest number of employees
    maxPos = findMaxPos(workers)

    # 3.2  Set count to 0
    count = 0

    # 3.3  Loop for each number of employees in array
    for index in range(len(workers)):

        # 3.4  If current employees is greater than or equal to maximum employees*0.9
        if workers[index] >= workers[maxPos] * 0.9:

            # 3.5  Set count to count + 1
            count = count + 1

        # 3.6  End If

    # 3.7  End Loop

    # 3.8  Display message showing number of companies that employ within 10% of the highest number of employees
    print("Count of top 10% of employees: " + str(count))


#
# Main Program
#

# Initialise global variables
companys = [""] * 100
numEmployees = [0] * 100
ceoSalary = [0] * 100

# 1 Read from file into parallel arrays.
# OUT: company(), numEmployees(), ceoSalary()
companys, numEmployees, ceoSalary = getData()

# 2 Find and display the difference between CEO salary.
# IN: company(), ceoSalary()
findSalaryDiff(companys, ceoSalary)

# 3 Find and display the companies with top 10% of employees
# IN: numEmployees()
findTop(numEmployees)
