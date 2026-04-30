# Title: H DDD Create Practise DB
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
    dob DATE CHECK(dob LIKE "____-__-__"),
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


def dropVaccineTable():
    
    # SQL query
    dropTable = '''
    DROP TABLE IF EXISTS Vaccine;
    '''

    # Drop the table
    cursor.execute(dropTable)

def createVaccineTable():
    
    # SQL query
    createTable = '''CREATE TABLE Vaccine (
    vaxID INTEGER NOT NULL
        CHECK(vaxID >= 1),
    name TEXT NOT NULL,
    cost REAL NOT NULL
        CHECK (cost >= 0),
    PRIMARY KEY(vaxID)
    );'''

    # Create the new table
    cursor.execute(createTable)


def insertVaccineData():
    
    line = ''
    data = []
    values = ''
    file = open('../CSV/Pet.csv',     'r', encoding='utf-8')
    file = open('../CSV/Vaccine.csv', 'r', encoding='utf-8')
    
    # Read header
    line = file.readline()
    
    # Read first line
    line = file.readline()
    
    # Loop for each record
    while line != '':
        
        # Split data
        data = line.split(',')
        
        vaxID = data[0].strip()
        name = data[1].strip()
        cost = data[2].strip()
        
        # Create data
        values = f'({vaxID},"{name}","{cost}")'
        
        # SQL to insert data
        newData = f'INSERT INTO Vaccine VALUES {values};'
        
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
    petID INTEGER NOT NULL,
    vaxID INTEGER NOT NULL,
    vaxDate DATE NOT NULL
        CHECK (vaxDate LIKE "____-__-__"),
    reaction BOOL DEFAULT FALSE
        CHECK (reaction IN (0, 1)),
    paid BOOL DEFAULT FALSE
        CHECK (paid IN (0, 1)),
    PRIMARY KEY(vaxID, petID, vaxDate),
    FOREIGN KEY(petID) REFERENCES Pet(petID),
    FOREIGN KEY(vaxID) REFERENCES Vaccine(vaxID)
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
        
        petID = data[0].strip()
        vaxID = data[1].strip()
        vaxDate = data[2].strip()
        reaction = data[3].strip()
        paid = data[4].strip()
        
        # Create data
        values = f'({petID},{vaxID},"{vaxDate}",{reaction},{paid})'
        
        # SQL to insert data
        newData = f'INSERT INTO Vaccination VALUES {values};'
        
        # Insert new data
        cursor.execute(newData)

        # Commit the new data
        conn.commit()
        
        # Read next line
        line = file.readline()
        
    # Close connection to file
    file.close()


#
# Main program
#

# Create a connection to a database
# Creates a new database file, if it doesn’t exist
conn = sqlite3.connect('../H-CS-Database.db')

# Create a database cursor
cursor = conn.cursor()


# Pet table
print("1. Pet table")
dropPetTable()
createPetTable()
insertPetData()


# Vaccine table
print("2. Vaccine table")
dropVaccineTable()
createVaccineTable()
insertVaccineData()


# Vaccination table
print("3. Vaccination table")
dropVaccinationTable()
createVaccinationTable()
insertVaccinationData()


# Close the connection to the database
conn.close()
