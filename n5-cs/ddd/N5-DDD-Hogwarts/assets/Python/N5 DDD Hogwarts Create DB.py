# Title: N5 DDD Hogwarts Create DB
# Author: Mr Friend
# Date: 10 May 2026

# Get extra code
import sqlite3


def houseTable():

    def dropTable():
        
        # SQL query
        dropTable = '''
        DROP TABLE IF EXISTS House;
        '''

        # Drop the table
        cursor.execute(dropTable)


    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE House (
        id INT NOT NULL,
        name VARCHAR(20) NOT NULL,
        guidanceTeacher VARCHAR(30),
        emblem VARCHAR(10) NOT NULL,
        colour VARCHAR(20) NOT NULL,
        PRIMARY KEY (id)
        );'''

        # Create the new table
        cursor.execute(createTable)


    def insertData():
        
        line = ''
        data = []
        values = ''
        
        file = open('../CSV/House.csv', 'r', encoding='utf-8')
        
        # Read header
        line = file.readline()
        
        # Read first line
        line = file.readline()
        
        # Loop for each record
        while line != '':
            
            # Split data
            data = line.split(',')
            
            # Extract values
            id = data[0].strip()
            name = data[1].strip()
            guidance = data[2].strip()
            emblem = data[3].strip()
            colour = data[4].strip()
            
            # Check for NULL values
            if guidance == '':
                guidance = 'NULL'
            else:
                guidance = f'"{guidance}"'
            
            # Create data            
            values = f'({id},"{name}",{guidance},"{emblem}","{colour}")'
            
            # SQL to insert data
            newData = f'INSERT INTO House VALUES {values};'
            
            # Insert new data
            cursor.execute(newData)

            # Commit the new data
            conn.commit()
            
            # Read next line
            line = file.readline()
    
    
    dropTable()
    createTable()
    insertData()


def subjectTable():
    
    def dropTable():
        
        # SQL query
        dropTable = '''
        DROP TABLE IF EXISTS Subject;
        '''

        # Drop the table
        cursor.execute(dropTable)

    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE Subject (
        id VARCHAR(5) NOT NULL,
        name VARCHAR(30) NOT NULL,
        PRIMARY KEY (id)
        );'''

        # Create the new table
        cursor.execute(createTable)


    def insertData():
        
        line = ''
        data = []
        values = ''
        
        file = open('../CSV/Subject.csv', 'r', encoding='utf-8')
        
        # Read header
        line = file.readline()
        
        # Read first line
        line = file.readline()
        
        # Loop for each record
        while line != '':
            
            # Split data
            data = line.split(',')
            
            # Extract values
            id = data[0].strip()
            name = data[1].strip()
            
            # Create data
            values = f'("{id}","{name}")'
            
            # SQL to insert data
            newData = f'INSERT INTO Subject VALUES {values};'
            
            # Insert new data
            cursor.execute(newData)

            # Commit the new data
            conn.commit()
            
            # Read next line
            line = file.readline()
    
    
    dropTable()
    createTable()
    insertData()


def pupilTable():
    
    def dropTable():
        
        # SQL query
        dropTable = '''
        DROP TABLE IF EXISTS Pupil;
        '''

        # Drop the table
        cursor.execute(dropTable)


    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE Pupil (
        id INT NOT NULL,
        lastName VARCHAR(30) NOT NULL,
        firstName VARCHAR(20) NOT NULL,
        houseID INT NOT NULL,
        year VARCHAR(2) NOT NULL
            CHECK (year IN ("S1", "S2", "S3", "S4", "S5", "S6")),
        age INT NOT NULL
            CHECK (age >= 11 AND age <= 18),
        PRIMARY KEY (id),
        FOREIGN KEY (houseID)
            REFERENCES House (id)
        );'''

        # Create the new table
        cursor.execute(createTable)


    def insertData():
        
        line = ''
        data = []
        values = ''
        
        file = open('../CSV/Pupil.csv', 'r', encoding='utf-8')
        
        # Read header
        line = file.readline()
        
        # Read first line
        line = file.readline()
        
        # Loop for each record
        while line != '':
            
            # Split data
            data = line.split(',')
            
            # Extract values
            id = data[0].strip()
            lastName = data[1].strip()
            firstName = data[2].strip()
            houseID = data[3].strip()
            year = data[4].strip()
            age = data[5].strip()
            
            # Create data
            values = f'({id},"{lastName}","{firstName}",{houseID},' \
                     + f'"{year}",{age})'
            
            # SQL to insert data
            newData = f'INSERT INTO Pupil VALUES {values};'
            
            # Insert new data
            cursor.execute(newData)

            # Commit the new data
            conn.commit()
            
            # Read next line
            line = file.readline()
    
    
    dropTable()
    createTable()
    insertData()


def resultTable():
    
    def dropTable():
        
        # SQL query
        dropTable = '''
        DROP TABLE IF EXISTS Result;
        '''

        # Drop the table
        cursor.execute(dropTable)


    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE Result (
        pupilID INT NOT NULL,
        subjectID VARCHAR(5) NOT NULL,
        grade VARCHAR(10),
        PRIMARY KEY (pupilID, subjectID),
        FOREIGN KEY (pupilID)
            REFERENCES Pupil (id),
        FOREIGN KEY (subjectID)
            REFERENCES Subject (id)
        );'''

        # Create the new table
        cursor.execute(createTable)


    def insertData():
        
        line = ''
        data = []
        values = ''
        
        file = open('../CSV/Result.csv', 'r', encoding='utf-8')
        
        # Read header
        line = file.readline()
        
        # Read first line
        line = file.readline()
        
        # Loop for each record
        while line != '':
            
            # Split data
            data = line.split(',')
            
            # Extract values
            pupilID = data[0].strip()
            subjectID = data[1].strip()
            grade = data[2].strip()
            
            # Check for NULL values
            if grade == '':
                grade = 'NULL'
            else:
                grade = f'"{grade}"'
            
            # Create data
            values = f'({pupilID},"{subjectID}",{grade})'
            
            # SQL to insert data
            newData = f'INSERT INTO Result VALUES {values};'
            
            # Insert new data
            cursor.execute(newData)

            # Commit the new data
            conn.commit()
            
            # Read next line
            line = file.readline()
    
    
    dropTable()
    createTable()
    insertData()


#
# Main program
#

# Create a connection to a database
# Creates a new database file, if it doesn’t exist
conn = sqlite3.connect('../Hogwarts.db')

# Create a database cursor
cursor = conn.cursor()


# House table
print(" 1. House table")
houseTable()

# Subject table
print(" 2. Subject table")
subjectTable()

# Pupil table
print(" 3. Pupil table")
pupilTable()

# Result table
print(" 4. Result table")
resultTable()


# Close the connection to the database
conn.close()
