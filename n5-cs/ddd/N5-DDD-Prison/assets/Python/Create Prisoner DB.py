# Title: Create Prisoner DB
# Author: Mr Friend
# Date: 24 Apr 2026

# Get extra code
import sqlite3


def dropPrisonerTable():
    
    # SQL query
    dropTable = '''
    DROP TABLE IF EXISTS Prisoner;
    '''

    # Drop the table
    cursor.execute(dropTable)


def createPrisonerTable():
    
    # SQL query
    createTable = """CREATE TABLE Prisoner (
        prisonID INT NOT NULL,
        surname VARCHAR(30) NOT NULL 
            CHECK (LENGTH(surname) >= 3),
        forename VARCHAR(20) NOT NULL 
            CHECK (LENGTH(forename) >= 3),
        hair VARCHAR(6) 
            CHECK (hair IN ("Black", "Blond", "Brown", "Grey",
                            "None", "Red", "White")),
        eyes VARCHAR(5) 
            CHECK (eyes IN ("Amber", "Black", "Blue", "Brown",
                            "Green", "Hazel", "Grey")),
        height FLOAT NOT NULL
            CHECK (height >= 1.3
               AND height <= 2.5),
        conviction VARCHAR(20) NOT NULL,
        openPrison BOOLEAN NOT NULL
            CHECK (openPrison IN (0, 1)),
        dob DATE NOT NULL,
        PRIMARY KEY (prisonID)
    );"""

    # Create the new table
    cursor.execute(createTable)


def insertPrisonerData():
    
    line = ''
    data = []
    values = ''
    
    file = open('../CSV/Prisoner.csv', 'r', encoding='utf-8')
    
    # Read first line
    line = file.readline()
    
    # Loop for each record
    while line != '':
        
        # Split data
        data = line.split(',')
        
        prisonID = data[0].strip()
        surname = data[1].strip()
        forename = data[2].strip()
        hair = data[3].strip()
        eyes = data[4].strip()
        height = data[5].strip()
        conviction = data[6].strip()
        openPrison = data[7].strip()
        dob = data[8].strip()
        
        # Create data
        values = '("' + prisonID + '","' + surname + '","' + forename + '","' \
                 + hair + '","' + eyes + '",' +  height + ',"' +  conviction \
                 + '",'
        
        if openPrison == "True":
            values = values + "TRUE"
        else:
            values = values + "FALSE"
            
        values = values + ',"' + dob + '")'
        
        # SQL to insert data
        newData = 'INSERT INTO Prisoner VALUES' + values + ';'
        
        # Insert new data
        cursor.execute(newData)

        # Commit the new data
        conn.commit()
        
        # Read next line
        line = file.readline()


#
# Main program
#

# Create a connection to a database
# Creates a new database file, if it doesn’t exist
conn = sqlite3.connect('../Prison.db')

# Create a database cursor
cursor = conn.cursor()


# Prisoner table
print("1. Prisoner table")
dropPrisonerTable()
createPrisonerTable()
insertPrisonerData()


# Close the connection to the database
conn.close()