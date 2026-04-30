# Title: N5 DDD Create Practise DB
# Author: Mr Friend
# Date: 30 Apr 2026

# Get extra code
import sqlite3


def dropPetTable():
    
    # SQL query
    dropTable = '''
    DROP TABLE IF EXISTS Pet;
    '''

    # Drop the table
    cursor.execute(dropTable)


def createPetTable():
    
    # SQL query
    createTable = '''CREATE TABLE Pet (
    petID INTEGER NOT NULL
        CHECK(petID >= 1),
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    dob TEXT CHECK(dob LIKE "____-__-__"),
    PRIMARY KEY(petID)
    );'''

    # Create the new table
    cursor.execute(createTable)


def insertPetData():
    
    line = ''
    data = []
    values = ''
    
    file = open('../CSV/Pet.csv', 'r', encoding='utf-8')
    
    # Read header
    line = file.readline()
    
    # Read first line
    line = file.readline()
    
    # Loop for each record
    while line != '':
        
        # Split data
        data = line.split(',')
        
        petID = data[0].strip()
        name = data[1].strip()
        species = data[2].strip()
        dob = data[3].strip()
        
        # Create data
        values = f'({petID},"{name}","{species}","{dob}")'
        
        # SQL to insert data
        newData = f'INSERT INTO Pet VALUES {values};'
        
        # Insert new data
        cursor.execute(newData)

        # Commit the new data
        conn.commit()
        
        # Read next line
        line = file.readline()
        
    # Close connection to file
    file.close()


def dropVaccinationTable():
    
    # SQL query
    dropTable = '''
    DROP TABLE IF EXISTS Vaccination;
    '''

    # Drop the table
    cursor.execute(dropTable)


def createVaccinationTable():
    
    # SQL query
    createTable = '''CREATE TABLE Vaccination (
    vaxID INTEGER NOT NULL,
    petID INTEGER NOT NULL,
    vaxDate TEXT NOT NULL
        CHECK (vaxDate LIKE "____-__-__"),
    vaxType TEXT NOT NULL,
    reaction BOOL DEFAULT FALSE
        CHECK (reaction IN (0, 1)),
    PRIMARY KEY(vaxID),
    FOREIGN KEY(petID) REFERENCES Pet(petID)
    );'''

    # Create the new table
    cursor.execute(createTable)


def insertVaccinationData():
    
    line = ''
    data = []
    values = ''
    
    file = open('../CSV/Vaccination.csv', 'r', encoding='utf-8')
    
    # Read header
    line = file.readline()
    
    # Read first line
    line = file.readline()
    
    # Loop for each record
    while line != '':
        
        # Split data
        data = line.split(',')
        
        vaxID = data[0].strip()
        petID = data[1].strip()
        vaxDate = data[2].strip()
        vaxType = data[3].strip()
        reaction = data[4].strip()
        
        # Create data
        values = f'({vaxID},{petID},"{vaxDate}","{vaxType}",{reaction})'
             
        # SQL to insert data
        newData = 'INSERT INTO Vaccination VALUES' + values + ';'
        
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
conn = sqlite3.connect('../N5-CS-Database.db')

# Create a database cursor
cursor = conn.cursor()


# Pet table
print("1. Pet table")
dropPetTable()
createPetTable()
insertPetData()


# Vaccination table
print("2. Vaccination table")
dropVaccinationTable()
createVaccinationTable()
insertVaccinationData()


# Close the connection to the database
conn.close()
