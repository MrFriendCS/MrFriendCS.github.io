# Title: Create Datatypes
# Author: Mr Friend
# Date: 28 Sep 2024

"""
Create the data and export as SQL statements to build table.
"""

# Import
import random


def getIDs(count):
    """Create a list of IDs."""
    
    # Initialise local variables
    tempList = [0] * count
    
    # Loop for each
    for index in range(count):
            
        tempList[index] = index + 1
        
    # Return list
    return tempList


def getTexts(noOfRows):
    """Create list of colours."""
    
    # Initialise local variables
    # Khaki and Mauve spelt intentionally incorrect.
    colours = ["Aquamarine", "Blue", "Crimson", "Fuscia", "Goldenred",
               "Green", "Indigo", "Khake", "Maroon", "Mauv", "Orange",
               "Pink", "Puce", "Purple", "Red", "Teal", "Turquoise",
               "Violet", "Yellow"]
    
    tempList = [""] * noOfRows
    
    # Loop for each row
    for index in range(noOfRows):
        tempList[index] = random.choice(colours)
        
    # Return list
    return tempList


def getIntegers(noOfRows):
    """Create a list of integers."""
    
    # Initilise local variables
    min = 0
    max = 100
    tempList = [0] * noOfRows
    
    # Loop for each row
    for index in range(noOfRows):
        tempList[index] = random.randint(min, max)
    
    # Return list
    return tempList


def getReals(noOfRows):
    """Create a list of real values"""
    
    # Initilise local variables
    min = 100
    max = 250
    tempList = [0.0] * noOfRows
    
    # Loop for each
    for index in range(noOfRows):
        tempList[index] = random.randint(min, max) / 100
    
    # Return list
    return tempList


def getDates(noOfRows):
    """Create a list of dates."""
    
    # Initialise local variables
    tempList = [""] * noOfRows
    
    # Loop for each
    for index in range(noOfRows):
        
        # Pick values
        year = random.randint(1900, 2024)
        month = random.randint(1, 12)
        day = random.randint(1, 30)
        
        if month == 2 and day > 28:
            
            # Pick a new day
            day = random.randint(1, 28)
        
        if month < 10:
            # Add leading zero
            monthStr = "0" + str(month)
        else:
            # Cast to string
            monthStr = str(month)
        
        if day < 10:
            # Add leading zero
            dayStr = "0" + str(day)
        else:
            # Cast to string
            dayStr = str(day)
        
        tempList[index] = str(year) + "-" + monthStr + "-" + dayStr
        
    return tempList

def getTimes(noOfRows):
    """Create a list of times."""
    
    # Initialise local variables
    tempList = [""] * noOfRows
    
    # Loop for each
    for index in range(noOfRows):
        
        # Pick values
        hour = random.randint(8, 15)
        mins = random.randint(0, 59)
        secs = random.randint(0, 59)
        
        if hour < 10:
            # Add leading zero
            hourStr = "0" + str(hour)
        else:
            # Cast to string
            hourStr = str(hour)
        
        if mins < 10:
            # Add leading zero
            minsStr = "0" + str(mins)
        else:
            # Cast to string
            minsStr = str(mins)
        
        if secs < 10:
            # Add leading zero
            secsStr = "0" + str(secs)
        else:
            # Cast to string
            secsStr = str(secs)
        
        tempList[index] = hourStr + ":" + minsStr + ":" + secsStr
        
    return tempList


def getBooleans(noOfRows):
    """Create a list of Boolean values (0, 1)."""
    
    # Initialise local variable
    value = 0
    tempList = [1] * noOfRows
    
    # Loop for each
    for index in range(noOfRows):
        
        # Pick value
        value = random.randint(1, 10)
        
        # 30% chance
        if value > 7:
            
            # Update value
            tempList[index] = 0
            
    return tempList


def writeTable(a, b, c, d, e, f, g):
    
    file = open("..\\Datatypes.sql", "w")
    
    # SQL - Create table
    
    file.write("CREATE TABLE Datatypes (\n")
    file.write("    rowID INT NOT NULL UNIQUE,\n")
    file.write("    colour VARCHAR(10)\n")
    file.write("        CHECK(LENGTH(colour) >= 3),\n")
    file.write("    score INT\n")
    file.write("        CHECK(score >= 0 AND score <= 100),\n")
    file.write("    height FLOAT NOT NULL\n")
    file.write("        CHECK(height >= 1.0 AND height <= 2.5),\n")
    file.write("    dob DATE\n")
    file.write("        CHECK(dob >= \"1900-01-01\" AND dob <= \"2024-12-31\"),\n")
    file.write("    start TIME\n")
    file.write("        CHECK(start >= \"08:00:00\" AND start <= \"16:00:00\"),\n")
    file.write("    nice BOOLEAN NOT NULL,\n")
    file.write("    PRIMARY KEY (rowID)\n")
    file.write(");\n\n")
    
    # SQL - Create values
    
    # Loop for each prisoner
    for index in range(len(a)):
        file.write("INSERT INTO Datatypes VALUES (")
        file.write(str(a[index]) + ",")
        file.write("\"" + b[index] + "\",")
        file.write(str(c[index]) + ",")
        file.write(str(d[index]) + ",")
        file.write("\"" + e[index] + "\",")
        file.write("\"" + f[index] + "\",")
        file.write(str(g[index]) + ");\n")
        
    file.close()


def main():
    """Main program."""

    # Initialise variables
    noOfRows = 50 

    # 1 - Get row IDs
    ids = getIDs(noOfRows)

    # 2 - Get text - colours
    texts = getTexts(noOfRows)

    # 3 - Get integers
    integers = getIntegers(noOfRows)
    
    # 4 - Get decimals
    reals = getReals(noOfRows)
    
    # 5 - Get dates
    dates = getDates(noOfRows)
    
    # 6 - Get times
    times = getTimes(noOfRows)
    
    # 7 - Get Boolean values
    booleans = getBooleans(noOfRows)
    
    # 8 - Write table
    writeTable(ids, texts, integers, reals, dates, times, booleans)


# Call main()
main()
